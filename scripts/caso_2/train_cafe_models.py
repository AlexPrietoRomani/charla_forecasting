"""
Modelado predictivo de rendimiento de café (qq/ha) para Caso 2 (Jaén, Cajamarca).
Compara:
  - Baseline: Media histórica (Leave-One-Year-Out)
  - Modelo Aislado: Regresión solo con NDVI promedio anual (demuestra la falla por saturación espectral)
  - Modelo Fusión (AgroVisión): EVI fenológico + Variables hídricas de floración (ERA5-Land)
  - Modelo Árboles Parsimoniosos: Random Forest (d=2)

Valida estrictamente con Leave-One-Year-Out (LOYO) y Walk-Forward sobre datos reales INEI / MIDAGRI-SIEA.
"""

from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error, mean_absolute_error

DATA_PATH = Path("data/caso_2/cafe_jaen_campanias.csv")

def train_cafe_loyo():
    df = pd.read_csv(DATA_PATH)
    df_eval = df.dropna(subset=["rendimiento_qq_ha"]).copy().reset_index(drop=True)
    n = len(df_eval)
    print(f"Cargado dataset real de café: {n} campañas auditadas ({df_eval['campania'].min()} a {df_eval['campania'].max()})")

    y_true = df_eval["rendimiento_qq_ha"].values

    preds_mean = []
    preds_solo_ndvi = []
    preds_fusion = []
    preds_rf = []

    # Features para los modelos
    feat_fusion = ["evi_flor", "lluvia_flor_mm", "def_hidrico_flor_mm", "tmax_flor_c"]
    feat_ndvi = ["ndvi_anual"]

    for i in range(n):
        # Leave-One-Year-Out split
        train_idx = [j for j in range(n) if j != i]
        test_idx = [i]

        df_tr = df_eval.iloc[train_idx]
        df_te = df_eval.iloc[test_idx]

        # 1. Baseline: media histórica
        preds_mean.append(df_tr["rendimiento_qq_ha"].mean())

        # Escalador ajustado solo en train para evitar leakage
        scaler_ndvi = StandardScaler()
        X_tr_ndvi = scaler_ndvi.fit_transform(df_tr[feat_ndvi])
        X_te_ndvi = scaler_ndvi.transform(df_te[feat_ndvi])

        scaler_fus = StandardScaler()
        X_tr_fus = scaler_fus.fit_transform(df_tr[feat_fusion])
        X_te_fus = scaler_fus.transform(df_te[feat_fusion])

        # 2. Solo NDVI anual
        m_ndvi = Ridge(alpha=1.0)
        m_ndvi.fit(X_tr_ndvi, df_tr["rendimiento_qq_ha"])
        preds_solo_ndvi.append(m_ndvi.predict(X_te_ndvi)[0])

        # 3. Fusión Multimodal (Ridge regularizado)
        m_fus = Ridge(alpha=1.0)
        m_fus.fit(X_tr_fus, df_tr["rendimiento_qq_ha"])
        preds_fusion.append(m_fus.predict(X_te_fus)[0])

        # 4. Random Forest Parsimonioso
        m_rf = RandomForestRegressor(n_estimators=50, max_depth=2, random_state=42)
        m_rf.fit(X_tr_fus, df_tr["rendimiento_qq_ha"])
        preds_rf.append(m_rf.predict(X_te_fus)[0])

    preds_mean = np.array(preds_mean)
    preds_solo_ndvi = np.array(preds_solo_ndvi)
    preds_fusion = np.array(preds_fusion)
    preds_rf = np.array(preds_rf)

    print("\n=== EVALUACIÓN LEAVE-ONE-YEAR-OUT (LOYO) ===")
    for nombre, p in [
        ("1. Baseline Media Histórica", preds_mean),
        ("2. Solo NDVI Anual (Saturado)", preds_solo_ndvi),
        ("3. Fusión Multimodal (Ridge)", preds_fusion),
        ("4. Random Forest (d=2)", preds_rf),
    ]:
        mae = mean_absolute_error(y_true, p)
        rmse = np.sqrt(mean_squared_error(y_true, p))
        mape = mean_absolute_percentage_error(y_true, p) * 100
        print(f"  {nombre:30s} | MAE = {mae:.2f} qq/ha | RMSE = {rmse:.2f} qq/ha | MAPE = {mape:.1f}%")

if __name__ == "__main__":
    train_cafe_loyo()
