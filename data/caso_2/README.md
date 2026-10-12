# Caso 2: Rendimiento de Café en Jaén (MIDAGRI + Satélite MODIS + Clima ERA5)

Este directorio contiene los conjuntos de datos correspondientes al **Caso 2: Predicción de Rendimiento Agrícola y Trampa Biofísica del NDVI**.

## Zona de Estudio
* **Provincia:** Jaén, Departamento de Cajamarca, Perú (`-5.7049°`, `-79.0104°`).
* **Altitud y relieve:** Cuenca cafetalera nororiental (600 a 1,800 msnm).
* **Periodo cubierto:** 2001 a 2024 (24 campañas agrícolas continuas).

## Archivos del Caso 2
1. **`cafe_jaen_campanias.csv`**:
   * Dataset consolidado determinista alineado con el ciclo biológico del café (Floración: Ago-Oct, Llenado: Nov-Feb, Cosecha: Mar-Jul).
   * Columnas: `campania`, `rendimiento_kg_ha`, `rendimiento_qq_ha`, `superficie_cosechada_ha`, `produccion_t`, `ndvi_anual`, `evi_anual`, `lluvia_flor_mm`, `tmax_flor_c`, `anomalia_rend_kg_ha`, etc.
2. **`cafe_jaen_hipotesis.json`**:
   * Evaluación cuantitativa de las 4 hipótesis científicas (H1: Saturación espectral del NDVI, H2: Ventana crítica de floración, H3: Superioridad de índices corregidos EVI, H4: Fusión biofísica clima + satélite).
3. **`cafe_jaen_resultados.csv`**:
   * Métricas y pronósticos año a año evaluados bajo protocolo estricto de **Ventana Temporal Expansiva** (sin fuga temporal hacia el futuro).
   * Modelos comparados: M0 (Persistencia), M1 (Tendencia histórica), M2 (Solo satélite NDVI), M3 (Solo clima ERA5), M4 (Fusión clima + satélite).
4. **`deprecated/`**:
   * Datasets sintéticos previos aislados del pipeline oficial para asegurar la integridad de la investigación.
