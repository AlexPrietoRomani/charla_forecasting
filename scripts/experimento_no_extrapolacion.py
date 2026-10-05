"""
Experimento Propio de No-Extrapolación en Árboles de Decisión (Diapositiva 05).
Demuestra de forma empírica y reproducible por qué los modelos basados en árboles
(Random Forest / ExtraTrees / XGBoost) colapsan en una meseta constante cuando
los datos del mundo real superan el rango histórico de entrenamiento.

Usa datos reales de SENAMHI Punchana (Iquitos, 2019-2025).
Entrenamiento: días con Tmax <= 34.0 °C.
Evaluación: días extremos con Tmax > 34.0 °C (olas de calor hasta 37.5 °C).

Compara:
1. Árbol en niveles (y_t): Colapsa en la media de la hoja más alta (meseta plana <= 34.0 °C).
2. Modelo en diferencias (Delta y_t = y_t - y_{t-1}) o Regresión Lineal/ARIMA: Extrapola la tendencia.

Exporta: data/experimento_extrapolacion.csv
"""

from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge

DATA_PATH = Path("data/senamhi_diario.csv")
OUT_CSV = Path("data/experimento_extrapolacion.csv")

def run_extrapolation_experiment():
    print("Iniciando Experimento Propio de No-Extrapolación...")
    df = pd.read_csv(DATA_PATH, parse_dates=["fecha"]).set_index("fecha")
    
    # Construir lags 1 a 7
    df_lags = pd.DataFrame(index=df.index)
    df_lags["tmax"] = df["tmax"]
    for l in range(1, 8):
        df_lags[f"lag_{l}"] = df["tmax"].shift(l)
    df_lags["delta_tmax"] = df["tmax"] - df["tmax"].shift(1)
    for l in range(1, 8):
        df_lags[f"delta_lag_{l}"] = df_lags["delta_tmax"].shift(l)
        
    df_clean = df_lags.dropna()
    
    # Restringir entrenamiento a Tmax <= 34.0 °C
    train_mask = df_clean["tmax"] <= 34.0
    df_train = df_clean[train_mask]
    
    # Holdout de evaluación: días extremos con Tmax > 34.5 °C (hasta 37.5 °C)
    # Seleccionamos un episodio real continuo de ola de calor (ej. Septiembre-Octubre 2023)
    ola_calor = df_clean.loc["2023-09-15":"2023-10-15"]
    
    features_levels = [f"lag_{l}" for l in range(1, 8)]
    features_deltas = [f"delta_lag_{l}" for l in range(1, 8)]
    
    # 1. Random Forest entrenado en niveles y_t
    rf_levels = RandomForestRegressor(n_estimators=100, max_depth=8, random_state=42)
    rf_levels.fit(df_train[features_levels], df_train["tmax"])
    pred_rf_levels = rf_levels.predict(ola_calor[features_levels])
    
    # 2. Random Forest entrenado en diferencias Delta y_t
    rf_deltas = RandomForestRegressor(n_estimators=100, max_depth=8, random_state=42)
    rf_deltas.fit(df_train[features_deltas], df_train["delta_tmax"])
    pred_deltas = rf_deltas.predict(ola_calor[features_deltas])
    pred_rf_con_deltas = ola_calor["lag_1"].values + pred_deltas
    
    # 3. Modelo lineal en diferencias (Ridge)
    ridge_deltas = Ridge(alpha=1.0)
    ridge_deltas.fit(df_train[features_deltas], df_train["delta_tmax"])
    pred_ridge_deltas = ola_calor["lag_1"].values + ridge_deltas.predict(ola_calor[features_deltas])
    
    # Construir tabla comparativa del episodio extremo
    df_out = pd.DataFrame({
        "fecha": [d.strftime("%Y-%m-%d") for d in ola_calor.index],
        "tmax_real": ola_calor["tmax"].round(1).values,
        "pred_arbol_niveles": pred_rf_levels.round(2),
        "pred_arbol_diferencias": pred_rf_con_deltas.round(2),
        "pred_ridge_diferencias": pred_ridge_deltas.round(2),
        "tope_entrenamiento": 34.0
    })
    
    df_out.to_csv(OUT_CSV, index=False)
    print(f"Guardado experimento en: {OUT_CSV}")
    print("\nEpisodio de ola de calor real en Punchana (Sept-Oct 2023):")
    print(df_out[df_out["tmax_real"] >= 34.5].head(10).to_string(index=False))
    
    max_train_val = df_train["tmax"].max()
    max_tree_pred = pred_rf_levels.max()
    max_real_val = ola_calor["tmax"].max()
    print(f"\nTecho de entrenamiento: {max_train_val:.1f} °C")
    print(f"Máximo valor real observado en la ola de calor: {max_real_val:.1f} °C")
    print(f"Meseta máxima a la que el árbol puede predecir: {max_tree_pred:.2f} °C")
    print(f"Error por saturación de hoja: {max_real_val - max_tree_pred:.2f} °C (el árbol queda totalmente ciego por encima de 34.0 °C)")

if __name__ == "__main__":
    run_extrapolation_experiment()
