# Plan de Implementación: Animaciones Avanzadas de Alta Fidelidad y Casos de Uso Sectoriales Trazables

**Fecha:** 2026-10-01  
**Especificación:** `docs/superpowers/specs/2026-10-01-animaciones-avanzadas-casos-sectoriales-design.md`  
**Archivos Afectados:**
- `scripts/build_deck.py` (Generador del mazo HTML)
- `presentacion.html` (Salida autocontenida de 25 diapositivas)
- `scripts/take_screenshots.py` (Validador visual automatizado con Microsoft Edge headless)

---

## Tareas de Implementación

### Tarea 1: Ampliación de Estilos CSS y `@keyframes` para Nuevas Dinámicas
- **Archivo:** `scripts/build_deck.py` (sección `<style>`)
- **Descripción:** Definir nuevas animaciones continuas para:
  - `anim-logistic-tangent` (pulsación de la tangente de velocidad máxima $\frac{rk}{4}$ en el punto de inflexión).
  - `anim-hw-decay` (barras de ponderación decreciente exponencial para lags 1 a 14).
  - `anim-stl-multi-scan` (barrido vertical sincronizado a través de las 4 capas $Y_t, T_t, S_t, R_t$).
  - `anim-matrix-drop` (caída de valores temporales a las columnas de la tabla supervisada).
  - `anim-tree-out-of-bounds` (punto de datos saliendo de la caja de entrenamiento y fijándose en la meseta).
  - `anim-lstm-cell-belt` (cinta transportadora del estado de celda $C_{t-1} \to C_t$).
  - `anim-patch-token` & `anim-attention-matrix` (segmentación en parches y mapa de calor de atención cruzada).
  - `anim-hud-pulse` (retícula y telemetría de dron de precisión).
  - `anim-red-edge-scan` (acantilado del Red Edge y línea de saturación $\text{LAI}>3$).
  - `anim-drought-alert` (evento de sequía en floración disparando aborto floral).
  - `anim-4dvar-pulse` & `anim-jetstream` (asimilación satelital y corriente en chorro en 250 hPa).
  - `anim-timesfm-stream` (tokenización de parches continuos de series de tiempo).
  - `anim-sector-pulse` (rutas luminosas guiando por sector en el árbol de decisión).
- **Verificación:** Ejecutar `python scripts/build_deck.py` y comprobar que no hay errores de sintaxis CSS.

### Tarea 2: Rediseño Slide 4 (Curvas Paramétricas & Holt-Winters)
- **Archivo:** `scripts/build_deck.py` (Slide 4)
- **Mecanismos Visuales:**
  - Panel izquierdo: Curva logística completa con asíntota $L=100\%$, punto de inflexión $t_0$ ($L/2$), recta tangente de pendiente máxima y trazador con coordenadas dinámicas $(t, y_t)$, junto a la curva roja desbocada $e^{rt}$.
  - Panel derecho: Gráfico de barras de ponderación decreciente de Holt-Winters ($w_1 = 0.30$ hasta $w_{14} \approx 0.002$).
  - Caja explicativa: Caso real del brote de Dengue en Loreto (INS/MINSA) y reposición retail de 50k SKUs; citas a Verhulst (1838) e Hyndman (2002).
- **Verificación:** Capturar `screenshots/slide_04.png` y verificar renderizado.

### Tarea 3: Rediseño Slide 5 (Descomposición STL)
- **Archivo:** `scripts/build_deck.py` (Slide 5)
- **Mecanismos Visuales:**
  - 4 subgráficos apilados sincronizados: $Y_t$ (Demanda original), $T_t$ (Tendencia Loess), $S_t$ (Ciclo estacional 24h/7d) y $R_t$ (Residuos estocásticos con outliers en rojo).
  - Cursor de barrido vertical continuo conectando las 4 señales en tiempo real.
  - Caja explicativa: Caso real del COES (Perú) y RTE (Francia) para despacho eléctrico; cita a Cleveland et al. (1990).
- **Verificación:** Capturar `screenshots/slide_05.png` y verificar renderizado.

### Tarea 4: Rediseño Slide 6 (El Puente Tabular)
- **Archivo:** `scripts/build_deck.py` (Slide 6)
- **Mecanismos Visuales:**
  - Flujo horizontal superior de la serie temporal continua.
  - Ventana deslizante que avanza y proyecta las observaciones como columnas ($Lag_1 \dots Lag_{14}$) hacia las filas de una tabla supervisada animada.
  - Caja explicativa: Caso real de Walmart en la M5 Forecasting Competition; cita a Makridakis et al. (2022).
- **Verificación:** Capturar `screenshots/slide_06.png` y verificar renderizado.

### Tarea 5: Rediseño Slide 7 (Patología de los Árboles)
- **Archivo:** `scripts/build_deck.py` (Slide 7)
- **Mecanismos Visuales:**
  - Espacio de partición ortogonal 2D con hiper-rectángulos de decisión $[X_{\min}, X_{\max}]$.
  - Trazador de datos que excede el rango histórico y cae en la última caja, forzando la meseta horizontal plana.
  - Caja explicativa: Caso real de la crisis eléctrica de Texas (ERCOT, febrero 2021, -18 °C en Dallas, 20 GW de subestimación); cita a Grinsztajn et al. (NeurIPS 2022).
- **Verificación:** Capturar `screenshots/slide_07.png` y verificar renderizado.

### Tarea 6: Rediseño Slide 8 (Deep Learning: LSTM vs PatchTST)
- **Archivo:** `scripts/build_deck.py` (Slide 8)
- **Mecanismos Visuales:**
  - Celda LSTM con compuertas de olvido $f_t$, entrada $i_t$, estado de celda $C_t$ y salida $h_t$.
  - PatchTST con segmentación en parches de 16 pasos y matriz de auto-atención multi-cabeza.
  - Caja explicativa: Caso real de CAISO (California) y Enel Green Power para 1,000 turbinas eólicas; citas a Hochreiter & Schmidhuber (1997) y Nie et al. (ICLR 2023).
- **Verificación:** Capturar `screenshots/slide_08.png` y verificar renderizado.

### Tarea 7: Rediseño Slide 10 (Visión por Computador en Agro)
- **Archivo:** `scripts/build_deck.py` (Slide 10)
- **Mecanismos Visuales:**
  - Interfaz de Vuelo Dron HUD completa con retícula, telemetría de altitud/velocidad/GPS Jaén, bounding boxes YOLOv12 con IDs y confianzas de cerezas maduras/verdes/roya, y polígono de segmentación SAM 2.1.
  - Caja explicativa: Caso real de CENFROCAFE (Jaén) y ECOM Agroindustrial para aforo 90 días antes del corte; citas a Kirillov et al. (2024) y Ramos et al. (2020).
- **Verificación:** Capturar `screenshots/slide_10.png` y verificar renderizado.

### Tarea 8: Rediseño Slide 11 (Biofísica Satelital & Saturación NDVI)
- **Archivo:** `scripts/build_deck.py` (Slide 11)
- **Mecanismos Visuales:**
  - Corte histológico de hoja de café (cutícula, empalizada con cloroplastos absorbiendo 665 nm Rojo al 95%, mesófilo esponjoso reflejando 842 nm NIR al 85%).
  - Curva espectral continua 400-2500 nm con escalón Red Edge (705 nm) y comparación de saturación NDVI ($\text{LAI}>3$) frente a linealidad de EVI y NDRE.
  - Caja explicativa: Caso real de Copersucar / Raízen (caña en Brasil) y AgroVisión (café y arándanos en Perú); citas a Gates et al. (1965) y Huete et al. (2002).
- **Verificación:** Capturar `screenshots/slide_11.png` y verificar renderizado.

### Tarea 9: Rediseño Slide 12 (Fusión Multimodal Fenológica)
- **Archivo:** `scripts/build_deck.py` (Slide 12)
- **Mecanismos Visuales:**
  - Diagrama tri-modular sincronizado con 3 ventanas fenológicas (Floración, Llenado, Cosecha), curva de lluvia CHIRPS y serie Sentinel-2 EVI.
  - Alerta animada de sequía en floración que dispara el aborto floral irreversible y reduce la proyección a 18.2 qq/ha.
  - Caja explicativa: Caso real de la Campaña 2024 en Jaén (Cajamarca); citas a Ramos et al. (2020) y Barbosa et al. (2021).
- **Verificación:** Capturar `screenshots/slide_12.png` y verificar renderizado.

### Tarea 10: Rediseño Slide 13 (Modelos Físicos Globales & 4D-Var)
- **Archivo:** `scripts/build_deck.py` (Slide 13)
- **Mecanismos Visuales:**
  - Malla columnar 3D de la atmósfera con niveles isobáricos (1000 hPa a 250 hPa), corrientes en chorro, advección, Coriolis y plumas convectivas.
  - Ciclo animado de asimilación 4D-Var inyectando datos de satélites en órbita polar cada 6 horas.
  - Caja explicativa: Caso real de Maersk y Air France para optimización de rutas transoceánicas; cita a Bauer et al. (Nature 2015).
- **Verificación:** Capturar `screenshots/slide_13.png` y verificar renderizado.

### Tarea 11: Rediseño Slide 15 (GraphCast DeepMind & Zero-Shot)
- **Archivo:** `scripts/build_deck.py` (Slide 15)
- **Mecanismos Visuales:**
  - Esfera terrestre con malla icosaédrica multi-resolución de DeepMind ($M_0$ a $M_6$) con pulsos de red neuronal de grafos (GNN).
  - Stream de tokenización de parches de TimesFM (Google) y Chronos (Amazon T5) pronosticando en frío.
  - Caja explicativa: Caso real de alerta temprana del Huracán Otis (2023) y Google Flood Hub en 80 países; citas a Lam et al. (Science 2023) y Das et al. (2024).
- **Verificación:** Capturar `screenshots/slide_15.png` y verificar renderizado.

### Tarea 12: Rediseño Slide 23 (Árbol de Decisión Práctico por Sector)
- **Archivo:** `scripts/build_deck.py` (Slide 23)
- **Mecanismos Visuales:**
  - Flujograma de decisión estructurado con 4 sectores prioritarios: Energía/Utilities (CAISO/COES), Retail/Supply Chain (Walmart M5), Agroexportación (AgroVisión) y Salud Pública/Epidemias (INS/MINSA).
  - Trazadores animados guiando al usuario por las 4 vías según volumen de datos, latencia y regulación.
  - Caja explicativa: Criterio para líderes técnicos y tomadores de decisiones; citas a Makridakis et al. (M4/M5) y Lim et al. (2021).
- **Verificación:** Capturar `screenshots/slide_23.png` y verificar renderizado.

### Tarea 13: Verificación Global, Compilación y Commit Semántico
- **Acciones:**
  1. Ejecutar `python scripts/build_deck.py`.
  2. Ejecutar validador de sintaxis HTML (0 etiquetas sin cerrar).
  3. Ejecutar `python scripts/take_screenshots.py` para regenerar capturas de todas las diapositivas mejoradas.
  4. Revisar visualmente las capturas con `view_file`.
  5. Realizar commit semántico con detalle de cambios.
