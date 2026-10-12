# Caso 1: Datos de Clima SENAMHI (Punchana, Iquitos)

Este directorio contiene los conjuntos de datos correspondientes al **Caso 1: Pronóstico Climático en la Selva Peruana**.

## Ubicación y Estación
* **Estación:** Punchana, Loreto, Perú (Código SENAMHI: `103015`, Web: `150208`).
* **Coordenadas:** `-3.6903°` Lat, `-73.2556°` Lon, `91 msnm`.
* **Periodo:** `2019-01-01` a `2025-12-31` (2,557 días continuos).

## Archivos del Caso 1
1. **`senamhi_diario.csv`**:
   * Serie temporal histórica procesada sin huecos tras interpolación lineal física y control de ceros en precipitación.
   * Columnas: `fecha`, `anio`, `mes`, `dia`, `tmax`, `tmin`, `humedad`, `precip`.
2. **`benchmark_punchana.csv`**:
   * Tabla comparativa de los 8 modelos evaluados en holdout temporal estricto de 90 días (Oct-Dic 2025).
   * Columnas: `modelo`, `rmse_1d`, `mae_1d`, `rmse_7d`, `tiempo_s`, `hardware`, `p_valor_vs_mejor`, `interpretacion_dm`.
3. **`senamhi_forecast_7d.csv`**:
   * Pronóstico multimodelo para el horizonte $t+1$ a $t+7$ con cuantiles de incertidumbre (P10 y P90) y temperaturas reales observadas.
   * Columnas: `fecha`, `tmax_observada`, `pred_extratrees`, `pred_chronos`, `pred_timesfm`, `pred_arima`, `ci_lower_p10`, `ci_upper_p90`, `chronos_p10`, `chronos_p90`.
4. **`noaa_ecmwf_forecast.csv`**:
   * Pronóstico físico global numérico comparando la discrepancia entre NOAA GFS (EE.UU.) y ECMWF IFS (Europa) en Iquitos.
   * Columnas: `fecha`, `tmax_ecmwf`, `tmax_gfs`, `delta_temp`, `precip_ecmwf`, `precip_gfs`.
5. **`experimento_extrapolacion.csv`**:
   * Experimento propio de fallo de extrapolación fuera del rango histórico (Random Forest vs Ridge/Splines).
   * Columnas: `tmax_real`, `rf_directo`, `ridge_directo`, `rf_diferenciado`.
