# Pipeline del Caso 2: Rendimiento de Café en Jaén (MIDAGRI + Satélite + Clima)

Este directorio contiene los scripts para la extracción de fuentes oficiales, teledetección satelital, fusión fenológica y evaluación de hipótesis del **Caso 2: Café en Jaén**.

## Flujo de Ejecución (Extracción a Validación Expansiva)

1. **Compilación de rendimientos oficiales:**
   ```bash
   python scripts/caso_2/compile_midagri_jaen.py
   ```
   * Extrae y audita compendios INEI / MIDAGRI (2010 a 2024).

2. **Descarga de reanálisis ERA5:**
   ```bash
   python scripts/caso_2/fetch_clima_jaen.py
   ```
   * Extrae microclima histórico diario de Open-Meteo Archive (2000-2024).

3. **Extracción satelital MODIS:**
   ```bash
   python scripts/caso_2/extract_modis_jaen.py
   ```
   * Descarga compuestos MOD13Q1 (250m, 16d) vía Planetary Computer STAC API.

4. **Fusión determinista fenológica:**
   ```bash
   python scripts/caso_2/build_cafe_real.py
   ```
   * Integra rendimientos oficiales, ventanas fenológicas de floración y llenado, y anomalías.
   * Exporta: `data/caso_2/cafe_jaen_campanias.csv`

5. **Evaluación de hipótesis y validación temporal expansiva:**
   ```bash
   python scripts/caso_2/eval_hipotesis_cafe.py
   ```
   * Audita las hipótesis científicas H1 a H4.
   * Evalúa modelos M0 a M4 en ventana expansiva (sin contaminación futura).
   * Exporta: `data/caso_2/cafe_jaen_hipotesis.json` y `data/caso_2/cafe_jaen_resultados.csv`

6. **Generación de gráficos y figuras de análisis:**
   ```bash
   python scripts/caso_2/visualizar_caso_2.py
   ```
   * Exporta:
     * `images/caso_2/rendimiento_historico.png` (Serie oficial de café y crisis de roya)
     * `images/caso_2/saturacion_ndvi.png` (Curva de saturación espectral)
     * `images/caso_2/comparativa_modelos_cafe.png` (Error MAE y RMSE M0-M4)
