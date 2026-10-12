# Pipeline del Caso 1: Clima SENAMHI Punchana (Iquitos)

Este directorio contiene los scripts para el procesamiento, modelado predictivo, benchmark y visualización del **Caso 1: Clima en la Selva Tropical**.

## Flujo de Ejecución (ETL a Benchmark)

1. **Limpieza e imputación controlada:**
   ```bash
   python scripts/caso_1/clean_senamhi.py
   ```
   * Lee: `data/raw/senamhi_punchana_raw.csv`
   * Exporta: `data/caso_1/senamhi_diario.csv`

2. **Benchmark riguroso de 8 modelos:**
   ```bash
   python scripts/caso_1/benchmark_punchana.py
   ```
   * Evalúa: Naive, ARIMA, Holt-Winters, Random Forest, ExtraTrees, LSTM (5 semillas), Chronos Zero-Shot, TimesFM Zero-Shot.
   * Aplica test de Diebold-Mariano y regla de parsimonia.
   * Exporta: `data/caso_1/benchmark_punchana.csv` y `data/caso_1/senamhi_forecast_7d.csv`

3. **Experimento propio de no-extrapolación:**
   ```bash
   python scripts/caso_1/experimento_no_extrapolacion.py
   ```
   * Demuestra el límite de los árboles fuera del rango histórico.
   * Exporta: `data/caso_1/experimento_extrapolacion.csv`

4. **Generación de gráficos y figuras de análisis:**
   ```bash
   python scripts/caso_1/visualizar_caso_1.py
   ```
   * Exporta:
     * `images/caso_1/serie_punchana.png` (Serie térmica y lluvias)
     * `images/caso_1/benchmark_modelos.png` (RMSE y significancia Diebold-Mariano)
     * `images/caso_1/forecast_7d_cono.png` (Cono de incertidumbre P10-P90)
