# Módulos y Scripts del Proyecto — Charla Forecasting

La carpeta `scripts/` se estructura en subdirectorios modulares según los casos de aplicación y la construcción del deck interactivo:

```text
scripts/
├── caso_1/                   # Scripts del Caso 1: Clima SENAMHI Punchana (Iquitos)
│   ├── clean_senamhi.py               # Limpieza e interpolación de la serie diaria SENAMHI
│   ├── benchmark_punchana.py          # Benchmark de 8 modelos, test Diebold-Mariano y forecast 7d
│   ├── train_clima_models.py          # Entrenamiento multi-modelo con validación temporal
│   ├── experimento_no_extrapolacion.py# Experimento de fallo de extrapolación con árboles
│   ├── visualizar_caso_1.py           # Generación de gráficos y figuras de análisis en images/caso_1/
│   └── README.md                      # Pipeline y ejecución del Caso 1
├── caso_2/                   # Scripts del Caso 2: Rendimiento Café Jaén (MIDAGRI + Satélite)
│   ├── compile_midagri_jaen.py        # Extracción y auditoría de anuarios MIDAGRI / INEI
│   ├── fetch_clima_jaen.py            # Descarga de reanálisis ERA5 vía Open-Meteo
│   ├── extract_modis_jaen.py          # Extracción satelital MODIS MOD13Q1 de Planetary Computer
│   ├── extract_satellite_series.py    # Extracción Sentinel-2 con máscara de calidad
│   ├── build_cafe_real.py             # Fusión determinista fenológica a data/caso_2/
│   ├── eval_hipotesis_cafe.py         # Evaluación de H1-H4 y validación expansiva M0-M4
│   ├── train_cafe_models.py           # Modelado predictivo de rendimiento
│   ├── test_cdse.py                   # Verificación de credenciales Copernicus CDSE
│   ├── test_pbi.py                    # Inspección de tablero PowerBI MIDAGRI
│   ├── visualizar_caso_2.py           # Generación de gráficos y figuras de análisis en images/caso_2/
│   ├── deprecated_build_agro_dataset_SINTETICO.py # Script histórico sintético aislado
│   └── README.md                      # Pipeline y ejecución del Caso 2
├── build_deck.py             # Generador del deck HTML interactivo autocontenido (presentacion.html)
├── deck_branding.py          # Assets, logos oficiales e insignias de ponente
├── deck_notes.py             # Notas del orador y guion cronometrado para cada slide
├── deck_slides_p1.py         # Diapositivas 1 a 12 (Sección 1 y 2: Teoría, Modelos y Satélites)
├── deck_slides_p2.py         # Diapositivas 13 a 23 (Sección 3 a 5: Casos Reales y Decisión)
├── deck_styles.py            # Estilos CSS responsive, paleta semántica y modo claro/oscuro
├── generate_notebooks.py     # Generador automatizado de los notebooks Jupyter en notebooks/
├── test_loader.py            # Prueba rápida de carga y sanitización de datos de ambos casos
├── audit_layout.py           # Auditoría visual Playwright contra espacios vacíos
├── take_screenshots.py       # Captura de pantalla de diapositivas seleccionadas
└── verify_presentation.py    # Verificación en navegador con consola de errores
```

## Ejecución Rápida
* Reconstruir la presentación interactiva:
  ```bash
  python scripts/build_deck.py
  ```
* Ejecutar análisis y figuras del Caso 1:
  ```bash
  python scripts/caso_1/visualizar_caso_1.py
  ```
* Ejecutar análisis y figuras del Caso 2:
  ```bash
  python scripts/caso_2/visualizar_caso_2.py
  ```
* Probar carga de datos:
  ```bash
  python scripts/test_loader.py
  ```
