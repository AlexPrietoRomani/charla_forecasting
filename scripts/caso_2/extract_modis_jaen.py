import pystac_client
import planetary_computer as pc
import rasterio
from rasterio.windows import from_bounds
from rasterio.warp import transform_bounds
import numpy as np
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
import datetime
import os
import sys

def process_item(item_dict):
    item_id = item_dict['id']
    dt_str = item_dict['datetime']
    assets = item_dict['assets']
    
    ndvi_href = assets['250m_16_days_NDVI']['href']
    evi_href = assets['250m_16_days_EVI']['href']
    rel_href = assets['250m_16_days_pixel_reliability']['href']
    
    try:
        with rasterio.open(ndvi_href) as s_ndvi, rasterio.open(evi_href) as s_evi, rasterio.open(rel_href) as s_rel:
            w_bounds = transform_bounds('EPSG:4326', s_ndvi.crs, -79.1, -5.8, -78.8, -5.6)
            win = from_bounds(*w_bounds, transform=s_ndvi.transform)
            
            rel_arr = s_rel.read(1, window=win)
            valid_mask = (rel_arr == 0) | (rel_arr == 1)
            n_valid = int(np.sum(valid_mask))
            total_px = int(rel_arr.size)
            
            if n_valid > 50:
                ndvi_arr = s_ndvi.read(1, window=win) * 0.0001
                evi_arr = s_evi.read(1, window=win) * 0.0001
                
                v_ndvi = ndvi_arr[valid_mask]
                v_evi = evi_arr[valid_mask]
                
                # filter out obvious bad values
                good_ndvi = v_ndvi[(v_ndvi > 0) & (v_ndvi <= 1)]
                good_evi = v_evi[(v_evi > 0) & (v_evi <= 1)]
                
                ndvi_med = float(np.median(good_ndvi)) if len(good_ndvi) > 0 else np.nan
                evi_med = float(np.median(good_evi)) if len(good_evi) > 0 else np.nan
            else:
                ndvi_med = np.nan
                evi_med = np.nan
                
            return {
                'item_id': item_id,
                'fecha': dt_str[:10],
                'ndvi_med': round(ndvi_med, 4) if not np.isnan(ndvi_med) else np.nan,
                'evi_med': round(evi_med, 4) if not np.isnan(evi_med) else np.nan,
                'n_validos': n_valid,
                'total_pixeles': total_px,
                'pct_valido': round(n_valid / total_px * 100.0, 1)
            }
    except Exception as e:
        return {'item_id': item_id, 'fecha': dt_str[:10], 'error': str(e)}

def main():
    print("Connecting to Planetary Computer STAC...")
    catalog = pystac_client.Client.open(
        "https://planetarycomputer.microsoft.com/api/stac/v1",
        modifier=pc.sign_inplace
    )
    
    # Search MODIS 16-day VI (Terra and Aqua) for 2000-2024
    print("Searching MOD13Q1 / MYD13Q1 items for Jaén (2000-2024)...")
    search = catalog.search(
        collections=["modis-13Q1-061"],
        bbox=[-79.1, -5.8, -78.8, -5.6],
        datetime="2000-01-01/2024-12-31"
    )
    items = list(search.items())
    print(f"Total MODIS items found: {len(items)}")
    
    # Filter Terra items for consistency (or use both)
    # Using Terra (MOD13Q1) covers 2000-2024 fully (Aqua started in 2002)
    terra_items = [it for it in items if it.id.startswith("MOD13Q1")]
    print(f"Terra (MOD13Q1) items: {len(terra_items)}")
    
    # Prepare metadata for items to pass to threads
    item_dicts = []
    for it in terra_items:
        # Resolve start date from item ID if datetime is None
        # Format: MOD13Q1.AYYYYDDD.h10v09...
        if it.datetime:
            dt = it.datetime
        else:
            parts = it.id.split('.')
            yr = int(parts[1][1:5])
            doy = int(parts[1][5:8])
            dt = datetime.datetime(yr, 1, 1) + datetime.timedelta(days=doy - 1)
            
        item_dicts.append({
            'id': it.id,
            'datetime': dt.strftime('%Y-%m-%d'),
            'assets': {
                '250m_16_days_NDVI': {'href': it.assets['250m_16_days_NDVI'].href},
                '250m_16_days_EVI': {'href': it.assets['250m_16_days_EVI'].href},
                '250m_16_days_pixel_reliability': {'href': it.assets['250m_16_days_pixel_reliability'].href}
            }
        })
        
    # Sort chronologically
    item_dicts.sort(key=lambda x: x['datetime'])
    
    results = []
    print("Extracting vegetation indices using 8 concurrent workers...")
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(process_item, it): it for it in item_dicts}
        done_cnt = 0
        for f in as_completed(futures):
            res = f.result()
            if 'error' not in res:
                results.append(res)
            done_cnt += 1
            if done_cnt % 50 == 0 or done_cnt == len(item_dicts):
                print(f"Progress: {done_cnt}/{len(item_dicts)} composites processed")
                
    df = pd.DataFrame(results)
    df.sort_values('fecha', inplace=True)
    df.reset_index(drop=True, inplace=True)
    
    out_file = 'data/raw/cafe_real/modis_jaen_16d.csv'
    df.to_csv(out_file, index=False)
    print(f"\nExtraction complete! Saved {len(df)} records to {out_file} (Size: {os.path.getsize(out_file)} bytes)")
    print(df.head(5))
    print(df.tail(5))
    print("\nSummary statistics:")
    print(df[['ndvi_med', 'evi_med', 'pct_valido']].describe())

if __name__ == '__main__':
    main()
