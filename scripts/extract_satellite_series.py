"""
Extracción de serie histórica satelital (Sentinel-2 L2A) y agroclimática
para zona cafetalera de referencia (Jaén, Perú) usando la arquitectura de AgroVisión.
"""

import asyncio
import json
import logging
from pathlib import Path
import httpx
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("extract_satellite")

TOKEN_URL = "https://identity.dataspace.copernicus.eu/auth/realms/CDSE/protocol/openid-connect/token"
STATS_URL = "https://sh.dataspace.copernicus.eu/api/v1/statistics"
CLIENT_ID = "sh-62cd3506-dc81-4a93-8a1e-aab597e2930a"
CLIENT_SECRET = "CVOBs1YiF2Ncxn7NygcJaWiZRAAN0zwN"

# Coordenadas finca/zona cafetalera Jaén
LAT = -5.6766
LON = -78.7742
DELTA = 0.005  # ~500m buffer

GEOJSON = {
    "type": "Polygon",
    "coordinates": [[
        [LON - DELTA, LAT - DELTA],
        [LON + DELTA, LAT - DELTA],
        [LON + DELTA, LAT + DELTA],
        [LON - DELTA, LAT + DELTA],
        [LON - DELTA, LAT - DELTA],
    ]]
}

START_DATE = "2019-01-01T00:00:00Z"
END_DATE = "2025-12-31T23:59:59Z"

INDEX_CONFIG = {
    "ndvi": {
        "bands_sensor": ["B04", "B08", "SCL", "dataMask"],
        "formula": "(s.B08 - s.B04) / (s.B08 + s.B04)",
    },
    "evi": {
        "bands_sensor": ["B02", "B04", "B08", "SCL", "dataMask"],
        "formula": "2.5 * (s.B08 - s.B04) / (s.B08 + 6.0 * s.B04 - 7.5 * s.B02 + 1.0)",
    },
    "ndre": {
        "bands_sensor": ["B05", "B08", "SCL", "dataMask"],
        "formula": "(s.B08 - s.B05) / (s.B08 + s.B05)",
    },
    "ndwi": {
        "bands_sensor": ["B03", "B08", "SCL", "dataMask"],
        "formula": "(s.B03 - s.B08) / (s.B03 + s.B08)",
    },
}

def stats_evalscript(idx_name: str) -> str:
    cfg = INDEX_CONFIG[idx_name]
    formula = cfg["formula"]
    bands_json = json.dumps(cfg["bands_sensor"])
    return f"""//VERSION=3
function setup() {{
  return {{
    input: [{{bands: {bands_json}}}],
    output: [{{id: "{idx_name}", bands: 1}}, {{id: "dataMask", bands: 1}}]
  }};
}}
function evaluatePixel(s) {{
  let val = {formula};
  let cloudy = [3, 8, 9, 10, 11].indexOf(s.SCL) > -1;
  return {{{idx_name}: [val], dataMask: [cloudy ? 0 : s.dataMask]}};
}}"""

async def get_cdse_token() -> str:
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            TOKEN_URL,
            data={
                "grant_type": "client_credentials",
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
            },
            timeout=30.0,
        )
        resp.raise_for_status()
        return resp.json()["access_token"]

async def fetch_index_series(client: httpx.AsyncClient, token: str, idx_name: str) -> dict[str, float]:
    body = {
        "input": {
            "bounds": {
                "geometry": GEOJSON,
                "properties": {"crs": "http://www.opengis.net/def/crs/EPSG/0/4326"}
            },
            "data": [{"type": "sentinel-2-l2a"}]
        },
        "aggregation": {
            "timeRange": {"from": START_DATE, "to": END_DATE},
            "aggregationInterval": {"of": "P1M"},
            "evalscript": stats_evalscript(idx_name),
            "resx": 0.0001,
            "resy": 0.0001,
        }
    }
    logger.info(f"Consultando Statistical API para {idx_name.upper()}...")
    resp = await client.post(
        STATS_URL,
        headers={"Authorization": f"Bearer {token}"},
        json=body,
        timeout=120.0
    )
    resp.raise_for_status()
    data = resp.json().get("data", [])
    series = {}
    for item in data:
        month = item["interval"]["from"][:7] + "-01"
        stats = item.get("outputs", {}).get(idx_name, {}).get("bands", {}).get("B0", {}).get("stats", {})
        mean = stats.get("mean")
        if mean is not None and not isinstance(mean, str) and stats.get("sampleCount", 0) > 0:
            series[month] = round(float(mean), 4)
    return series

async def fetch_open_meteo_monthly() -> pd.DataFrame:
    logger.info("Consultando Open-Meteo Historical Archive...")
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": LAT,
        "longitude": LON,
        "start_date": "2019-01-01",
        "end_date": "2025-12-31",
        "daily": ["temperature_2m_mean", "temperature_2m_max", "temperature_2m_min", "precipitation_sum", "et0_fao_evapotranspiration"],
        "timezone": "America/Lima"
    }
    async with httpx.AsyncClient() as client:
        r = await client.get(url, params=params, timeout=30.0)
        r.raise_for_status()
        d = r.json().get("daily", {})
        df_daily = pd.DataFrame(d)
        df_daily["time"] = pd.to_datetime(df_daily["time"])
        df_daily["month"] = df_daily["time"].dt.to_period("M").dt.to_timestamp().dt.strftime("%Y-%m-%d")
        
        # Agregación mensual
        df_monthly = df_daily.groupby("month").agg({
            "temperature_2m_mean": "mean",
            "temperature_2m_max": "mean",
            "temperature_2m_min": "mean",
            "precipitation_sum": "sum",
            "et0_fao_evapotranspiration": "sum"
        }).reset_index()
        df_monthly.columns = ["fecha", "temp_media", "temp_max", "temp_min", "precip_total", "et0_total"]
        return df_monthly

async def main():
    token = await get_cdse_token()
    logger.info("Token CDSE obtenido.")

    async with httpx.AsyncClient() as client:
        indices = {}
        for idx in ["ndvi", "evi", "ndre", "ndwi"]:
            try:
                indices[idx] = await fetch_index_series(client, token, idx)
            except Exception as e:
                logger.error(f"Error consultando {idx}: {e}")

    # Clima mensual
    df_meteo = await fetch_open_meteo_monthly()

    # Consolidar
    all_months = df_meteo["fecha"].tolist()
    records = []
    for m in all_months:
        row = {"fecha": m}
        for idx in ["ndvi", "evi", "ndre", "ndwi"]:
            row[idx] = indices.get(idx, {}).get(m, None)
        records.append(row)
    
    df_indices = pd.DataFrame(records)
    df_merged = pd.merge(df_meteo, df_indices, on="fecha", how="left")

    # Interpolar huecos satelitales (por meses muy nublados)
    for col in ["ndvi", "evi", "ndre", "ndwi"]:
        df_merged[col] = df_merged[col].interpolate(method="linear").bfill().ffill()

    out_file = Path("data/raw/s2_spectral_indices.csv")
    out_file.parent.mkdir(parents=True, exist_ok=True)
    df_merged.to_csv(out_file, index=False)
    logger.info(f"Serie multiespectral guardada en: {out_file} ({len(df_merged)} meses)")

    # Archivo especifico para el hito T1.3 (s2_ndvi.csv)
    df_merged[["fecha", "ndvi", "evi", "temp_media", "precip_total"]].to_csv("data/raw/s2_ndvi.csv", index=False)
    logger.info("Hito T1.3 cumplido: guardado data/raw/s2_ndvi.csv")

if __name__ == "__main__":
    asyncio.run(main())
