# Diccionario de Datos — Charla Forecasting

## 1. Clima SENAMHI: Estación Punchana (Iquitos, Loreto)
* **Código estación:** `103015` (frontend code `150208`)
* **Ubicación:** Punchana, Maynas, Loreto, Perú
* **Coordenadas:** Latitud `-3.6903°`, Longitud `-73.2556°`, Altitud `91 msnm`
* **Periodo cubierto:** `2019-01-01` a `2025-12-31` (7 años continuos, 2,557 días)
* **Archivo crudo:** `data/raw/senamhi_punchana_raw.csv` (descargado con `garua` v0.30.0)
* **Archivo procesado:** `data/senamhi_diario.csv` (92.9 KB)

### Reporte de calidad y huecos (% NaN en datos crudos):
* `tmax`: 9.7% de datos faltantes (249 días) $\rightarrow$ interpolación lineal con límite temporal. Media 31.7 °C, Mín 19.2 °C (friaje), Máx 38.0 °C.
* `precip`: 11.1% de datos faltantes (283 días) $\rightarrow$ imputación controlada 0.0 mm.
* `tmin`: 24.8% de datos faltantes (633 días).
* `humedad`: 26.1% de datos faltantes (667 días).

---

## 2. Caso Café / Agro: Zona de Referencia y Variables Satelitales
* **Zona de estudio:** Jaén, Cajamarca, Perú (capital cafetalera nororiental)
* **Coordenadas:** Latitud `-5.6766°`, Longitud `-78.7742°`, Altitud media `618 - 1200 msnm`
* **Sensores y variables:**
  * **Sentinel-2 L2A:** Reflectancias de superficie (B02 Azul, B04 Rojo, B05 Red-Edge, B08 NIR) con máscara de nubes SCL.
  * **Índices espectrales:** NDVI, EVI (Huete 2002), SAVI (Huete 1988), NDRE (Barnes 2000), NDWI (Gao 1996).
  * **Microclima (Open-Meteo Archive):** Temperatura media, precipitación acumulada, VPD (déficit de presión de vapor), radiación solar y ET0.
  * **Ventanas fenológicas:** Floración (Ago-Oct), Llenado/Expansión (Nov-Feb), Cosecha (Mar-Jul).
