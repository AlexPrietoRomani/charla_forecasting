# Repositorio de Imágenes y Assets Visuales (`docs/images/`)

Todas las imágenes, figuras de análisis y recursos visuales se centralizan bajo `docs/images/` divididos en tres áreas funcionales:

```text
docs/images/
├── front/                    # Assets del Frontend (Plantilla Oficial y Diapositivas)
│   ├── bg_cover_official.png          # Fondo oficial de portada (Iquitos Data Fest)
│   ├── bg_content_official.png        # Fondo oficial de contenido de diapositiva
│   ├── bg_closing_official.png        # Fondo oficial de cierre / agradecimiento
│   ├── profile_alex.jpg               # Fotografía de perfil del ponente
│   ├── qr_alex_website.png            # Código QR hacia la web personal de Alex Prieto
│   ├── qr_charla_forecasting.svg      # Código QR del repositorio
│   └── logos/                         # Tiras institucionales y badges
│       ├── official_logos_strip.png   # Tira superior (UNAP + Neokernel)
│       └── data_wizard_badge.png      # Insignia de ponente Data Wizard
├── caso_1/                   # Figuras de Análisis del Caso 1 (Clima SENAMHI Iquitos)
│   ├── serie_punchana.png             # Serie térmica histórica y barras de precipitación
│   ├── benchmark_modelos.png          # Comparativa de RMSE y prueba Diebold-Mariano
│   └── forecast_7d_cono.png           # Cono de duda P10-P90 vs temperatura real
├── caso_2/                   # Figuras de Análisis del Caso 2 (Café Jaén MIDAGRI)
│   ├── rendimiento_historico.png      # Evolución de rendimiento y quiebre roya 2012-2014
│   ├── saturacion_ndvi.png            # Curva de saturación espectral en dosel cerrado
│   └── comparativa_modelos_cafe.png   # Error MAE/RMSE de validación temporal expansiva
└── README.md                 # Este documento
```

## Generación
Para regenerar las figuras de análisis y verificar los assets del front:
```bash
python scripts/pagina/generar_imagenes_deck.py
```
