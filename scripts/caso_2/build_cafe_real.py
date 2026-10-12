"""
Compilación del dataset consolidado del Caso B: data/caso_2/cafe_jaen_campanias.csv.
100% determinista, cero números aleatorios, trazabilidad total a data/raw/cafe_real/.

Fuentes primarias integradas:
1. Rendimiento y Cosecha oficial: INEI Compendio Estadístico Cajamarca 2017 y 2025 (data/raw/cafe_real/midagri_jaen_rendimiento.csv)
2. Satélite real MODIS MOD13Q1 v6.1 (2000-2024): Microsoft Planetary Computer (data/raw/cafe_real/modis_jaen_16d.csv)
3. Clima diario real ERA5 Open-Meteo Archive (2000-2024): (data/raw/cafe_real/clima_jaen_diario.csv)

Ventanas fenológicas botánicas (Jaén, Cajamarca):
- Floración: Agosto a Octubre (año previo Y-1)
- Llenado de grano: Noviembre (Y-1) a Febrero (año Y)
- Cosecha: Marzo a Julio (año Y)
"""

import os
import pandas as pd
import numpy as np

def build_cafe_dataset():
    print("Iniciando compilación determinista del Caso B (Café Jaén)...")
    
    # 1. Cargar Rendimiento Oficial
    rend_path = "data/raw/cafe_real/midagri_jaen_rendimiento.csv"
    df_rend = pd.read_csv(rend_path)
    print(f"Cargado rendimiento oficial: {len(df_rend)} campañas ({df_rend['anio'].min()} - {df_rend['anio'].max()})")
    
    # 2. Cargar Clima Diario ERA5
    clima_path = "data/raw/cafe_real/clima_jaen_diario.csv"
    df_clima = pd.read_csv(clima_path, parse_dates=["fecha"]).set_index("fecha")
    print(f"Cargado clima ERA5: {len(df_clima)} días ({df_clima.index.min().date()} - {df_clima.index.max().date()})")
    
    # 3. Cargar Índices Satelitales MODIS
    modis_path = "data/raw/cafe_real/modis_jaen_16d.csv"
    df_modis = pd.read_csv(modis_path, parse_dates=["fecha"]).set_index("fecha")
    print(f"Cargado satélite MODIS: {len(df_modis)} observaciones 16-días ({df_modis.index.min().date()} - {df_modis.index.max().date()})")
    
    # Años disponibles para análisis de campañas completas (2001 a 2024)
    # Una campaña Y necesita floración en Ago-Oct(Y-1), por tanto inicia en 2001
    campaigns = []
    
    for anio in range(2001, 2025):
        # Fechas fenológicas
        d_flor_start = f"{anio - 1}-08-01"
        d_flor_end = f"{anio - 1}-10-31"
        
        d_llen_start = f"{anio - 1}-11-01"
        d_llen_end = f"{anio}-02-28" if (anio % 4 != 0 or (anio % 100 == 0 and anio % 400 != 0)) else f"{anio}-02-29"
        
        d_cos_start = f"{anio}-03-01"
        d_cos_end = f"{anio}-07-31"
        
        d_anual_start = f"{anio}-01-01"
        d_anual_end = f"{anio}-12-31"
        
        # Agregación Clima: Floración
        clima_flor = df_clima.loc[d_flor_start:d_flor_end]
        lluvia_flor = float(clima_flor["lluvia_mm"].sum())
        tmax_flor = float(clima_flor["tmax"].mean())
        tmin_flor = float(clima_flor["tmin"].mean())
        et0_flor = float(clima_flor["et0_mm"].sum())
        def_hidrico_flor = float(lluvia_flor - et0_flor)  # balance hídrico
        dias_tmax_30_flor = int((clima_flor["tmax"] >= 30.0).sum())
        
        # Agregación Clima: Llenado
        clima_llen = df_clima.loc[d_llen_start:d_llen_end]
        lluvia_llen = float(clima_llen["lluvia_mm"].sum())
        tmax_llen = float(clima_llen["tmax"].mean())
        
        # Agregación Satelital MODIS: Floración
        modis_flor = df_modis.loc[d_flor_start:d_flor_end]
        ndvi_flor = float(modis_flor["ndvi_med"].median()) if len(modis_flor.dropna(subset=["ndvi_med"])) > 0 else np.nan
        evi_flor = float(modis_flor["evi_med"].median()) if len(modis_flor.dropna(subset=["evi_med"])) > 0 else np.nan
        
        # Agregación Satelital MODIS: Llenado
        modis_llen = df_modis.loc[d_llen_start:d_llen_end]
        ndvi_llen = float(modis_llen["ndvi_med"].median()) if len(modis_llen.dropna(subset=["ndvi_med"])) > 0 else np.nan
        evi_llen = float(modis_llen["evi_med"].median()) if len(modis_llen.dropna(subset=["evi_med"])) > 0 else np.nan
        
        # Agregación Satelital MODIS: Anual
        modis_anual = df_modis.loc[d_anual_start:d_anual_end]
        ndvi_anual = float(modis_anual["ndvi_med"].median())
        evi_anual = float(modis_anual["evi_med"].median())
        n_obs_sat = int(modis_anual["n_validos"].gt(0).sum())
        pct_val_sat = float(modis_anual["pct_valido"].mean())
        
        # Datos oficiales de rendimiento si existen para este año
        rend_match = df_rend[df_rend["anio"] == anio]
        if len(rend_match) > 0:
            row_r = rend_match.iloc[0]
            rend_kg = float(row_r["rendimiento_kg_ha"])
            rend_qq = float(row_r["rendimiento_qq_ha"])
            sup_ha = float(row_r["superficie_cosechada_ha"])
            prod_t = float(row_r["produccion_t"])
            fuente_doc = f"{row_r['fuente']} ({row_r['documento']}, p.{row_r['pagina']})"
        else:
            rend_kg = np.nan
            rend_qq = np.nan
            sup_ha = np.nan
            prod_t = np.nan
            fuente_doc = "No reportado en compendios INEI consultados"
            
        campaigns.append({
            "campania": anio,
            "rendimiento_kg_ha": rend_kg,
            "rendimiento_qq_ha": rend_qq,
            "superficie_cosechada_ha": sup_ha,
            "produccion_t": prod_t,
            "ndvi_anual": round(ndvi_anual, 4),
            "evi_anual": round(evi_anual, 4),
            "ndvi_flor": round(ndvi_flor, 4),
            "evi_flor": round(evi_flor, 4),
            "ndvi_llen": round(ndvi_llen, 4),
            "evi_llen": round(evi_llen, 4),
            "lluvia_flor_mm": round(lluvia_flor, 1),
            "tmax_flor_c": round(tmax_flor, 2),
            "def_hidrico_flor_mm": round(def_hidrico_flor, 1),
            "dias_calor_flor": dias_tmax_30_flor,
            "lluvia_llen_mm": round(lluvia_llen, 1),
            "tmax_llen_c": round(tmax_llen, 2),
            "n_obs_sat_validas": n_obs_sat,
            "pct_cobertura_sat": round(pct_val_sat, 1),
            "fuente_trazabilidad": fuente_doc
        })
        
    df_camp = pd.DataFrame(campaigns)
    
    # Calcular anomalía de rendimiento con ventana expansiva (sin leakage futuro)
    # anomalia_rend = y_t - mean(y_{<= t-1})
    anomalias = []
    rend_history = []
    for idx, row in df_camp.iterrows():
        y_val = row["rendimiento_kg_ha"]
        if np.isnan(y_val):
            anomalias.append(np.nan)
        else:
            if len(rend_history) >= 2:
                # tendencia o media previa
                anom = y_val - np.mean(rend_history)
            else:
                anom = 0.0
            anomalias.append(round(anom, 2))
            rend_history.append(y_val)
            
    df_camp["anomalia_rend_kg_ha"] = anomalias
    
    out_csv = "data/caso_2/cafe_jaen_campanias.csv"
    df_camp.to_csv(out_csv, index=False)
    print(f"\nCompilado exitoso! Guardado en {out_csv} (Total campañas: {len(df_camp)})")
    
    # Mostrar resumen con datos oficiales
    con_datos = df_camp.dropna(subset=["rendimiento_kg_ha"])
    print(f"\nCampañas con rendimiento oficial reportado ({len(con_datos)} campañas):")
    print(con_datos[["campania", "rendimiento_qq_ha", "ndvi_anual", "evi_anual", "lluvia_flor_mm", "tmax_flor_c", "anomalia_rend_kg_ha"]].to_string(index=False))
    
    return df_camp

if __name__ == "__main__":
    build_cafe_dataset()
