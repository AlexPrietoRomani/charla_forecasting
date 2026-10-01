"""
Script de limpieza y estructuración de la serie diaria de SENAMHI.
Estación: Punchana (Iquitos, Loreto) - Código 103015.
Periodo: 2019-01-01 a 2025-12-31 (7 años).
"""

from pathlib import Path
import numpy as np
import pandas as pd

RAW_PATH = Path("data/raw/senamhi_punchana_raw.csv")
OUT_PATH = Path("data/senamhi_diario.csv")

def clean_senamhi_data():
    df = pd.read_csv(RAW_PATH, sep=";")
    df.columns = ["anio", "mes", "dia", "tmax", "tmin", "humedad", "precip"]

    # Construir fecha estándar
    df["fecha"] = pd.to_datetime(
        df["anio"].astype(str) + "-" +
        df["mes"].astype(str).str.zfill(2) + "-" +
        df["dia"].astype(str).str.zfill(2),
        errors="coerce"
    )
    df = df.dropna(subset=["fecha"]).sort_values("fecha").drop_duplicates("fecha")

    # Reemplazo de S/D y T (Traza)
    for col in ["tmax", "tmin", "humedad", "precip"]:
        df[col] = df[col].astype(str).str.strip().replace({
            "S/D": np.nan, "s/d": np.nan,
            "T": 0.0, "t": 0.0
        })
        df[col] = pd.to_numeric(df[col], errors="coerce")

    # Reindexar al calendario diario completo (sin días faltantes)
    full_idx = pd.date_range("2019-01-01", "2025-12-31", freq="D")
    df = df.set_index("fecha").reindex(full_idx)
    df.index.name = "fecha"

    # Llenado controlado para forecasting:
    # tmax: interpolación lineal hasta máx 3 días seguidos
    df["tmax_raw"] = df["tmax"]
    df["tmax"] = df["tmax"].interpolate(method="time", limit=3).bfill().ffill()
    
    # precip: huecos asumidos como 0.0 o mediana estacional
    df["precip_raw"] = df["precip"]
    df["precip"] = df["precip"].fillna(0.0)

    # Variables de calendario / temporales útiles para modelos
    df["mes"] = df.index.month
    df["dia_anio"] = df.index.dayofyear
    df["dia_semana"] = df.index.dayofweek

    # Guardar dataframe limpio
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df[["tmax", "tmin", "precip", "humedad", "mes", "dia_anio", "dia_semana"]].round(2).to_csv(OUT_PATH)
    print(f"Dataset limpio guardado en: {OUT_PATH} ({len(df)} filas, {OUT_PATH.stat().st_size / 1024:.1f} KB)")

if __name__ == "__main__":
    clean_senamhi_data()
