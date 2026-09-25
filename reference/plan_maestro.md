# Plan Maestro — ¿Puede la IA predecir el futuro? (SENAMHI + café NDVI)

## 1. Qué vamos a presentar (narrativa, 16 slides clon Data_Wizard)

Hilo: **predecir = cuantificar incertidumbre para decidir**. Dos casos reales Perú:
- **Caso A (clima):** pronóstico T°/lluvia estación SENAMHI con 5 niveles de modelo.
- **Caso B (café):** rendimiento qq/ha desde NDVI Sentinel-2 + clima.

Outline (detalle en `reference/estructura_presentacion.md`, adaptar slides 9-12 a SENAMHI/café):
1 Portada + gancho · 2 Mapa 4 familias + zero-shot · 3 ML tabular (RF→XGB/LGBM/CatBoost)
4 Series clásicas (ARIMA/ETS/Prophet) · 5 DL (LSTM/DeepAR/N-BEATS/TFT/PatchTST)
6 Zero-shot (TimesFM/Chronos/Lag-Llama/Moirai) · 7 CV (YOLO conteo vs U-Net máscara vs ViT)
8 Fusión NDVI+clima · **9-10 DEMO clima SENAMHI en vivo** · **11-12 DEMO café NDVI en vivo**
13 Lecciones (validación temporal, costo del error, NDVI se satura)
14 Receta ¿qué modelo cuándo? · 15 Cierre · 16 Gracias+refs.

## 2. Cómo construir las dispos (igual que Data_Wizard, sin inventar stack)

- Single-file `presentacion.html`: Chart.js + PapaParse + Leaflet vía CDN, CSS vars claro/oscuro, navegación `←/→/F/Inicio/Fin`, fallback embebido si no hay servidor.
- Datos del deck = **CSVs pequeños** en `data/`: `senamhi_diario.csv`, `senamhi_forecast_7d.csv`, `cafe_ndvi_rendimiento.csv` (<200 KB c/u). Lo pesado (SENAMHI crudo, GeoTIFF) **no** entra al deck ni al git.
- Servir local: `python -m http.server 8000` → `.../presentacion.html`. Doble-clic funciona con fallback.
- DoD deck: abre offline, 16 slides, gráficos leen CSV en vivo, teclado OK.

## 3. Práctica A — Clima SENAMHI multi-modelo (1 estación cafetalera)

**Dato:** SENAMHI Perú solo permite descarga mes-a-mes con cuenta + Cloudflare. Usar `garua` (PyPI, MIT):
```bash
pip install garua
garua --search "Jaen"            # o Pichanaki / Quillabamba
garua --station <COD> --mode range --from 2019 --to 2025   # crudo → data/raw/ (ignorado)
```
Fallback si Turnstile bloquea: `senamhi-scraper` o descarga manual mes-a-mes al mismo `data/raw/`.
Limpieza: normalizar `S/D`→NaN, `T`→0.0, dedup fechas, resample diario, report huecos (% NaN por variable).
**Estación por defecto:** Jaén (Cajamarca, café). Alternativas: Pichanaki (Junín), Quillabamba (Cusco). Decidir en T1.

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
