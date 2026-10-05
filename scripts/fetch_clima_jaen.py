import urllib.request
import ssl
import json
import pandas as pd
import os

lat, lon = -5.7049, -79.0104
start_date = '2000-01-01'
end_date = '2024-12-31'

url = (
    f"https://archive-api.open-meteo.com/v1/archive?"
    f"latitude={lat}&longitude={lon}&start_date={start_date}&end_date={end_date}&"
    f"daily=temperature_2m_max,temperature_2m_min,temperature_2m_mean,precipitation_sum,et0_fao_evapotranspiration,shortwave_radiation_sum&"
    f"timezone=America%2FLima"
)

print('Fetching ERA5 daily weather from Open-Meteo Archive for Jaén...')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx, timeout=60) as resp:
    data = json.loads(resp.read().decode('utf-8'))

daily = data['daily']
df = pd.DataFrame({
    'fecha': daily['time'],
    'tmax': daily['temperature_2m_max'],
    'tmin': daily['temperature_2m_min'],
    'tmean': daily['temperature_2m_mean'],
    'lluvia_mm': daily['precipitation_sum'],
    'et0_mm': daily['et0_fao_evapotranspiration'],
    'rad_mj_m2': daily['shortwave_radiation_sum']
})

output_file = 'data/raw/cafe_real/clima_jaen_diario.csv'
df.to_csv(output_file, index=False)
print(f'Saved {len(df)} daily weather records (2000-2024) to {output_file} (Size: {os.path.getsize(output_file)})')
print(df.head(5))
print(df.tail(5))
