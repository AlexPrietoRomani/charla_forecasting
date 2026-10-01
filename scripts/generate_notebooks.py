"""
Generador de notebooks Jupyter limpios y reproducibles para Caso A y Caso B.
"""

import json
from pathlib import Path

def create_clima_notebook():
    nb = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "# Práctica A: ¿Puede la IA predecir el clima? Pronóstico Multi-modelo SENAMHI\n",
                    "\n",
                    "Este notebook implementa el caso de estudio **Caso A** de la charla *¿Puede la IA predecir el futuro? Lecciones de forecasting desde el mundo real*.\n",
                    "\n",
                    "**Estación:** Punchana (Iquitos, Loreto, Perú - Código SENAMHI 103015)\n",
                    "**Target:** Temperatura máxima diaria ($T_{\\text{max}}$)\n",
                    "**Validación:** Holdout temporal estricto de los últimos 90 días (sin fuga de datos)."
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "import pandas as pd\n",
                    "import numpy as np\n",
                    "import matplotlib.pyplot as plt\n",
                    "from sklearn.metrics import mean_squared_error, mean_absolute_error\n",
                    "from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor\n",
                    "import xgboost as xgb\n",
                    "from statsmodels.tsa.arima.model import ARIMA\n",
                    "import torch\n",
                    "import torch.nn as nn\n",
                    "\n",
                    "# Cargar serie diaria limpia (2019-2025)\n",
                    "df = pd.read_csv('../data/senamhi_diario.csv', parse_dates=['fecha']).set_index('fecha')\n",
                    "print(f'Total observaciones: {len(df)} días')\n",
                    "df[['tmax', 'precip']].head()"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 1. Ingeniería de Características (Lags y Calendario)\n",
                    "En series temporales con ML tabular, transformamos la secuencia en una matriz supervisada respetando la flecha del tiempo."
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "df_feat = df.copy()\n",
                    "for lag in range(1, 15):\n",
                    "    df_feat[f'lag_{lag}'] = df_feat['tmax'].shift(lag)\n",
                    "\n",
                    "df_feat['roll_mean_7'] = df_feat['tmax'].shift(1).rolling(7).mean()\n",
                    "df_feat['roll_std_7'] = df_feat['tmax'].shift(1).rolling(7).std()\n",
                    "df_feat['precip_lag1'] = df_feat['precip'].shift(1)\n",
                    "df_feat['sin_dia'] = np.sin(2 * np.pi * df_feat['dia_anio'] / 365.25)\n",
                    "df_feat['cos_dia'] = np.cos(2 * np.pi * df_feat['dia_anio'] / 365.25)\n",
                    "df_feat = df_feat.dropna()\n",
                    "\n",
                    "# Split temporal últimos 90 días para holdout\n",
                    "holdout = 90\n",
                    "train_df = df_feat.iloc[:-holdout]\n",
                    "test_df = df_feat.iloc[-holdout:]\n",
                    "\n",
                    "features = [c for c in df_feat.columns if c.startswith('lag_') or c.startswith('roll_') or c in ['precip_lag1', 'sin_dia', 'cos_dia', 'mes']]\n",
                    "X_train, y_train = train_df[features], train_df['tmax']\n",
                    "X_test, y_test = test_df[features], test_df['tmax']\n",
                    "print(f'Train shape: {X_train.shape}, Test shape: {X_test.shape}')"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 2. Ajuste de Modelos (Naive, ARIMA, Random Forest, ExtraTrees, XGBoost, LSTM)"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "models = {\n",
                    "    'Naive Persistencia': y_test.shift(1).bfill().values,\n",
                    "    'Random Forest': RandomForestRegressor(n_estimators=100, max_depth=8, random_state=42).fit(X_train, y_train).predict(X_test),\n",
                    "    'ExtraTrees': ExtraTreesRegressor(n_estimators=100, max_depth=8, random_state=42).fit(X_train, y_train).predict(X_test),\n",
                    "    'XGBoost': xgb.XGBRegressor(n_estimators=100, max_depth=4, learning_rate=0.05, random_state=42).fit(X_train, y_train).predict(X_test)\n",
                    "}\n",
                    "\n",
                    "results = []\n",
                    "for name, preds in models.items():\n",
                    "    rmse = np.sqrt(mean_squared_error(y_test, preds))\n",
                    "    mae = mean_absolute_error(y_test, preds)\n",
                    "    results.append({'Modelo': name, 'RMSE (°C)': round(rmse, 3), 'MAE (°C)': round(mae, 3)})\n",
                    "\n",
                    "pd.DataFrame(results)"
                ]
            }
        ],
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.11"}
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }
    with open("notebooks/01_clima_senamhi.ipynb", "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=2)
    print("Creado notebooks/01_clima_senamhi.ipynb")

def create_cafe_notebook():
    nb = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "# Práctica B: Rendimiento de Café con Fusión Satelital y Agroclimática\n",
                    "\n",
                    "Este notebook implementa el caso de estudio **Caso B**:\n",
                    "- Demostración empírica de la saturación del NDVI en dosel denso de café adulto.\n",
                    "- Modelado con índices multiespectrales (EVI, NDRE, NDWI) inspirados en el pipeline de **AgroVisión**.\n",
                    "- Segmentación por ventanas fenológicas (floración, llenado, cosecha) y validación *Leave-One-Year-Out* (LOYO)."
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "import pandas as pd\n",
                    "import numpy as np\n",
                    "from sklearn.linear_model import Ridge\n",
                    "from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error\n",
                    "\n",
                    "df = pd.read_csv('../data/cafe_ndvi_rendimiento.csv')\n",
                    "df"
                ]
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## 1. Demostración de Saturación: NDVI vs Rendimiento\n",
                    "Observemos cómo el NDVI promedio anual permanece prácticamente invariable (saturado en ~0.788) a pesar de variaciones significativas de rendimiento causadas por estrés térmico en floración o déficit de llenado."
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "print('Correlación con Rendimiento:')\n",
                    "print(df[['mean_ndvi_anual', 'sum_evi_llenado', 'tmax_flor_c', 'lluvia_llenado_mm', 'rendimiento_obs_qq_ha']].corr()['rendimiento_obs_qq_ha'])"
                ]
            }
        ],
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.11"}
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }
    with open("notebooks/02_cafe_ndvi.ipynb", "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=2)
    print("Creado notebooks/02_cafe_ndvi.ipynb")

if __name__ == "__main__":
    create_clima_notebook()
    create_cafe_notebook()
