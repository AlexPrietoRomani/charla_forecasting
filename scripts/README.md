# Directorio de Scripts (`scripts/`)

El directorio `scripts/` organiza el pipeline de datos, modelos y herramientas de la página:

```text
scripts/
├── caso_1/                   # Caso 1: Clima SENAMHI Punchana (Iquitos)
│   ├── clean_senamhi.py               # Limpieza e imputación de la serie diaria SENAMHI
│   ├── benchmark_punchana.py          # Benchmark de 8 modelos, test Diebold-Mariano y forecast 7d
│   ├── train_clima_models.py          # Entrenamiento multi-modelo con validación temporal
│   ├── experimento_no_extrapolacion.py# Experimento de fallo de extrapolación con árboles
│   ├── visualizar_caso_1.py           # Generación de gráficos y figuras en docs/images/caso_1/
│   └── README.md                      # Documentación del pipeline Caso 1
├── caso_2/                   # Caso 2: Rendimiento Café Jaén (MIDAGRI + Satélite)
│   ├── compile_midagri_jaen.py        # Extracción y auditoría de anuarios MIDAGRI / INEI
│   ├── fetch_clima_jaen.py            # Descarga de reanálisis ERA5 vía Open-Meteo
│   ├── extract_modis_jaen.py          # Extracción satelital MODIS MOD13Q1 de Planetary Computer
│   ├── extract_satellite_series.py    # Extracción Sentinel-2 con máscara de calidad
│   ├── build_cafe_real.py             # Fusión determinista fenológica a data/caso_2/
│   ├── eval_hipotesis_cafe.py         # Evaluación de H1-H4 y validación expansiva M0-M4
│   ├── train_cafe_models.py           # Modelado predictivo de rendimiento
│   ├── test_cdse.py                   # Verificación de credenciales Copernicus CDSE
│   ├── test_pbi.py                    # Inspección de tablero PowerBI MIDAGRI
│   ├── visualizar_caso_2.py           # Generación de gráficos y figuras en docs/images/caso_2/
│   ├── deprecated_build_agro_dataset_SINTETICO.py # Script histórico sintético aislado
│   └── README.md                      # Documentación del pipeline Caso 2
├── pagina/                   # Herramientas de soporte de la Página / Diapositivas
│   ├── generar_imagenes_deck.py       # Orquestador general de figuras y verificación de assets
│   ├── audit_layout.py                # Auditoría visual Playwright contra espacios vacíos
│   ├── take_screenshots.py            # Captura de pantalla de diapositivas seleccionadas
│   ├── verify_presentation.py         # Verificación en navegador con consola de errores
│   ├── inspect_slides.py              # Inspección sintáctica de títulos y slides
│   ├── generate_notebooks.py          # Generador de notebooks Jupyter en notebooks/
│   └── README.md                      # Documentación de herramientas de la página
├── audit_f9_desaturacion.py  # Validador F9: desaturación de color
├── audit_f10_layout_typography.py # Validador F10: layout y tipografía de los 21 prototipos y el bundle
├── audit_f12_claridad.py     # Validador F12: claridad no estadística (`--all`, `--bundle`; tests en test_audit_f12_claridad.py)
├── build_deck.py             # Proxy de compatibilidad hacia back/build_deck.py
└── README.md                 # Este documento
```

## Estructura de Front y Back
* **Frontend:** El código de estilos, diapositivas y marcas se encuentra en [`front/`](file:///home/aprietor/github/charla_forecasting/front/).
* **Backend:** El motor de compilación y enlace de datos se encuentra en [`back/`](file:///home/aprietor/github/charla_forecasting/back/).

## Validadores de fase

```bash
python scripts/audit_f12_claridad.py --all      # glosario, cifras, hero, rutas, videos (0 fallos esperados)
python scripts/audit_f12_claridad.py --bundle   # glosario presente en presentacion.html compilado
PYTHONIOENCODING=utf-8 python scripts/audit_f10_layout_typography.py
```

`audit_f10_layout_typography.py` conserva dos avisos heredados que no son de F12: faltan las 46 capturas `f10_*` y el marcador S5 `ŷ<sub>t+h</sub>` (texto del cierre anterior, reemplazado en F12 por el cierre en 3 frases de la diapo 29).
