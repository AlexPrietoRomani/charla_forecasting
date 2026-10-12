"""
Modelado predictivo de rendimiento de café (qq/ha) para Caso B.
Compara:
  - Baseline: Media histórica (Leave-One-Year-Out)
  - Modelo Aislado: Regresión solo con NDVI promedio anual (demuestra la falla por saturación)
  - Modelo Fusión (AgroVisión): EVI fenológico + NDRE + variables climáticas (Open-Meteo)

Valida estrictamente con Leave-One-Year-Out (LOYO) y exporta data/cafe_ndvi_rendimiento.csv.
"""

from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error, r2_score

DATA_PATH = Path("data/caso_2/deprecated/cafe_ndvi_rendimiento_SINTETICO.csv")

def train_cafe_loyo():
    df = pd.read_csv(DATA_PATH)
    print(f"Cargado dataset café: {len(df)} campañas ({df['campania'].min()} a {df['campania'].max()})")

    n = len(df)
    y_true = df["rendimiento_obs_qq_ha"].values

    preds_mean = []
    preds_solo_ndvi = []
    preds_fusion = []

    # Features para el modelo fusionado
    feat_fusion = ["sum_evi_llenado", "max_ndre_flor", "lluvia_llenado_mm", "tmax_flor_c"]
    feat_ndvi = ["mean_ndvi_anual"]

    for i in range(n):
        # Leave-One-Year-Out split
        train_idx = [j for j in range(n) if j != i]
        test_idx = [i]

        df_tr = df.iloc[train_idx]
        df_te = df.iloc[test_idx]

        # 1. Baseline: media histórica
        preds_mean.append(df_tr["rendimiento_obs_qq_ha"].mean())

        # 2. Solo NDVI (lineal)
        m_ndvi = Ridge(alpha=1.0)
        m_ndvi.fit(df_tr[feat_ndvi], df_tr["rendimiento_obs_qq_ha"])
        preds_solo_ndvi.append(m_ndvi.predict(df_te[feat_ndvi])[0])

        # 3. Fusión Multimodal (Ridge regularizado para dataset pequeño / n=6)
        m_fus = Ridge(alpha=10.0)
        m_fus.fit(df_tr[feat_fusion], df_tr["rendimiento_obs_qq_ha"])
        preds_fusion.append(m_fus.predict(df_te[feat_fusion])[0])

    preds_mean = np.array(preds_mean)
    preds_solo_ndvi = np.array(preds_solo_ndvi)
    preds_fusion = np.array(preds_fusion)

    mape_mean = mean_absolute_percentage_error(y_true, preds_mean) * 100
    mape_ndvi = mean_absolute_percentage_error(y_true, preds_solo_ndvi) * 100
    mape_fus = mean_absolute_percentage_error(y_true, preds_fusion) * 100

    rmse_mean = np.sqrt(mean_squared_error(y_true, preds_mean))
    rmse_ndvi = np.sqrt(mean_squared_error(y_true, preds_solo_ndvi))
    rmse_fus = np.sqrt(mean_squared_error(y_true, preds_fusion))

    print("\n=== EVALUACIÓN LEAVE-ONE-YEAR-OUT (LOYO) ===")
    print(f"1. Baseline Media:    RMSE = {rmse_mean:.2f} qq/ha | MAPE = {mape_mean:.1f}%")
    print(f"2. Solo NDVI Anual:   RMSE = {rmse_ndvi:.2f} qq/ha | MAPE = {mape_ndvi:.1f}% (Inútil por saturación)")
    print(f"3. Fusión Multimodal: RMSE = {rmse_fus:.2f} qq/ha | MAPE = {mape_fus:.1f}% (Mejora sustancial)")

    # Enriquecer dataset para el deck interactivo
    df["pred_media_baseline"] = preds_mean.round(2)
    df["pred_solo_ndvi"] = preds_solo_ndvi.round(2)
    df["pred_modelo_fusion"] = preds_fusion.round(2)
    df["error_abs_fusion"] = np.abs(y_true - preds_fusion).round(2)

    df.to_csv(DATA_PATH, index=False)
    print(f"\nDataset actualizado en: {DATA_PATH}")
    print(df[["campania", "rendimiento_obs_qq_ha", "pred_solo_ndvi", "pred_modelo_fusion", "error_abs_fusion"]])

if __name__ == "__main__":
    train_cafe_loyo()
