"""
Entrenamiento y evaluación comparativa multi-modelo para pronóstico de clima SENAMHI (Iquitos).
Compara:
  1. Naive persistencia / estacional
  2. ARIMA/ETS (statsmodels)
  3. Random Forest (scikit-learn)
  4. XGBoost & LightGBM
  5. LSTM (PyTorch)

Valida con holdout temporal de 90 días (sin leakage) y genera data/senamhi_forecast_7d.csv.
"""

from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
import xgboost as xgb
import lightgbm as lgb
from statsmodels.tsa.arima.model import ARIMA
import torch
import torch.nn as nn

DATA_PATH = Path("data/senamhi_diario.csv")
OUT_FORECAST_PATH = Path("data/senamhi_forecast_7d.csv")

def create_features(df, target_col="tmax", max_lags=14):
    df_feat = df.copy()
    # Lags de temperatura
    for lag in range(1, max_lags + 1):
        df_feat[f"lag_{lag}"] = df_feat[target_col].shift(lag)
    
    # Medias y desvíos móviles
    df_feat["roll_mean_7"] = df_feat[target_col].shift(1).rolling(7).mean()
    df_feat["roll_std_7"] = df_feat[target_col].shift(1).rolling(7).std()
    df_feat["roll_mean_14"] = df_feat[target_col].shift(1).rolling(14).mean()
    
    # Exógenas climáticas (precipitación lag 1)
    df_feat["precip_lag1"] = df_feat["precip"].shift(1)
    
    # Temporales cíclicas
    df_feat["sin_dia"] = np.sin(2 * np.pi * df_feat["dia_anio"] / 365.25)
    df_feat["cos_dia"] = np.cos(2 * np.pi * df_feat["dia_anio"] / 365.25)
    
    return df_feat.dropna()

def train_eval():
    df = pd.read_csv(DATA_PATH, parse_dates=["fecha"]).set_index("fecha")
    print(f"Cargado dataset SENAMHI: {len(df)} días ({df.index.min().date()} a {df.index.max().date()})")

    # Split temporal estricto: últimos 90 días para holdout
    holdout_days = 90
    train_df = df.iloc[:-holdout_days]
    test_df = df.iloc[-holdout_days:]
    print(f"Train: {len(train_df)} días | Test (Holdout): {len(test_df)} días")

    y_test = test_df["tmax"].values

    # 1. Baseline Naive (persistencia del valor previo)
    y_pred_naive = test_df["tmax"].shift(1).bfill().values
    rmse_naive = np.sqrt(mean_squared_error(y_test, y_pred_naive))
    mae_naive = mean_absolute_error(y_test, y_pred_naive)
    print(f"[Baseline Naive]       RMSE: {rmse_naive:.3f} °C | MAE: {mae_naive:.3f} °C")

    # 2. ARIMA (statsmodels)
    history = list(train_df["tmax"].values)
    arima_preds = []
    # Modelo ARIMA(2,0,1) sobre serie
    arima_model = ARIMA(train_df["tmax"], order=(2, 0, 1)).fit()
    y_pred_arima = arima_model.forecast(steps=holdout_days).values
    rmse_arima = np.sqrt(mean_squared_error(y_test, y_pred_arima))
    mae_arima = mean_absolute_error(y_test, y_pred_arima)
    print(f"[Clásico ARIMA]       RMSE: {rmse_arima:.3f} °C | MAE: {mae_arima:.3f} °C")

    # Features para ML
    df_features = create_features(df, target_col="tmax", max_lags=14)
    feature_cols = [c for c in df_features.columns if c.startswith("lag_") or c.startswith("roll_") or c in ["precip_lag1", "sin_dia", "cos_dia", "mes"]]

    X_train = df_features.loc[df_features.index.isin(train_df.index), feature_cols]
    y_train = df_features.loc[df_features.index.isin(train_df.index), "tmax"]

    X_test = df_features.loc[df_features.index.isin(test_df.index), feature_cols]
    y_test_ml = df_features.loc[df_features.index.isin(test_df.index), "tmax"]

    # 3. Random Forest
    rf = RandomForestRegressor(n_estimators=100, max_depth=8, random_state=42, n_jobs=-1)
    rf.fit(X_train, y_train)
    y_pred_rf = rf.predict(X_test)
    rmse_rf = np.sqrt(mean_squared_error(y_test_ml, y_pred_rf))
    mae_rf = mean_absolute_error(y_test_ml, y_pred_rf)
    print(f"[ML Random Forest]    RMSE: {rmse_rf:.3f} °C | MAE: {mae_rf:.3f} °C")

    # 4. XGBoost
    model_xgb = xgb.XGBRegressor(n_estimators=100, max_depth=4, learning_rate=0.05, random_state=42)
    model_xgb.fit(X_train, y_train)
    y_pred_xgb = model_xgb.predict(X_test)
    rmse_xgb = np.sqrt(mean_squared_error(y_test_ml, y_pred_xgb))
    mae_xgb = mean_absolute_error(y_test_ml, y_pred_xgb)
    print(f"[ML XGBoost]          RMSE: {rmse_xgb:.3f} °C | MAE: {mae_xgb:.3f} °C")

    # 5. ExtraTrees (Geurts et al., 2006)
    from sklearn.ensemble import ExtraTreesRegressor
    et = ExtraTreesRegressor(n_estimators=100, max_depth=8, random_state=42, n_jobs=-1)
    et.fit(X_train, y_train)
    y_pred_et = et.predict(X_test)
    rmse_et = np.sqrt(mean_squared_error(y_test_ml, y_pred_et))
    mae_et = mean_absolute_error(y_test_ml, y_pred_et)
    print(f"[ML ExtraTrees]       RMSE: {rmse_et:.3f} °C | MAE: {mae_et:.3f} °C")

    # 6. Deep Learning: PyTorch LSTM
    # Normalización simple
    t_mean, t_std = y_train.mean(), y_train.std()
    
    def make_sequences(series, seq_len=14):
        X, y = [], []
        vals = (series.values - t_mean) / t_std
        for i in range(len(vals) - seq_len):
            X.append(vals[i:i+seq_len])
            y.append(vals[i+seq_len])
        return np.array(X, dtype=np.float32), np.array(y, dtype=np.float32)

    X_seq_tr, y_seq_tr = make_sequences(train_df["tmax"])
    X_seq_te, y_seq_te = make_sequences(df["tmax"].iloc[-(holdout_days + 14):])

    class SimpleLSTM(nn.Module):
        def __init__(self):
            super().__init__()
            self.lstm = nn.LSTM(input_size=1, hidden_size=32, batch_first=True)
            self.fc = nn.Linear(32, 1)
        def forward(self, x):
            out, _ = self.lstm(x)
            return self.fc(out[:, -1, :])

    torch.manual_seed(42)
    lstm = SimpleLSTM()
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(lstm.parameters(), lr=0.01)

    X_t_tr = torch.tensor(X_seq_tr).unsqueeze(-1)
    y_t_tr = torch.tensor(y_seq_tr).unsqueeze(-1)

    lstm.train()
    for epoch in range(40):
        optimizer.zero_grad()
        loss = criterion(lstm(X_t_tr), y_t_tr)
        loss.backward()
        optimizer.step()

    lstm.eval()
    with torch.no_grad():
        X_t_te = torch.tensor(X_seq_te).unsqueeze(-1)
        y_pred_lstm_norm = lstm(X_t_te).squeeze(-1).numpy()
        y_pred_lstm = (y_pred_lstm_norm * t_std) + t_mean

    rmse_lstm = np.sqrt(mean_squared_error(y_test, y_pred_lstm))
    mae_lstm = mean_absolute_error(y_test, y_pred_lstm)
    print(f"[DL LSTM 1 capa]      RMSE: {rmse_lstm:.3f} °C | MAE: {mae_lstm:.3f} °C")

    # Exportar predicción multi-horizonte (últimos 7 días) para el gráfico interactivo del deck
    last_7_days = test_df.iloc[-7:]
    fechas_7d = [d.strftime("%Y-%m-%d") for d in last_7_days.index]
    obs_7d = last_7_days["tmax"].values
    
    # Pronósticos de los modelos para los últimos 7 días
    pred_rf_7d = y_pred_rf[-7:]
    pred_xgb_7d = y_pred_xgb[-7:]
    pred_lstm_7d = y_pred_lstm[-7:]
    pred_naive_7d = y_pred_naive[-7:]

    # Bandas de confianza 90% para Random Forest (+/- 1.645 * std_residuos)
    residuos_rf = y_test_ml - y_pred_rf
    std_err = np.std(residuos_rf)
    ci_lower = (pred_rf_7d - 1.645 * std_err).round(2)
    ci_upper = (pred_rf_7d + 1.645 * std_err).round(2)

    df_forecast_7d = pd.DataFrame({
        "fecha": fechas_7d,
        "tmax_observada": obs_7d.round(2),
        "pred_naive": pred_naive_7d.round(2),
        "pred_random_forest": pred_rf_7d.round(2),
        "pred_xgboost": pred_xgb_7d.round(2),
        "pred_lstm": pred_lstm_7d.round(2),
        "ci_lower_90": ci_lower,
        "ci_upper_90": ci_upper
    })

    df_forecast_7d.to_csv(OUT_FORECAST_PATH, index=False)
    print(f"\nPredicciones 7 días guardadas en: {OUT_FORECAST_PATH}")
    print(df_forecast_7d)

    # Tabla resumen de métricas para la presentación
    resumen = pd.DataFrame({
        "Modelo": ["Naive Persistencia", "ARIMA (2,0,1)", "Random Forest", "ExtraTrees", "XGBoost", "LSTM (1 capa)"],
        "RMSE (°C)": [rmse_naive, rmse_arima, rmse_rf, rmse_et, rmse_xgb, rmse_lstm],
        "MAE (°C)": [mae_naive, mae_arima, mae_rf, mae_et, mae_xgb, mae_lstm],
        "Mejora vs Naive": [
            "0.0%",
            f"{((rmse_naive - rmse_arima)/rmse_naive)*100:+.1f}%",
            f"{((rmse_naive - rmse_rf)/rmse_naive)*100:+.1f}%",
            f"{((rmse_naive - rmse_et)/rmse_naive)*100:+.1f}%",
            f"{((rmse_naive - rmse_xgb)/rmse_naive)*100:+.1f}%",
            f"{((rmse_naive - rmse_lstm)/rmse_naive)*100:+.1f}%",
        ]
    })
    print("\n=== RESUMEN DE MODELOS (HOLDOUT 90 DÍAS) ===")
    print(resumen.to_string(index=False))

    return resumen

if __name__ == "__main__":
    train_eval()
