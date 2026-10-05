
import os
import json
import pandas as pd

def build_deck():
    bench_df = pd.read_csv('data/benchmark_punchana.csv')
    forecast_7d_df = pd.read_csv('data/senamhi_forecast_7d.csv')
    extrap_df = pd.read_csv('data/experimento_extrapolacion.csv')
    cafe_camp_df = pd.read_csv('data/cafe_jaen_campanias.csv')
    cafe_res_df = pd.read_csv('data/cafe_jaen_resultados.csv')
    noaa_ecmwf_df = pd.read_csv('data/noaa_ecmwf_forecast.csv')
    
    with open('data/cafe_jaen_hipotesis.json', 'r', encoding='utf-8') as f:
        hipotesis_cafe = json.load(f)

    senamhi_diario_df = pd.read_csv('data/senamhi_diario.csv')
    senamhi_sub = senamhi_diario_df.tail(180).to_dict(orient='records')

    def clean_nans(obj):
        if isinstance(obj, float) and (pd.isna(obj) or obj != obj):
            return None
        elif isinstance(obj, dict):
            return {k: clean_nans(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [clean_nans(v) for v in obj]
        return obj

    raw_payload = {
        'benchmark': bench_df.to_dict(orient='records'),
        'forecast_7d': forecast_7d_df.to_dict(orient='records'),
        'extrapolacion': extrap_df.to_dict(orient='records'),
        'cafe_campanias': cafe_camp_df.to_dict(orient='records'),
        'cafe_resultados': cafe_res_df.to_dict(orient='records'),
        'hipotesis_cafe': hipotesis_cafe,
        'noaa_ecmwf': noaa_ecmwf_df.to_dict(orient='records'),
        'senamhi_reciente': senamhi_sub
    }
    data_payload = clean_nans(raw_payload)
    print('Payload prepared successfully with', len(data_payload), 'keys')

build_deck()
