# ¿Puede la IA predecir el futuro? Lecciones de forecasting desde el mundo real

Charla estilo `Data_Wizard`: deck interactivo single-file `presentacion.html` (Chart.js + datos CSV en vivo).

## Estructura
```text
charla_forecasting/
├── presentacion.html   # deck final (a construir, clonando estilo Data_Wizard)
├── articles/           # papers descargados (PDF+MD, NO se versionan — ver .gitignore)
├── data/               # CSVs demo del deck (temperatura, NDVI-fruta)
├── models/             # pesos .pt/.pkl/etc (NO se versionan)
├── images/             # assets del deck
├── notebooks/          # demos (temperatura, NDVI)
├── reference/          # Brief + outline de la charla
├── refs.bib            # bibliografía (resultado de la investigación)
└── .gitignore
```

## Estado
- [x] Repo init + estructura
- [x] Investigación (ML/DL/series/CV + SENAMHI Iquitos + Café NDVI/EVI AgroVisión)
- [x] Demos mínimas y notebooks (`notebooks/01_clima_senamhi.ipynb`, `notebooks/02_cafe_ndvi.ipynb`)
- [x] Datasets procesados y exportados (<100KB en `data/`)
- [x] Deck interactivo single-file `presentacion.html` (16 slides, Chart.js, modo claro/oscuro, soporte offline)
