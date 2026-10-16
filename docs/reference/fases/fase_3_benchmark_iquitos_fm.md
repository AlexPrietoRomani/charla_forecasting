# Fase 3: Caso A — Benchmark de 8 Modelos en Iquitos con Foundation Models

> **Documento de Fase:** `docs/reference/fases/fase_3_benchmark_iquitos_fm.md`  
> **Plan Relacionado:** [plan_detallado_diapositivas.md](../plan_detallado_diapositivas.md) (Sección 3: Protocolo del Benchmark Ampliado)  
> **Estado:** `[ ] Pendiente de Ejecución` (Requiere aprobación explícita del usuario)

---

## 1. Objetivo de la Fase
Ejecutar un benchmark forense y riguroso de 8 modelos sobre los datos reales de la estación meteorológica Punchana (SENAMHI, 2,557 días entre 2019 y 2025):
- Evaluar en igualdad de condiciones sobre un *holdout* estricto de 90 días (octubre–diciembre 2025) sin filtración temporal.
- Incorporar por primera vez modelos fundacionales *zero-shot* contemporáneos (Chronos de Amazon y TimesFM de Google) compitiendo contra baselines estadísticos, árboles (ExtraTrees/RF) y Deep Learning local (LSTM).
- Calcular métricas formales: RMSE, MAE, cobertura empírica P10–P90, tiempo de entrenamiento/inferencia y significancia estadística (prueba de Diebold-Mariano).

---

## 2. Entregables
1. `scripts/caso_1/benchmark_punchana.py` (Script integral y reproducible con semillas fijas).
2. `data/caso_1/benchmark_punchana.csv` (Tabla canónica con columnas: `modelo`, `familia`, `rmse_1d`, `mae_1d`, `rmse_7d`, `mae_7d`, `tiempo_s`, `hardware`, `cobertura_p10_p90`, `p_valor_vs_mejor`).
3. `data/caso_1/senamhi_forecast_7d.csv` (Pronóstico diario a 7 días con bandas de incertidumbre P10/P90 de los modelos destacados y llamadas reales a NOAA/ECMWF).
4. `notebooks/01_clima_senamhi.ipynb` ejecutado con todos los outputs reales y gráficos comparativos.

---

## 3. Subfases y Tareas

### SF3.1 Pipeline de Preprocesamiento y División Temporal
- [X] **T3.1.1** Cargar `data/caso_1/senamhi_diario.csv` y verificar la ventana temporal (2019-01-01 a 2025-12-31, 2,557 días).
- [X] **T3.1.2** Definir split temporal estricto: Entrenamiento = 2,467 días iniciales; Holdout de evaluación ciego = últimos 90 días.
- [X] **T3.1.3** Construir matriz de rezagos (lags 1 a 14) y variables de calendario para los modelos tabulares sin fuga de información del futuro.

### SF3.2 Implementación y Ejecución de los 8 Modelos
- [X] **T3.2.1** Modelo 0: Naive estacional (persistencia de 7 días / estacionalidad semanal).
- [X] **T3.2.2** Modelo 1: ARIMA / SARIMAX calibrado mediante AIC sobre la serie diferenciada.
- [X] **T3.2.3** Modelo 2: Suavizado exponencial Holt-Winters con amortiguamiento.
- [X] **T3.2.4** Modelo 3: Random Forest con ventana deslizante.
- [X] **T3.2.5** Modelo 4: ExtraTrees / LightGBM con lags y rolling statistics.
- [X] **T3.2.6** Modelo 5: Red LSTM profunda (PyTorch), promediada en 5 semillas con reporte de $\mu \pm \sigma$.
- [X] **T3.2.7** Modelo 6: Chronos (Amazon) en modo Zero-Shot (sin entrenamiento local), evaluando cuantiles P10/P50/P90 nativos.
- [X] **T3.2.8** Modelo 7: TimesFM (Google) en modo Zero-Shot con parches de salida de 128.

### SF3.3 Auditoría Estadística y Exportación
- [X] **T3.3.1** Calcular métricas cuantitativas para horizontes $h=1$ y $h=7$ días.
- [X] **T3.3.2** Aplicar prueba de Diebold-Mariano entre el modelo de menor RMSE y los demás. Identificar empates estadísticos ($p > 0.05$).
- [X] **T3.3.3** Aplicar la regla de conclusión preestablecida: si hay empate estadístico, gana el más simple y parsimonioso (ExtraTrees en 0.25s).
- [X] **T3.3.4** Exportar `data/caso_1/benchmark_punchana.csv` y generar `data/caso_1/senamhi_forecast_7d.csv`.
- [X] **T3.3.5** Reejecutar `notebooks/01_clima_senamhi.ipynb` garantizando que guarde todas las celdas con resultados verificables.

---

## 4. Criterios de Aceptación (DoD Fase 3)
- [X] Todos los modelos se evalúan exactamente en el mismo periodo ciego de 90 días.
- [X] `data/caso_1/benchmark_punchana.csv` contiene las 8 filas completas sin celdas vacías.
- [X] Los tiempos de cómputo y consumo de hardware están medidos objetivamente.
- [X] El notebook 01 corre limpio de inicio a fin (`Kernel -> Restart & Run All`).
