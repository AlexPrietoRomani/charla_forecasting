# Plan Maestro — ¿Puede la IA predecir el futuro? (SENAMHI + café NDVI)

## 1. Qué vamos a presentar (narrativa, 25 slides avanzadas estilo Data_Wizard + HyperFrames)

Hilo: **predecir = cuantificar incertidumbre para decidir**. Dos casos reales Perú:
- **Caso A (clima):** pronóstico T°/lluvia estación SENAMHI con 5 niveles de modelo + comparativa multi-agencia (NOAA GFS vs ECMWF vs DWD ICON) + mapa satelital.
- **Caso B (café):** rendimiento qq/ha desde Sentinel-2 (EVI/NDRE vs saturación de NDVI) + clima + visor interactivo de capas y heatmaps.

Outline (detalle ampliado en `reference/estructura_presentacion.md`):
- **Bloque 1 (Fundamentos):** 1 Portada + gancho · 2 Anatomía de una serie desde cero (tendencia, ciclo, estacionalidad, ruido) · 3 El gran mapa de los 4 paradigmas.
- **Bloque 2 (Teoría & Mecanismos):** 4 Paradigma 1: Curvas paramétricas (exponencial, logística, Holt-Winters) · 5 Paradigma 1: Descomposición estadística (ARIMA, SARIMAX, Prophet) · 6 Paradigma 2: ML tabular mecanismo (lags SVG) · 7 Paradigma 2: Patología de no-extrapolación en árboles · 8 Paradigma 2: DL secuencial (LSTM vs PatchTST SVG) · 9 Paradigma 2: Cuándo usar DL (mito de la serie única) · 10 Paradigma 3: Visión agrícola (YOLOv12, SAM 2.1, DINOv2) · 11 Paradigma 3: Biofísica y saturación espectral (NDVI vs EVI/NDRE) · 12 Paradigma 3: Fusión multimodal fenológica · 13 Paradigma 4: Modelos globales (NOAA GFS, ECMWF IFS, DWD ICON) · 14 Paradigma 4: La disparidad en vivo para Iquitos · 15 Paradigma 4: GraphCast (DeepMind) y Zero-Shot (TimesFM, Chronos).
- **Bloque 3 (Casos Reales & Demos):** 16 Caso A mapa satelital Iquitos (Leaflet) · 17 Caso A benchmark 7 años · 18 Caso A DEMO clima 7d en vivo · 19 Caso B mapa satelital Jaén con Visor de Capas/Heatmaps (RGB, NDVI saturado, EVI, NDRE) · 20 Caso B prueba de las 6 campañas · 21 Caso B DEMO café en vivo (LOYO).
- **Bloque 4 (Cierre):** 22 Lecciones desde las trincheras · 23 Árbol de decisiones técnico · 24 Cierre (la IA no predice, cuantifica) · 25 Gracias + referencias BibTeX (`refs.bib`).

## 2. Cómo construir las dispos (igual que Data_Wizard, sin inventar stack)

- Single-file `presentacion.html`: Chart.js + PapaParse + Leaflet satelital vía CDN, CSS vars claro/oscuro, navegación `←/→/F/Inicio/Fin`, fallback embebido si no hay servidor.
- Layout full-bleed (`width: calc(100vw - 56px)`, `height: 100vh`) con split-panel grids para visualización panorámica sin restricciones de ancho.
- Datos del deck = **CSVs pequeños** en `data/`: `senamhi_diario.csv`, `senamhi_forecast_7d.csv`, `cafe_ndvi_rendimiento.csv`, `noaa_ecmwf_forecast.csv` (<100 KB c/u).
- Servir local: `python -m http.server 8000` → `.../presentacion.html`. Doble-clic funciona 100% offline con fallback embebido.
- DoD deck: abre offline, 25 slides, mapas satelitales Leaflet interactivos, visor de heatmaps, gráficos leen CSV en vivo, teclado OK.

## 3. Práctica A — Clima SENAMHI multi-modelo (1 estación cafetalera)

**Dato:** SENAMHI Perú solo permite descarga mes-a-mes con cuenta + Cloudflare. Usar `garua` (PyPI, MIT):
```bash
pip install garua
garua --search "Jaen"            # o Pichanaki / Quillabamba
garua --station <COD> --mode range --from 2019 --to 2025   # crudo → data/raw/ (ignorado)
```
Fallback si Turnstile bloquea: `senamhi-scraper` o descarga manual mes-a-mes al mismo `data/raw/`.
Limpieza: normalizar `S/D`→NaN, `T`→0.0, dedup fechas, resample diario, report huecos (% NaN por variable).
**Estación decidida:** Iquitos (Loreto, selva baja ~100 msnm) para práctica clima.
⚠️ Iquitos NO es zona café (café requiere 800-2000 msnm): la práctica café usará proxy declarado
(serie pública café Colombia/Brasil o adaptación [@niedbala2022]) + Sentinel-2 sobre zona cafetalera
referencial (Jaén por defecto). En slides se declara: clima = Iquitos real, café = proxy.

**Modelos (mismo split temporal, mismo target T°máx o lluvia 7 días):**
| Nivel | Modelo | Paquete |
|---|---|---|
| baseline | Naive estacional + ETS/ARIMA | statsmodels |
| clásico | Prophet | prophet |
| ML tabular | RF + XGBoost/LightGBM con lags 1-14 + dummies mes | scikit-learn, xgboost/lightgbm |
| DL | LSTM 1 capa | pytorch o keras |
| zero-shot | Chronos o TimesFM sin entrenar | `chronos-forecasting` / `timesfm` |

Validación: **TimeSeriesSplit 5 folds + holdout últimos 90 días** (nunca shuffle). Métricas: MAE/RMSE + cobertura intervalo. Export demo: `data/senamhi_diario.csv` (últimos 180 días obs) + `senamhi_forecast_7d.csv` (obs + 5 columnas pronóstico).
Notebook: `notebooks/01_clima_senamhi.ipynb`. Golden: RMSE RF < naive en holdout; CSVs existen y cargan en deck.

## 4. Práctica B — Café + NDVI (rendimiento qq/ha)

**Dato:** Sentinel-2 L2A vía Google Earth Engine (abierto) + clima SENAMHI estación elegida + rendimiento (ideal: serie anual del productor/coop; fallback: proxy o dataset paper arándano/uva [@niedbala2022] adaptado y declarado como tal).
Ventana fenológica café Perú: floración (ago-oct) → llenado (nov-feb) → cosecha (mar-jul). Features: **∑NDVI / max NDVI / EVI medio en ventana** + lluvia acumulada + T° media (misma ventana). Target: qq/ha por campaña.
```python
# ponytail: GEE punto/buffer finca, mediana mensual, mascara nubes SCL
import ee
ee.Initialize()
s2 = (ee.ImageCollection('COPERNICUS/S2_SR_HARMONIZED')
  .filterBounds(finca).filterDate('2019-01-01','2025-12-31')
  .map(lambda i: i.updateMask(i.select('SCL').neq(3).And(i.select('SCL').neq(9))))
ndvi = s2.median().normalizedDifference(['B8','B4'])
```
Modelos: RF + XGBoost (pocos datos = no DL). Validación: **leave-one-year-out**. Métrica: MAPE + R². Export demo: `data/cafe_ndvi_rendimiento.csv` (campaña, ndvi_acum, lluvia, temp, rendimiento_obs, pred_rf).
Notebook: `notebooks/02_cafe_ndvi.ipynb`. Golden: MAPE < 25% o declarado + CSV carga en deck con slider fenología.
Riesgo honesto para la slide 13: NDVI se satura en dosel denso y falla sin ventana fenológica — mostrarlo con 2 campañas.

## 5. Fases y orden

- F0 Setup (hecho repo + falta: `pip install garua pandas scikit-learn statsmodels prophet xgboost lightgbm torch chronos-forecasting earthengine-api`) 
- F1 Datos: elegir estación + descargar SENAMHI + definir polígono café + pulls S2
- F2 Práctica A notebook + CSVs demo clima
- F3 Práctica B notebook + CSV demo café (+ 2-3 papers café-NDVI a refs.bib)
- F4 Deck `presentacion.html` clonando Data_Wizard (copiar esqueleto, adaptar 16 slides, cablear CSVs)
- F5 Ensayo: offline OK, tiempos, fallback.

## Apéndice A — DoD global por tarea
Notebook corre top-to-bottom limpio + CSVs demo <200KB + validación temporal sin leakage + deck lee CSV en vivo + commit sin PDFs/pesos/datos crudos.
