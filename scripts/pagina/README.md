# Scripts de la Página y Presentación (`scripts/pagina/`)

Este directorio contiene las herramientas de auditoría visual, generación de imágenes de análisis, capturas automatizadas y soporte técnico del deck:

## Scripts Disponibles
1. **`generar_imagenes_deck.py`**:
   * Orquesta la generación completa de las imágenes de alta resolución (300 DPI) para Caso 1 (`docs/images/caso_1/`) y Caso 2 (`docs/images/caso_2/`), y audita los assets de `docs/images/front/`.
2. **`audit_layout.py`**:
   * Auditoría visual de espacios vacíos mediante Playwright (inspecciona desbordes y paddings).
3. **`take_screenshots.py`**:
   * Captura en lote de diapositivas seleccionadas para reportes o difusión.
4. **`verify_presentation.py`**:
   * Navegación automatizada en Chromium/Edge para capturar advertencias y errores de consola JavaScript.
5. **`inspect_slides.py`**:
   * Inspección sintáctica de títulos, clases e índices de diapositivas en los módulos de `front/`.
6. **`generate_notebooks.py`**:
   * Generador automatizado de los notebooks Jupyter en `notebooks/` (`01_clima_senamhi.ipynb` y `02_cafe_ndvi.ipynb`).
