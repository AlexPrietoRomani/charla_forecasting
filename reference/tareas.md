# Tareas — charla forecasting (SENAMHI + café NDVI)

`[ ]` pendiente · `[/]` en progreso · `[X]` hecho. Detalle largo en `plan_maestro.md`.

## F1 Datos
- [X] T1.1 Elegir estación SENAMHI (decidido: Iquitos; café con proxy declarado)
  - AC: código estación Iquitos + coords + periodo 2019-2025 anotados en `data/README.md`
  - Siguiente: `garua --search "Iquitos"` para fijar COD
- [X] T1.2 Descargar SENAMHI con garua → `data/raw/` + limpieza (S/D, T, dedup, diario)
  - AC: `% huecos` reportado; diario sin duplicados (`data/senamhi_diario.csv`, 92.9 KB)
  - Test: 2,557 días limpios (2019-2025), reporte documentado en `data/README.md`
- [X] T1.3 Pull Sentinel-2 (AgroVisión) NDVI/EVI mensual 2019-2025 sobre polígono
  - AC: serie mensual multiespectral guardada en `data/raw/s2_ndvi.csv` y `data/raw/s2_spectral_indices.csv`

## F2 Práctica clima
- [X] T2.1 Baselines: naive + ETS/ARIMA (holdout 90d: Naive RMSE 2.315 °C, ARIMA RMSE 2.121 °C)
- [X] T2.2 ML tabular RF/ExtraTrees/XGB con lags 1-14
  - AC: RMSE < naive en holdout (ExtraTrees RMSE 2.166 °C, RF RMSE 2.247 °C)
- [X] T2.3 LSTM 1 capa PyTorch (RMSE 2.097 °C, mejora 9.4% vs naive)
- [X] T2.4 Export `data/senamhi_diario.csv` + `senamhi_forecast_7d.csv` (<200KB)
  - Ambos CSVs listos para el deck interactivo vía PapaParse

## F3 Práctica café
- [X] T3.1 Armar tabla campaña: ∑EVI/NDVI ventana + lluvia/T° + qq/ha
  - Serie 2019-2025 agregada por ventanas (floración, llenado, cosecha)
- [X] T3.2 LOYO (Leave-One-Year-Out) → Fusión MAPE 4.4% vs Solo NDVI 5.4% (demostración empírica de saturación)
- [X] T3.3 Export `data/cafe_ndvi_rendimiento.csv` + papers en `refs.bib` + notebook `02_cafe_ndvi.ipynb`

## F4 Deck
- [X] T4.1 Esqueleto adaptado a `presentacion.html` expandido a 25 slides con layout full-bleed borde a borde
- [X] T4.2 Diagramas animados SVG interactivos estilo HyperFrames (curvas paramétricas, lags deslizantes, LSTM gates vs PatchTST, absorción espectral)
- [X] T4.3 Comparativa multi-agencia global (NOAA GFS vs ECMWF vs DWD ICON) con endpoint Open-Meteo y chart interactivo en Slide 14
- [X] T4.4 Mapas interactivos Leaflet con visor dinámico de capas/heatmaps (Satélite RGB, NDVI saturado, EVI biomasa, NDRE nitrógeno)
- [X] T4.5 Gráficos interactivos Chart.js cableados a `senamhi_forecast_7d.csv`, `noaa_ecmwf_forecast.csv` y `cafe_ndvi_rendimiento.csv` + fallbacks embebidos
- [X] T4.6 QA offline (doble clic sin servidor), teclado (←/→/F/Home/End) y switch tema claro/oscuro
- [X] T4.7 Motor HyperFrames GSAP (CDN 3.12.5): timelines secuenciados header→paneles,
  controles Narrar Replay/Paso 1-3 + teclas 1/2/3/R en 11 slides animadas,
  safety-timer progress(1) anti-stall, fallback sin-GSAP con todo visible.
  Auditoría 1600×900: 25/25 sin desborde vertical, stepping verificado.
- [X] T4.8 Fix charts 18/21 (columnas JS alineadas a CSV reales: tmax_observada/
  pred_random_forest/pred_xgboost/pred_lstm/ci_* y campania/rendimiento_obs_qq_ha/
  pred_modelo_fusion; check PASS 7pts+6campañas) + 6 diagramas SVG nivel distill.pub
  con sub-pasos data-hf-step (LSTM cinta+compuertas, PatchTST tokens+atención,
  ventana 2 filas, meseta+lineal+gap Δ4°C, hoja biofísica, saturación+crisis 2024).

## F5 Cierre
- [X] T5.1 Verificación de DoD global, datasets limpios (<200KB) y notebooks reproducibles
- [X] T5.2 Validación de los 4 paradigmas conceptuales y casos de estudio reales para Perú

