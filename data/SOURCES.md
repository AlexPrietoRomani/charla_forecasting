# Registro de Fuentes de Datos (SOURCES.md)

Este documento registra la procedencia, endpoints oficiales, parámetros de descarga y sumas de verificación SHA-256 de todos los datos utilizados en el proyecto. **Regla de integridad: Cero datos sintéticos no declarados.**

---

## 1. Clima Punchana — SENAMHI Perú (Caso A)

* **Archivo Procesado:** `data/senamhi_diario.csv`
* **SHA-256:** `5C2D1BDD7A94E0BDB9AFBEB2F98EF9D014C1FE706DD027D9EBE9AAF80D6588E9`
* **Fuente:** Servicio Nacional de Meteorología e Hidrología del Perú (SENAMHI)
* **Estación:** Punchana (Código estación: `103015`, código web: `150208`)
* **Ubicación:** Punchana, Maynas, Loreto, Perú (`-3.6903°`, `-73.2556°`, altitud `91 msnm`)
* **Periodo:** `2019-01-01` a `2025-12-31` (2,557 días continuos)
* **Método de Extracción:** Descarga automatizada vía librería de código abierto `garua` (PyPI, MIT)
* **Variables:** `tmax` (°C), `tmin` (°C), `precip` (mm), `humedad` (%)
* **Tratamiento:**
  * Duplicados de fecha eliminados.
  * `tmax`: 9.7% de faltantes (249 días) interpolados linealmente con límite temporal.
  * `precip`: Imputación controlada a 0.0 mm en días sin registro de lluvia.
* **Archivo Crudo:** `data/raw/senamhi_punchana_raw.csv`

---

## 2. Pronóstico Multi-Agencia Global en Iquitos (Caso A)

* **Archivo:** `data/noaa_ecmwf_forecast.csv`
* **SHA-256:** `73D8A48E038459CB11DF10A353682BC3CE694DB503644BCFA898603FE1CDE865`
* **Fuente:** Open-Meteo Weather Forecast API (`https://api.open-meteo.com/v1/forecast`)
* **Coordenadas:** `-3.6903°`, `-73.2556°` (Estación Punchana)
* **Modelos Consultados:**
  * NOAA GFS (Global Forecast System, EE.UU., resolución 0.25°)
  * ECMWF IFS (Integrated Forecasting System, Europa, resolución 0.1°)
* **Parámetros:** `hourly=temperature_2m,precipitation`, agregados a nivel diario (Tmax, Tmin, Lluvia acumulada)
* **Fecha de Extracción:** Octubre 2026

---

## 3. Clima Reanálisis ERA5 para Jaén (Caso B)

* **Archivo:** `data/raw/cafe_real/clima_jaen_diario.csv`
* **SHA-256:** `7068bd19385885215ad44823d9ca92496f79437a5480e5131d7c00c689f28461`
* **Fuente:** Open-Meteo Historical Weather Archive API (`https://archive-api.open-meteo.com/v1/archive`)
* **Coordenadas:** `-5.7049°`, `-79.0104°` (Centroide de la provincia de Jaén, Cajamarca, Perú)
* **Periodo:** `2000-01-01` a `2024-12-31` (9,132 días continuos)
* **Variables:** `tmax`, `tmin`, `tmean`, `lluvia_mm`, `et0_mm`, `rad_mj_m2`
* **Tratamiento:** Reanálisis ERA5 (ECMWF) determinista sin modificación de escala ni perturbaciones sintéticas.

---

## 4. Rendimiento Histórico Oficial de Café — Jaén (Caso B)

* **Archivo:** `data/raw/cafe_real/midagri_jaen_rendimiento.csv`
* **SHA-256:** `d871d15ff3e15c33d472d2ccf4dcd515c492abbc27c75ced2db99171fcd93d35`
* **Fuente Primaria:** Instituto Nacional de Estadística e Informática (INEI) y Dirección Regional de Agricultura y Riego - Cajamarca (MIDAGRI)
* **Documentos Oficiales Auditados:**
  1. *Compendio Estadístico Cajamarca 2017* (Libro digital Lib1492): Cuadro 12.1.8 (p. 231) y Cuadro 12.2.8 (p. 245) para las campañas 2010 a 2016.
  2. *Compendio Estadístico Cajamarca 2025* (CompDptal2025): Cuadro 12.1.8 (p. 213) y Cuadro 12.2.8 (p. 227) para las campañas 2018 a 2024.
* **Control de Calidad:** Verificación aritmética de coherencia: `abs(produccion_t * 1000 / superficie_cosechada_ha - rendimiento_kg_ha) / rendimiento_kg_ha < 0.001` (100% de registros aprobados).
* **Unidades:** Rendimiento reportado en `kg/ha` y convertido a quintales pergamino `qq/ha` (factor oficial: `1 qq = 46 kg`).

---

## 5. Teledetección Satelital Real MODIS — Jaén (Caso B)

* **Archivo:** `data/raw/cafe_real/modis_jaen_16d.csv`
* **SHA-256:** `2e1a2132c8ed9a0aa9bc61d4eed61b223f749713f7906cb25d8d5d058e8e7c5d`
* **Sensor:** MODIS Terra (MOD13Q1 v6.1, resolución 250 m, 16 días, periodo 2000–2024, 576 compuestos)
* **Plataforma:** Microsoft Planetary Computer STAC API (Colección `modis-13Q1-061`)
* **Límite Espacial:** `data/raw/cafe_real/jaen_limite.geojson` (SHA-256: `412b8b46de38dde624001a6e8ada901807c473e08d1d0730b4aee793850ce156`, Fuente: geoBoundaries ADM2 ID `86281439B77742651017236`).
* **Tratamiento:** Píxeles filtrados por máscara de fiabilidad (`pixel_reliability` 0 y 1); mediana espacial calculada en ventana de la cuenca cafetalera.

---

## 6. Dataset Consolidado Fenológico y Resultados de Hipótesis (Caso B)

* **Archivo Consolidado:** `data/cafe_jaen_campanias.csv`
* **SHA-256:** `1931b33e74009005427e2b8f937c089b0debd3d43253da17337ef510732aa421`
* **Resultados Validación Expansiva:** `data/cafe_jaen_resultados.csv` (SHA-256: `24f1ffeafe379d9ce8ef1845c273676627db83b86d79043b5b001424ad86feae`)
* **Auditoría de Hipótesis H1-H4:** `data/cafe_jaen_hipotesis.json` (SHA-256: `e03edb8f2d379083532e121e921edc9ed3e4bc69716cfbb2575c9e5f1f279847`)
* **Código Generador:** `scripts/build_cafe_real.py` (cero llamadas a `np.random`).

---

## 7. Benchmark de 8 Modelos en Iquitos (Caso A)

* **Archivo del Benchmark:** `data/benchmark_punchana.csv`
* **SHA-256:** `76f7fd8bc75e5688b05f9bc45628ee759b27254f8c4c8db8221fd79e49eff1b1`
* **Archivo de Pronóstico 7 Días:** `data/senamhi_forecast_7d.csv`
* **SHA-256:** `b04dac5b08c9242050e10c185fac98d3992ba40cd256b48df95a35094b57298b`
* **Metodología:** Holdout ciego de 90 días (Octubre-Diciembre 2025). Prueba de Diebold-Mariano con corrección de Harvey-Leybourne-Newbold (1997).
* **Modelos:** Naive Estacional, ARIMA (2,0,1), Holt-Winters Amortiguado, Random Forest, ExtraTrees, LSTM (PyTorch, 5 semillas), Chronos-T5 (Amazon Zero-Shot), TimesFM 2.5 200M (Google Zero-Shot).
