# Tareas — charla forecasting (SENAMHI + café NDVI)

`[ ]` pendiente · `[/]` en progreso · `[X]` hecho. Detalle largo en `plan_maestro.md`.

## F1 Datos
- [ ] T1.1 Elegir estación SENAMHI (defecto Jaén; alt Pichanaki/Quillabamba) + polígono finca café
  - AC: código estación + coords + periodo 2019-2025 anotados en `data/README.md`
- [ ] T1.2 Descargar SENAMHI con garua → `data/raw/` + limpieza (S/D, T, dedup, diario)
  - AC: `% huecos` reportado; diario sin duplicados
  - Test: notebook corre `garua --doctor` + lee 1 CSV crudo
- [ ] T1.3 Pull Sentinel-2 (GEE) NDVI/EVI mensual 2019-2025 sobre polígono
  - AC: serie mensual sin nubes (máscara SCL) guardada en `data/raw/s2_ndvi.csv`

## F2 Práctica clima
- [ ] T2.1 Baselines: naive + ETS/ARIMA + Prophet (holdout 90d, TimeSeriesSplit)
- [ ] T2.2 ML tabular RF/XGB/LGBM con lags 1-14
  - AC: RMSE < naive en holdout
- [ ] T2.3 LSTM 1 capa + Chronos/TimesFM zero-shot
- [ ] T2.4 Export `data/senamhi_diario.csv` + `senamhi_forecast_7d.csv` (<200KB)
  - Test usuario: deck lee ambos vía PapaParse

## F3 Práctica café
- [ ] T3.1 Armar tabla campaña: ∑NDVI/EVI ventana + lluvia/T° + qq/ha
- [ ] T3.2 RF/XGB + leave-one-year-out → MAPE/R²
- [ ] T3.3 Export `data/cafe_ndvi_rendimiento.csv` + 2-3 papers café a `refs.bib`

## F4 Deck
- [ ] T4.1 Copiar esqueleto `Data_Wizard/presentacion.html` → `presentacion.html`, retitular 16 slides
- [ ] T4.2 Cablear 4 gráficos a los 3 CSVs + fallbacks embebidos
- [ ] T4.3 QA offline (doble-clic sin servidor) + teclado + claro/oscuro

## F5 Cierre
- [ ] T5.1 Ensayo 20 min + commit final (sin PDFs/pesos/crudo)
