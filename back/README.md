# Backend y Compilador del Deck (`back/`)

Este directorio contiene la lógica de backend encargada de cargar los datos reales, sanitizar valores nulos, fusionar el payload con los módulos de `front/` y compilar el archivo autónomo `presentacion.html`:

## Módulos
1. **`build_deck.py`**:
   * Compilador principal del deck interactivo.
   * Carga los conjuntos de datos de `data/caso_1/` y `data/caso_2/`.
   * Sanitiza `NaN` e inyecta la carga útil JSON en el script global de la presentación.
   * Ensambla el CSS, las diapositivas y las notas de `front/`.
   * Genera el archivo autónomo raíz `presentacion.html`.
2. **`test_loader.py`**:
   * Validador unitario rápido para verificar la integridad de los 8 payloads de datos antes de la compilación.

## Ejecución
```bash
python back/build_deck.py
```
*(Nota: `python scripts/build_deck.py` también funciona como proxy directo).*
