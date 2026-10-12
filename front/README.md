# Frontend del Deck Interactivo (`front/`)

Este directorio contiene todo el código visual, estilístico y estructural de la interfaz de usuario de la presentación interactiva (`presentacion.html`), equivalente al front de la aplicación:

## Componentes y Módulos
1. **`deck_styles.py`**:
   * Hojas de estilo CSS completas.
   * Paleta semántica, variables CSS (`--bg-primary`, `--accent-coral`, etc.), soporte de tema claro/oscuro y layout split-screen 40/60 sin márgenes muertos ("Zero-White-Space").
2. **`deck_slides_p1.py`**:
   * Diapositivas 1 a 12 (Parte 1).
   * Comprende la portada oficial, la pregunta conductora, teoría de series temporales, las 4 familias de modelos y la física de satélites/NDVI.
3. **`deck_slides_p2.py`**:
   * Diapositivas 13 a 23 (Parte 2).
   * Comprende los casos de estudio aplicados (Caso 1 SENAMHI Iquitos y Caso 2 Café Jaén), demos interactivas en vivo con Chart.js, árbol de decisión y cierre con perfil del ponente.
4. **`deck_notes.py`**:
   * Speaker notes drawer (activado con la tecla `N`).
   * Contiene el guion cronometrado, pautas de oratoria e insights para cada una de las 23 diapositivas.
5. **`deck_branding.py`**:
   * Codificador Base64 para logos institucionales, fondos oficiales, QR interactivo y credenciales del expositor ubicadas en `docs/images/front/`.
6. **`assets/chart.umd.min.js`**:
   * Bundle local de Chart.js para funcionamiento 100% offline sin dependencias de internet.
