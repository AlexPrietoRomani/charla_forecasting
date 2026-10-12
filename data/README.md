# Diccionario y Organización de Datos — Charla Forecasting

Los datos del proyecto se encuentran estrictamente organizados por caso de estudio para garantizar trazabilidad, reproducibilidad y separación de responsabilidades:

```text
data/
├── caso_1/                   # Caso 1: Clima SENAMHI Punchana (Iquitos, Loreto)
│   ├── senamhi_diario.csv             # Serie diaria histórica procesada (2019-2025, 2,557 días)
│   ├── benchmark_punchana.csv         # Resultados del benchmark de 8 modelos con Diebold-Mariano
│   ├── senamhi_forecast_7d.csv        # Pronóstico a 7 días con bandas de incertidumbre P10-P90
│   ├── noaa_ecmwf_forecast.csv        # Pronóstico físico global NOAA GFS vs ECMWF IFS en Iquitos
│   ├── experimento_extrapolacion.csv  # Evaluación de falla de extrapolación con árboles de decisión
│   └── README.md                      # Ficha técnica y variables del Caso 1
├── caso_2/                   # Caso 2: Rendimiento de Café en Jaén (Cajamarca)
│   ├── cafe_jaen_campanias.csv        # Dataset consolidado fenológico (2001-2024, 24 campañas)
│   ├── cafe_jaen_hipotesis.json       # Auditoría empírica de hipótesis biológicas y espectrales (H1-H4)
│   ├── cafe_jaen_resultados.csv       # Métricas de validación temporal expansiva (M0 a M4)
│   ├── deprecated/                    # Datos sintéticos archivados (históricos)
│   └── README.md                      # Ficha técnica, fuentes oficiales y sensores del Caso 2
├── README.md                 # Este documento
└── SOURCES.md                # Registro formal de fuentes, hashes SHA-256 y licencias
```

---

## 1. Caso 1: Clima SENAMHI — Estación Punchana (Iquitos, Loreto)
* **Ubicación:** `data/caso_1/`
* **Código estación:** `103015` (frontend code `150208`)
* **Ubicación geográfica:** Punchana, Maynas, Loreto, Perú (`-3.6903°`, `-73.2556°`, `91 msnm`)
* **Periodo cubierto:** `2019-01-01` a `2025-12-31` (7 años continuos, 2,557 días)
* **Variables principales:** `tmax` (°C), `tmin` (°C), `precip` (mm), `humedad` (%)

---

## 2. Caso 2: Café / Agro — Rendimiento Oficial y Teledetección (Jaén, Cajamarca)
* **Ubicación:** `data/caso_2/`
* **Zona de estudio:** Jaén, Cajamarca, Perú (capital cafetalera nororiental, `-5.7049°`, `-79.0104°`)
* **Fuentes Oficiales:** Compendios Estadísticos INEI / MIDAGRI-SIEA (2010 a 2024)
* **Sensores satelitales:** MODIS Terra MOD13Q1 (250m, 16d, 2000-2024) y Sentinel-2 L2A (10m)
* **Reanálisis climático:** ERA5 vía Open-Meteo Archive (temperatura, lluvia, radiación y ET0)
* **Ventanas fenológicas:** Floración (Ago-Oct), Llenado/Expansión (Nov-Feb), Cosecha (Mar-Jul)
