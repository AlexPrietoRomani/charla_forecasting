# ¿Puede la IA predecir el futuro? Lecciones de forecasting desde el mundo real

Charla estilo `Data_Wizard`: deck interactivo single-file `presentacion.html` (Chart.js + datos CSV en vivo).

## Estructura
```text
charla_forecasting/
├── presentacion.html   # deck final interactivo (23 slides, Chart.js + datos reales)
├── front/              # código frontend de las diapositivas (estilos, slides, notas, branding)
├── back/               # motor backend de compilación y datos (build_deck.py, test_loader.py)
├── data/               # datos separados por casos de estudio
│   ├── caso_1/         # Caso 1: Clima SENAMHI Punchana (Iquitos)
│   └── caso_2/         # Caso 2: Rendimiento Café Jaén (Cajamarca)
├── docs/               # documentación y activos del proyecto (Project Suite)
│   ├── reference/      # planes, fases de trabajo y especificaciones de la charla
│   └── images/         # repositorio centralizado de imágenes y gráficos
│       ├── front/      # assets visuales del front/diapositivas (fondos, logos, QR, perfil)
│       ├── caso_1/     # figuras y gráficos de análisis de Clima SENAMHI
│       └── caso_2/     # figuras y gráficos de análisis de Café Jaén
├── scripts/            # pipelines de ejecución organizados
│   ├── caso_1/         # ETL, benchmark y modelos de Clima Iquitos
│   ├── caso_2/         # Satélite, clima ERA5, MIDAGRI y modelos Café Jaén
│   ├── pagina/         # generador de imágenes del deck, auditoría de layout y utilidades
│   └── build_deck.py   # proxy de compilación hacia back/build_deck.py
├── notebooks/          # demos Jupyter (01_clima_senamhi, 02_cafe_ndvi)
├── articles/           # papers descargados (PDF+MD, NO se versionan — ver .gitignore)
├── models/             # pesos .pt/.pkl/etc (NO se versionan)
├── refs.bib            # bibliografía académica
└── .gitignore
```

## Estado
- [x] Repo init + estructura
- [x] Investigación (ML/DL/series/CV + SENAMHI Iquitos + Café NDVI/EVI AgroVisión)
- [x] Demos mínimas y notebooks (`notebooks/01_clima_senamhi.ipynb`, `notebooks/02_cafe_ndvi.ipynb`)
- [x] Datasets procesados y exportados (<100KB en `data/`)
- [x] Deck interactivo single-file `presentacion.html` (16 slides, Chart.js, modo claro/oscuro, soporte offline)
