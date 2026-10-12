# Datos Deprecados y Sintéticos — Registro de Auditoría

> **Fecha de aislamiento:** 2026-10-04  
> **Motivo:** Auditoría de integridad científica. **NO USAR EN PRODUCCIÓN NI EN PRESENTACIÓN.**

## Archivos Aislados:
1. `cafe_ndvi_rendimiento_SINTETICO.csv` (anteriormente `data/cafe_ndvi_rendimiento.csv`)
2. `scripts/deprecated_build_agro_dataset_SINTETICO.py` (anteriormente `scripts/build_agro_dataset.py`)

## Hallazgos de la Auditoría Forense:
* **Rendimiento de café (qq/ha):** El script generaba la variable objetivo mediante una fórmula paramétrica ad-hoc (`15.0 + 14.0 * (EVI/2.6) + 4.0 * (lluvia/400) - 2.5 * max(0, Tmax - 31) + np.random.normal(0, 0.8)`). No provenía de ninguna cooperativa, productor ni agencia oficial (MIDAGRI/SIEA).
* **Índices espectrales (NDVI, EVI, NDRE, NDWI):** No correspondían a imágenes satelitales Sentinel-2 descargadas; fueron simulados mes a mes mediante funciones periódicas sinusoidales y una función sigmoide artificial que forzaba la saturación del NDVI en ~0.788.
* **Sesgo de circularidad:** El modelo de Machine Learning que "ganaba" la predicción solo aprendía los mismos coeficientes con los que el script había fabricado el dato sintético.

## Acción Correctiva (Fase 2 del Plan Maestro):
Reconstrucción completa del Caso B usando:
* Serie histórica oficial de producción y rendimiento agrícola de la provincia de Jaén (MIDAGRI - SIEA).
* Reflectancias e índices multiespectrales reales extraídos de MODIS MOD13Q1 y Sentinel-2 L2A mediante Microsoft Planetary Computer STAC API.
* Clima diario real ERA5 descargado de Open-Meteo Archive.
