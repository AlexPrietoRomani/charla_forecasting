# ¿Puede la IA predecir el futuro? Lecciones de forecasting desde el mundo real

Charla estilo `Data_Wizard`: deck interactivo single-file `presentacion.html` (Chart.js + datos CSV en vivo).

## Estructura
```text
charla_forecasting/
├── presentacion.html   # deck final interactivo (23 slides, Chart.js + datos reales)
├── articles/           # papers descargados (PDF+MD, NO se versionan — ver .gitignore)
├── data/               # datos separados por casos
│   ├── caso_1/         # Caso 1: Clima SENAMHI Punchana (Iquitos)
│   └── caso_2/         # Caso 2: Rendimiento Café Jaén (Cajamarca)
├── models/             # pesos .pt/.pkl/etc (NO se versionan)
├── images/             # assets del deck y gráficos generados
├── notebooks/          # demos Jupyter (01_clima_senamhi, 02_cafe_ndvi)
├── docs/               # documentación del proyecto (Project Suite)
│   └── reference/      # planes, fases de trabajo y especificaciones de la charla
├── scripts/            # scripts organizados por casos y deck
│   ├── caso_1/         # ETL, benchmark y modelos de Clima Iquitos
│   ├── caso_2/         # Satélite, clima ERA5, MIDAGRI y modelos Café Jaén
│   └── build_deck.py   # ensamblador del deck interactivo
├── refs.bib            # bibliografía académica
└── .gitignore
```

## Estado
- [x] Repo init + estructura
- [x] Investigación (ML/DL/series/CV + SENAMHI Iquitos + Café NDVI/EVI AgroVisión)
- [x] Demos mínimas y notebooks (`notebooks/01_clima_senamhi.ipynb`, `notebooks/02_cafe_ndvi.ipynb`)
- [x] Datasets procesados y exportados (<100KB en `data/`)
- [x] Deck interactivo single-file `presentacion.html` (16 slides, Chart.js, modo claro/oscuro, soporte offline)
