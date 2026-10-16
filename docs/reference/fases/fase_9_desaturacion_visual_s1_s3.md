# Fase 9: Desaturación Cognitiva y Rediseño Pedagógico-Visual de Secciones 1 y 3

> **Documento de Fase:** `docs/task/fases/fase_9_desaturacion_visual_s1_s3.md`  
> **Archivos objetivo (Sección 1):** `docs/notebooklm/seccion_1/prototipos/{5_Anatomia_de_la_senal_temporal_v3,6_Era_1_La_parsimonia_lineal_v3,7_Era_2_El_puente_tabular,8_Era_3_Deep_Learning_y_Parches,9_Era_4_Modelos_Fundacionales_Zero_Shot,10_El_Cono_de_Incertidumbre_y_Prediccion_Conforme,11_Arquitectura_de_Decision_y_Cierre_Ejecutivo}.html`  
> **Archivos objetivo (Sección 3):** `docs/notebooklm/seccion_3/prototipos/{19_c_mo_el_agro_invent_el_forecasting,20_del_almanaque_al_sat_lite,21_f_sica_biol_gica_y_el_l_mite_algor_tmico,22_reloj_fenol_gico_del_caf,23_precisi_n_actual_y_las_tres_trampas}.html`  
> **Archivos de compilación y notas:** `front/deck_notes.py`, `back/build_deck.py`, `presentacion.html`, `index.html`  
> **Estado:** `[X] Completada` (16 de octubre de 2026)

---

## 1. Diagnóstico Forense (Auditoría Visual @1366×768 y @1920×1080)

| # | Problema Detectado | Diapositivas Afectadas | Causa Raíz en el Código Actual |
|---|---|---|---|
| **D1** | **Pared de texto y barra de scroll vertical en la columna izquierda** (`.narrative-card` / `.left-column`). | **05, 06, 07, 08, 09, 10, 19, 20, 21, 22, 23** (crítico con scrollbar visible en **05** y **23**) | Se apilan 5 bloques: párrafo `lead` de 4 líneas + 2 o 3 cajas `.narr-block` extensas + caja extra `#metaphorCard` (en Diapo 05) + `.formula-bar` + `.speaker-box` ("Guía de Exposición" de 4 líneas). |
| **D2** | **Teleprompter público redundante (`.speaker-box`)**: el público lee lo mismo que el ponente va a decir. | **05 a 10** y **19 a 23** | La caja `"🎙️ GUÍA DE EXPOSICIÓN (QUÉ DECIR)"` ocupa ~22% de la altura útil izquierda, duplicando la función del drawer `[N] Notas` (`front/deck_notes.py`). |
| **D3** | **Doble subtitulado redundante dentro del lienzo derecho (`.sim-card`)**: cajas `"Arriba: ... / Abajo: ..."` o `"Izquierda: ... / Derecha: ..."`. | **07, 08, 09, 10, 19, 20, 21, 22, 23** | Los contenedores `.canvas-split-hint` restan entre `38px` y `52px` de altura útil al gráfico Canvas/SVG, comprimiendo las visualizaciones. |
| **D4** | **Vacío negro central en las 4 columnas del Árbol de Decisión** y falta de indicadores visuales comparativos. | **11** | `.lane-body` usa `justify-content: space-between`, separando artificialmente los chips superiores de las tarjetas inferiores y dejando un hueco vacío de ~130px sin gráficos comparativos. |
| **D5** | **Recorte vertical del cuadro de detalle inferior** en los 5 escalones tecnológicos. | **20** | El contenedor inferior `#stepDetailBox` (`"ESCALÓN 5 DE 5: MODELOS ACOPLADOS"`) desborda su altura y corta por la mitad la segunda línea (`"Reto: 500 variables (p)..."`). |
| **D6** | **Texto superpuesto sobre los dientes del engranaje central** (`Retraso (τ) 6-8 meses`). | **21** | El rótulo del engranaje se dibuja en el centro exacto del icono dentado sin placa de fondo sólida, dificultando su lectura, y el gráfico derecho carece de zonas coloreadas de umbral. |
| **D7** | **Etiquetas cortadas (`"Florac..."`, `"Cosecha"`) dentro del reloj fenológico** y panel derecho saturado de prosa. | **22** | El radio de la rueda es pequeño y los textos se dibujan dentro del anillo interior estrecho; a la derecha se anidan 3 cajas con párrafos largos que repiten la columna izquierda. |
| **D8** | **Solapamiento del botón `"Ir al Caso Jaén →"` sobre el texto de `"🔥 LA PRUEBA DE FUEGO"`**. | **23** | El botón está posicionado de forma absoluta o flotante dentro del banner inferior derecho, pisando la frase `"La teoría es hermosa, pero mañana la mediremos en Jaén"`. |

---

## [X] Fase 9 — Desaturación Cognitiva y Rediseño Pedagógico-Visual de Secciones 1 y 3

- **Objetivo:** Eliminar la saturación textual, las barras de scroll verticales y los solapamientos gráficos en los 12 prototipos interactivos de las Secciones 1 (Diapos 5–11) y 3 (Diapos 19–23), reemplazando párrafos largos por síntesis ejecutiva escaneable y enriqueciendo los lienzos con diagramas, cotas y medidores visuales auto-explicativos (*"Show, Don't Tell"*).
- **Entregable global:** Los 12 prototipos HTML en `docs/notebooklm/seccion_1/prototipos/` y `docs/notebooklm/seccion_3/prototipos/` refactorizados, `front/deck_notes.py` sincronizado, `scripts/audit_f9_desaturacion.py` en verde y bundles `presentacion.html` e `index.html` compilados y verificados en 1366×768 y 1920×1080.
- **AC global de la Fase:**
  - [X] Cero cajas `.speaker-box` de múltiples líneas en pantalla; sustituidas por `.executive-takeaway` de 1 línea ($\le 15$ palabras).
  - [X] Conteo de palabras en `.narrative-card` / `.left-column` $\le 110$ palabras por etapa (reducción $\ge 40\%$), logrando `scrollHeight <= clientHeight` (cero scrollbars verticales) en 1366×768 y 1920×1080.
  - [X] Cero recortes o solapamientos de texto/botones en las Diapos 11, 20, 21, 22 y 23.
  - [X] Lienzos auto-explicativos con cotas directas (Diapo 5), zonas coloreadas (Diapos 6 y 21), flechas conectoras serie→tabla (Diapo 7), medidores de barra (Diapos 8 y 11) y reloj fenológico ampliado sin truncamientos (Diapo 22).
- **Tests de la Fase:**
  - **Test Unitario:** Script `scripts/audit_f9_desaturacion.py` que verifica estáticamente los 12 archivos HTML (conteo de palabras por etapa, ausencia de `"GUÍA DE EXPOSICIÓN"` en el DOM visible y compilación limpia de `back/build_deck.py`).
  - **Test de Simulación de Usuario:** Recorrido automatizado en Chromium headless a `1366×768` y `1920×1080` sobre las Diapos 5–11 y 19–23 validando ausencia de scrollbars (`scrollHeight <= clientHeight`), cero errores de consola y generación de capturas de auditoría en `screenshots/f9_*.png`.

---

### [X] SF9.1 — Desaturación Textual, Reemplazo del Teleprompter en Pantalla y Cero Scrollbars (Secciones 1 y 3)

- **Objetivo:** Reducir en un 45% la densidad de palabras de la columna izquierda en los prototipos de las Diapos 5–10 y 19–23, reemplazar el bloque `"🎙️ GUÍA DE EXPOSICIÓN"` por una píldora ejecutiva de 1 línea (`💡 Idea Clave`) y eliminar el 100% de las barras de scroll verticales.
- **Entregable:** Los 11 prototipos con columna narrativa (`5` a `10` y `19` a `23`) desaturados y `front/deck_notes.py` con los guiones completos.
- **AC de la Sub fase:**
  - [X] Ningún prototipo supera las 110 palabras en la columna izquierda en ninguna de sus 4 etapas.
  - [X] Desaparecen por completo las barras de scroll verticales en `1366×768` (especialmente en Diapos 5 y 23).
- **Tests de la Sub fase:**
  - **Test Unitario:** Chequeo automatizado de longitud de `lead` ($\le 22$ palabras), `blocks` ($\le 18$ palabras por bloque) y `takeaway` ($\le 15$ palabras) en cada archivo HTML.
  - **Test de Simulación de Usuario:** Renderizado en Chromium headless a `1366×768` comprobando que `el.scrollHeight <= el.clientHeight + 2` en todas las tarjetas `.narrative-card` y `.left-column`.

#### [X] T9.1.1 — Reemplazo de `.speaker-box` ("Guía de Exposición") por Píldora Ejecutiva de 1 Línea (`💡 Idea Clave`) y Traslado a `front/deck_notes.py`
- **Objetivo de la Tarea:** Eliminar el bloque de teleprompter de 4 líneas en los 11 prototipos (`5`–`10` y `19`–`23`), sustituirlo por un `.executive-takeaway` compacto de 1 sola línea y verificar que el texto hablado completo esté disponible en `front/deck_notes.py` (tecla `N`).
- **Entregable:** Regla CSS `.executive-takeaway`, marcado HTML y propiedad `quote`/`takeaway` actualizados en los 11 prototipos + `front/deck_notes.py`.

> **🧠 Explicación:** Mostrar un párrafo de 4 líneas titulado *"🎙️ GUÍA DE EXPOSICIÓN (QUÉ DECIR)"* en la diapositiva proyectada genera **interferencia cognitiva (efecto redundancia de Mayer)**: la audiencia intenta leer el párrafo entrecomillado al mismo tiempo que escucha al ponente decir exactamente lo mismo, saturando el canal verbal. Al mover ese guion conversacional exclusivamente al drawer del orador (`[N] Notas` en `front/deck_notes.py`) y dejar en pantalla solo una **píldora ejecutiva de 1 línea (`💡 Idea Clave`)**, liberamos entre `65px` y `90px` de altura vertical en la columna izquierda y destacamos el mensaje gerencial sin ruido.

> **💡 Cómo hacerlo (ejemplo):**
> ```css
> /* Reemplazar el estilo de .speaker-box por un callout ejecutivo compacto de 1 línea */
> .speaker-box, .executive-takeaway {
>   display: flex;
>   align-items: center;
>   gap: 8px;
>   padding: 7px 11px;
>   border-radius: 8px;
>   border: 1px solid rgba(56, 239, 255, 0.28);
>   background: linear-gradient(135deg, rgba(14, 116, 144, 0.22), rgba(7, 13, 28, 0.9));
>   font: 600 clamp(10.5px, 0.78vw, 12px)/1.3 var(--sans);
>   color: #edf5ff;
>   margin-top: auto;
>   flex-shrink: 0;
> }
> .executive-takeaway strong { color: var(--ockham); white-space: nowrap; }
> ```
> ```html
> <!-- En el HTML de cada prototipo (5..10 y 19..23): reemplazar el bloque .speaker-box por: -->
> <div class="executive-takeaway" id="speakerQuote">
>   <strong>💡 Idea Clave:</strong> <span>Aísla tendencia y estacionalidad; jamás entrenes sobre el ruido.</span>
> </div>
> ```

- **AC de la Tarea:**
  - [X] Ninguno de los 11 prototipos contiene el texto `"GUÍA DE EXPOSICIÓN (QUÉ DECIR)"` ni `"CITA DE CONFERENCIA"` en la vista pública.
  - [X] El elemento `#speakerQuote` ocupa 1 sola línea (o máximo 2 en pantallas muy estrechas) con $\le 15$ palabras.
  - [X] `front/deck_notes.py` conserva las notas conversacionales completas para las Diapos 5–11 y 19–23.
- **Tests de la Tarea:**
  - **Test Unitario:** `grep -c "GUÍA DE EXPOSICIÓN" docs/notebooklm/seccion_{1,3}/prototipos/*.html` retorna `0` en todos los archivos activos.
  - **Test de Simulación de Usuario:** Cargar `presentacion.html#6` y `presentacion.html#19` en Chromium headless, verificar que la píldora inferior se renderiza en $< 38\text{px}$ de alto y que al pulsar `N` se abre el drawer con el guion completo.

##### [X] A9.1.1.1 — Actualizar `front/deck_notes.py` asegurando que contenga los guiones por etapa de las Diapos 5–11 y 19–23
- **Objetivo:** Garantizar que ninguna frase pedagógica del orador se pierda al compactar la vista pública.
- **Input:** Textos actuales de `quote` en los 11 prototipos y `front/deck_notes.py`.
- **Output:** `front/deck_notes.py` enriquecido con las citas completas por etapa.
- **Proceso:**
  1. Revisar las entradas `"5"` a `"11"` y `"19"` a `"23"` en `front/deck_notes.py`.
  2. Asegurar que cada entrada incluya la guía hablada completa de las 4 etapas.
- **Tests:**
  - **Test Unitario:** `.venv/bin/python -c "from front.deck_notes import get_speaker_notes; n=get_speaker_notes(); assert all(str(k) in n for k in [*range(5,12), *range(19,24)])"`.
  - **Test de Simulación de Usuario:** Abrir el drawer de notas con la tecla `N` en el navegador y comprobar su renderizado.
- **AC:** Las 12 diapositivas tienen notas completas y estructuradas en `front/deck_notes.py`.

##### [X] A9.1.1.2 — Reemplazar `.speaker-box` por `.executive-takeaway` de 1 línea en los 11 prototipos de Secciones 1 y 3
- **Objetivo:** Sustituir el HTML/CSS/JS de `.speaker-box` en los archivos `5`–`10` y `19`–`23`.
- **Input:** Archivos HTML en `docs/notebooklm/seccion_1/prototipos/` y `docs/notebooklm/seccion_3/prototipos/`.
- **Output:** Los 11 archivos HTML con píldora `💡 Idea Clave:` de $\le 15$ palabras por etapa.
- **Proceso:**
  1. Reemplazar el contenedor `.speaker-box` y su cabecera `"🎙️ GUÍA DE EXPOSICIÓN..."` por `<div class="executive-takeaway"><strong>💡 Idea Clave:</strong> <span id="speakerQuote">...</span></div>`.
  2. Actualizar en el objeto `STAGES` de cada prototipo el campo `quote` para que contenga una síntesis ejecutiva de $\le 15$ palabras en lugar de un párrafo de 45 palabras.
- **Tests:**
  - **Test Unitario:** Script en Python que verifica que cada string `quote` en `STAGES` tenga $\le 15$ palabras.
  - **Test de Simulación de Usuario:** Inspección de altura en DOM (`offsetHeight <= 42`) en `1366×768`.
- **AC:** Píldora ejecutiva visible, limpia y de 1 línea en las 4 etapas de los 11 prototipos.

#### [X] T9.1.2 — Síntesis Escaneable de `.narrative-card` (Reducción del 45% de Palabras y Eliminación de `#metaphorCard` Redundante en Diapo 5)
- **Objetivo de la Tarea:** Reescribir los textos de `lead` y `blocks` en todas las etapas (`STAGES`) de los prototipos `5`–`10` y `19`–`23` usando formato telegráfico escaneable (`Icono + Concepto Clave: Causa → Efecto`) y eliminar el recuadro redundante `#metaphorCard` en la Etapa 1 de la Diapo 5.
- **Entregable:** Objetos `STAGES` y marcado inicial depurados en los 11 prototipos, con cero barras de scroll verticales en `1366×768`.

> **🧠 Explicación:** En una presentación ejecutiva o magistral, una tarjeta lateral no es un capítulo de libro: el espectador debe escanearla en **menos de 4 segundos** para volver su vista al gráfico interactivo. En la Diapo 5 (`audit_s5_1366.png`), debajo de las 5 tarjetas interactivas de capas (`Y(t)`, `T(t)`, `S(t)`, `C(t)`, `ε(t)`) existe un recuadro adicional (`#metaphorCard`: *"🌊 CAUCE, MAREAS, SEQUÍAS Y TURBULENCIA"*) que repite literalmente las mismas 4 definiciones, forzando la aparición de una barra de scroll vertical. Eliminando ese bloque duplicado en la Etapa 1 y acortando cada `.narr-block` a **máximo 2 líneas ($\le 18$ palabras)** en todas las diapositivas, el texto respira, podemos subir la fuente base a `clamp(11.5px, 0.85vw, 13px)` y desaparecen todas las barras de scroll.

> **💡 Cómo hacerlo (ejemplo):**
> ```javascript
> // Antes (Saturado - 52 palabras en un solo bloque):
> // { title: "🌱 ¿POR QUÉ NACIÓ EN 1838?", body: "Los polinomios ingenuos proyectaban un crecimiento eterno. Pierre François Verhulst formuló la curva logística en S: crece rápido al inicio, alcanza su velocidad pico en t₀ y se frena al saturar la capacidad máxima L." }
>
> // Después (Escaneable Gerencial - 16 palabras, lectura en 2 segundos):
> {
>   title: "🌱 FRONTERA BIOLÓGICA (VERHULST, 1838)",
>   body: "Reemplaza la explosión infinita por una <strong>curva en S</strong> que frena al chocar con el <strong>techo físico L</strong>."
> }
> ```
> ```javascript
> // En docs/notebooklm/seccion_1/prototipos/5_Anatomia_de_la_senal_temporal_v3.html:
> // En Etapa 1 (act === 1), ocultar #metaphorCard porque #layerStack ya muestra las 5 capas interactivas:
> metaphorCard.hidden = (act === 1); // Solo se usa como tarjeta de apoyo compacta en etapas 2-4
> ```

- **AC de la Tarea:**
  - [X] En la Diapo 5 (Etapa 1), `#metaphorCard` no se duplica debajo de `#layerStack`, eliminando el scroll vertical.
  - [X] En los 11 prototipos (`5`–`10` y `19`–`23`), cada `lead` tiene $\le 22$ palabras y cada `block.body` tiene $\le 18$ palabras.
  - [X] En resolución `1366×768`, ninguna `.narrative-card` ni `.left-column` muestra barra de scroll (`scrollHeight <= clientHeight`).
- **Tests de la Tarea:**
  - **Test Unitario:** Script Python que extrae los bloques de texto de cada prototipo y verifica el umbral máximo de palabras ($\le 110$ palabras totales por etapa en la columna izquierda).
  - **Test de Simulación de Usuario:** Capturas en Chromium headless a `1366×768` de las Diapos 5 a 10 y 19 a 23 comprobando visualmente y por evaluación JS (`el.scrollHeight <= el.clientHeight`) que no hay scrollbars.

##### [X] A9.1.2.1 — Eliminar redundancia de `#metaphorCard` en Etapa 1 de Diapo 05 y compactar sus etapas 2, 3 y 4
- **Objetivo:** Suprimir el bloque repetido bajo las 5 capas en la Diapo 5 y sintetizar los textos de las etapas 2 (STL), 3 (Señal vs Ruido) y 4 (Overfitting).
- **Input:** `docs/notebooklm/seccion_1/prototipos/5_Anatomia_de_la_senal_temporal_v3.html`.
- **Output:** Archivo actualizado sin barra de scroll vertical en ninguna de sus 4 etapas.
- **Proceso:**
  1. Configurar `#metaphorCard` con `hidden` durante la Etapa 1 (donde ya están las 5 tarjetas de `#layerStack`).
  2. En las etapas 2, 3 y 4, limitar `#metaphorCard` a 2 viñetas escaneables de 1 línea cada una.
- **Tests:**
  - **Test Unitario:** Verificar en el código de Diapo 5 que `metaphorCard` se oculta en `act === 1`.
  - **Test de Simulación de Usuario:** Abrir Diapo 5 a `1366×768` y comprobar `leftColumn.scrollHeight <= leftColumn.clientHeight`.
- **AC:** Cero scroll vertical en la Diapo 5 a `1366×768` y `1920×1080`.

##### [X] A9.1.2.2 — Sintetizar textos de `STAGES` en los prototipos 06, 07, 08, 09 y 10 (Sección 1)
- **Objetivo:** Reducir en ~45% las palabras de `lead` y `blocks` en las Diapos 6 a 10 manteniendo intacto el rigor técnico.
- **Input:** Prototipos `6`, `7`, `8`, `9` y `10` en `docs/notebooklm/seccion_1/prototipos/`.
- **Output:** Los 5 archivos con textos ejecutivos de máximo 2 líneas por tarjeta y tipografía de cuerpo `clamp(11.5px, 0.85vw, 13px)`.
- **Proceso:**
  1. Reescribir `lead` ($\le 22$ palabras) y cada `block.body` ($\le 18$ palabras) en las 4 etapas de cada archivo.
  2. Ajustar el `padding` y `gap` de `.narrative-card` para que las tarjetas queden equilibradas sin apretarse ni desbordar.
- **Tests:**
  - **Test Unitario:** Conteo de palabras por etapa $\le 110$ en los archivos 6 a 10.
  - **Test de Simulación de Usuario:** Verificación en Chromium headless a `1366×768` en las 4 etapas de cada diapositiva.
- **AC:** Diapos 6 a 10 escaneables en $< 4$ segundos por etapa y sin barras de scroll.

##### [X] A9.1.2.3 — Sintetizar textos de `STAGES` en los prototipos 19, 20, 21, 22 y 23 (Sección 3)
- **Objetivo:** Reducir en ~45% las palabras de `lead` y `blocks` en las Diapos 19 a 23 eliminando la barra de scroll vertical de la Diapo 23.
- **Input:** Prototipos `19`, `20`, `21`, `22` y `23` en `docs/notebooklm/seccion_3/prototipos/`.
- **Output:** Los 5 archivos con tarjetas narrativas concisas y cero scroll vertical.
- **Proceso:**
  1. Sintetizar `lead` ($\le 22$ palabras) y `blocks` ($\le 18$ palabras por bloque) en las 4 etapas de los 5 prototipos de la Sección 3.
  2. Verificar especialmente en `23_precisi_n_actual_y_las_tres_trampas.html` que la columna izquierda encaje con holgura sin activar scrollbar.
- **Tests:**
  - **Test Unitario:** Conteo de palabras por etapa $\le 110$ en los archivos 19 a 23.
  - **Test de Simulación de Usuario:** Captura de Diapos 19 a 23 a `1366×768` confirmando `scrollHeight <= clientHeight`.
- **AC:** Cero barras de scroll en toda la Sección 3 y lectura inmediata.

---

### [X] SF9.2 — Rediseño Pedagógico-Visual ("Show, Don't Tell") de la Sección 1 (Diapositivas 5 a 11)

- **Objetivo:** Hacer que los lienzos gráficos de la Sección 1 (Diapos 5 a 11) se expliquen por sí mismos mediante cotas visuales, zonas sombreadas, conectores animados y medidores de barra, eliminando los banners de instrucciones redundantes (`"Arriba: ... / Abajo: ..."`) y el vacío negro de la Diapo 11.
- **Entregable:** Prototipos `5` a `11` en `docs/notebooklm/seccion_1/prototipos/` con visualizaciones enriquecidas.
- **AC de la Sub fase:**
  - [X] Eliminados los banners redundantes `.canvas-split-hint` en las Diapos 6, 7, 8, 9 y 10, ganando $+42\text{px}$ de alto para los gráficos.
  - [X] Incorporadas anotaciones visuales pedagógicas directas en los lienzos de las Diapos 5, 6, 7, 8, 9, 10 y 11.
- **Tests de la Sub fase:**
  - **Test Unitario:** Verificación de presencia de los nuevos elementos visuales/funciones de dibujo en los 7 archivos HTML de la Sección 1.
  - **Test de Simulación de Usuario:** Capturas en Chromium headless a `1366×768` y `1920×1080` de las Diapos 5 a 11 validando claridad visual y ausencia de solapes.

#### [X] T9.2.1 — Diapo 05 (`5_Anatomia_de_la_senal_temporal_v3.html`): Barras de Peso en Tarjetas de Capas y Cotas Visuales Directas en el Monitor 2D
- **Objetivo de la Tarea:** Incorporar en cada una de las 5 tarjetas de `#layerStack` una mini-barra visual de energía/peso relativo y dibujar sobre el monitor 2D (`#wave2d`) cotas explicativas directas (vector de pendiente $T(t)$, corchete de periodo $\lambda$ para $S(t)$ y banda de dispersión $\pm\varepsilon(t)$).
- **Entregable:** `docs/notebooklm/seccion_1/prototipos/5_Anatomia_de_la_senal_temporal_v3.html` con tarjetas de capas visuales y cotas en el Canvas 2D.

> **🧠 Explicación:** Cuando el público ve una onda compleja en el monitor 2D, necesita identificar visualmente *qué rasgo geométrico* corresponde a cada letra de la ecuación $Y(t) = T(t) + S(t) + C(t) + \varepsilon(t)$. Al dibujar sobre el propio Canvas una **línea guía punteada con etiqueta `Pendiente T(t)`**, un **corchete horizontal `[← Periodo S(t) →]`** entre dos crestas y una **envoltura translúcida `±Ruido ε(t)`**, el gráfico enseña visualmente la anatomía de la señal sin necesidad de leer definiciones largas.

> **💡 Cómo hacerlo (ejemplo):**
> ```javascript
> // En drawWave2D() de 5_Anatomia_de_la_senal_temporal_v3.html:
> // 1. Si T(t) está activo, dibujar flecha de tendencia estructural:
> if (state.layers.T) {
>   ctx.save();
>   ctx.strokeStyle = 'rgba(56, 189, 248, 0.75)';
>   ctx.setLineDash([5, 4]);
>   ctx.lineWidth = 1.8;
>   ctx.beginPath();
>   ctx.moveTo(padL + 20, yStartT);
>   ctx.lineTo(w - padR - 20, yEndT);
>   ctx.stroke();
>   ctx.fillStyle = '#38bdf8';
>   ctx.font = '700 10.5px "JetBrains Mono"';
>   ctx.fillText('↗ Pendiente Estructural T(t)', padL + 28, yStartT - 8);
>   ctx.restore();
> }
> // 2. Si S(t) está activo, dibujar corchete de ciclo fijo entre dos picos:
> if (state.layers.S) {
>   drawBracket(ctx, xPeak1, xPeak2, yPeak - 14, '↔ Periodo Fijo S(t)', '#c084fc');
> }
> ```

- **AC de la Tarea:**
  - [X] Las 5 tarjetas de `#layerStack` incluyen un indicador visual de peso/rol (`100% Señal Total`, `Cauce ~45%`, `Marea ~30%`, `Ciclo ~15%`, `Azar ~10%`).
  - [X] El monitor 2D muestra cotas gráficas directas para $T(t)$ y $S(t)$ sin solapar la curva principal.
- **Tests de la Tarea:**
  - **Test Unitario:** Verificar la presencia de las cotas en la función de renderizado 2D de `5_Anatomia_de_la_senal_temporal_v3.html`.
  - **Test de Simulación de Usuario:** Captura de Diapo 5 a `1366×768` comprobando que las cotas del monitor 2D y las 5 tarjetas de capas se ven limpias y proporcionadas.

##### [X] A9.2.1.1 — Agregar mini-barras de peso e iconos pedagógicos en `#layerStack` y cotas en `#wave2d`
- **Objetivo:** Enriquecer visualmente las tarjetas de capas y el monitor 2D de la Diapo 5.
- **Input:** `docs/notebooklm/seccion_1/prototipos/5_Anatomia_de_la_senal_temporal_v3.html`.
- **Output:** Archivo HTML con `#layerStack` mejorado y cotas en Canvas.
- **Proceso:**
  1. Añadir en cada `.layer-btn` un badge de proporción visual y descripción de 1 línea concisa.
  2. Añadir en el renderizador 2D la línea guía de pendiente $T(t)$ y el corchete de periodo $S(t)$.
- **Tests:**
  - **Test Unitario:** Comprobar sintaxis JS y presencia de etiquetas en el Canvas 2D.
  - **Test de Simulación de Usuario:** Renderizar Diapo 5 en Chromium a `1366×768` y revisar captura.
- **AC:** Monitor 2D y tarjetas de capas auto-explicativos y sin desborde.

#### [X] T9.2.2 — Diapos 06 y 07 (`6_Era_1...` y `7_Era_2...`): Zonas Visuales en Curva Logística y Flechas de Mapeo Serie → Tabla Supervisada
- **Objetivo de la Tarea:** Eliminar los banners redundantes sobre el canvas en las Diapos 6 y 7; añadir bandas visuales de las 3 fases de crecimiento en la curva de Verhulst (Diapo 6) y dibujar flechas conectoras directas desde los puntos de la ventana deslizante ($y_{t-1}, y_{t-7}, y_{t+1}$) hacia sus celdas en la tabla supervisada (Diapo 7).
- **Entregable:** `6_Era_1_La_parsimonia_lineal_v3.html` y `7_Era_2_El_puente_tabular.html` actualizados.

> **🧠 Explicación:** En la Diapo 7 (`audit_s7_1366.png`), el espectador ve arriba una serie con una caja naranja (*"Ventana de 7 Lags"*) y abajo una tabla con columnas `Lag 1`, `Lag 7`, `Media Móvil` y `Objetivo`, pero **no hay flechas que conecten qué punto de la curva va a qué columna de la tabla**. Además, arriba del gráfico hay dos botones/banners estáticos (*"Arriba: Ventana deslizándose... / Abajo: Filas creadas..."*) que ocupan espacio sin aportar diseño. Al quitar esos 2 banners y trazar **líneas punteadas con punta de flecha** desde el nodo $y_{t-1}$ hasta la cabecera `Lag 1 (Ayer)` y desde el nodo verde $y_{t+1}$ hasta la cabecera `🎯 Objetivo (Mañana)`, el mecanismo de *feature engineering* tabular se entiende en 2 segundos.

> **💡 Cómo hacerlo (ejemplo):**
> ```javascript
> // En 7_Era_2_El_puente_tabular.html (función de dibujo del Canvas):
> // Trazar conector visual desde el último punto naranja (Lag 1) hasta la columna "Lag 1" de la tabla:
> function drawMappingArrow(ctx, x1, y1, x2, y2, color, label) {
>   ctx.save();
>   ctx.strokeStyle = color;
>   ctx.setLineDash([4, 3]);
>   ctx.lineWidth = 1.6;
>   ctx.beginPath();
>   ctx.moveTo(x1, y1 + 6);
>   ctx.bezierCurveTo(x1, (y1 + y2) / 2, x2, (y1 + y2) / 2, x2, y2 - 6);
>   ctx.stroke();
>   // Punta de flecha en (x2, y2 - 4)
>   ctx.setLineDash([]);
>   ctx.fillStyle = color;
>   ctx.beginPath();
>   ctx.moveTo(x2, y2 - 2);
>   ctx.lineTo(x2 - 4, y2 - 9);
>   ctx.lineTo(x2 + 4, y2 - 9);
>   ctx.closePath();
>   ctx.fill();
>   ctx.restore();
> }
> ```

- **AC de la Tarea:**
  - [X] En Diapo 6 se muestran 3 zonas sutilmente sombreadas en la etapa Verhulst (`1. Despegue`, `2. Inflexión t₀`, `3. Saturación en Techo L`) sin banners redundantes.
  - [X] En Diapo 7 se eliminan los 2 banners `"Arriba: ... / Abajo: ..."` y se dibujan flechas conectoras entre los puntos de la ventana en la serie y las columnas de la tabla supervisada.
- **Tests de la Tarea:**
  - **Test Unitario:** Verificar ausencia de `.canvas-split-hint` en Diapos 6 y 7 y presencia de la función `drawMappingArrow` en Diapo 7.
  - **Test de Simulación de Usuario:** Capturas en Chromium a `1366×768` de Diapos 6 y 7 confirmando que las zonas y flechas se visualizan con total nitidez.

##### [X] A9.2.2.1 — Actualizar Diapo 06 (`6_Era_1_La_parsimonia_lineal_v3.html`) con 3 zonas visuales en Verhulst y limpieza de banners
- **Objetivo:** Hacer auto-explicativa la curva logística y el eco autorregresivo ARIMA en la Diapo 6.
- **Input:** `docs/notebooklm/seccion_1/prototipos/6_Era_1_La_parsimonia_lineal_v3.html`.
- **Output:** Archivo actualizado con zonas visuales etiquetadas sobre el lienzo.
- **Proceso:**
  1. Retirar los banners superiores redundantes dentro del marco del canvas para ganar área gráfica.
  2. Dibujar bandas verticales sutiles y badges para `Fase 1: Aceleración`, `Fase 2: Inflexión (t₀)` y `Fase 3: Freno por Techo L`.
- **Tests:**
  - **Test Unitario:** Verificar sintaxis JS en Diapo 6.
  - **Test de Simulación de Usuario:** Captura a `1366×768` de la Diapo 6.
- **AC:** Curva de Verhulst con fases claramente delimitadas y sin textos amontonados.

##### [X] A9.2.2.2 — Actualizar Diapo 07 (`7_Era_2_El_puente_tabular.html`) con conectores visuales Serie → Tabla y limpieza de banners
- **Objetivo:** Conectar visualmente los rezagos de la serie continua con las columnas de la tabla supervisada.
- **Input:** `docs/notebooklm/seccion_1/prototipos/7_Era_2_El_puente_tabular.html`.
- **Output:** Archivo actualizado sin banners `"Arriba:/Abajo:"` y con flechas conectoras animadas.
- **Proceso:**
  1. Eliminar el contenedor de banners `"Arriba: Ventana deslizándose... / Abajo: Filas creadas..."`.
  2. En el renderizador del Canvas (Etapa 1), dibujar conectores curvos punteados desde $y_{t-1}$ (naranja), $y_{t-7}$ (naranja) y $y_{t+1}$ (verde) hacia la cabecera de la tabla inferior.
- **Tests:**
  - **Test Unitario:** Comprobar que la función de conectores está activa en la Etapa 1 de Diapo 7.
  - **Test de Simulación de Usuario:** Captura a `1366×768` de la Diapo 7 verificando alineación de flechas y tabla.
- **AC:** Transformación Serie 1D $\rightarrow$ Matriz 2D comprensible visualmente al instante.

#### [X] T9.2.3 — Diapos 08, 09 y 10 (`8_Era_3...`, `9_Era_4...`, `10_El_Cono...`): Medidores en Compuertas LSTM/PatchTST, Flujo Zero-Shot Visual y Etiquetas Limpias en el Cono
- **Objetivo de la Tarea:** Eliminar los banners superiores redundantes (`"Arriba:/Abajo:"`, `"Izquierda:/Derecha:"`) en las Diapos 8, 9 y 10; agregar barras de nivel visuales dentro de las 3 compuertas LSTM en Diapo 8; añadir badges de flujo en Diapo 9; y despejar las etiquetas superpuestas sobre las trayectorias de Monte Carlo en la Diapo 10.
- **Entregable:** Prototipos `8`, `9` y `10` en `docs/notebooklm/seccion_1/prototipos/` actualizados.

> **🧠 Explicación:**
> - En la **Diapo 08 (`audit_s8_1366.png`)**, las 3 cajas de compuertas (`1. Compuerta Olvido`, `2. Compuerta Entrada`, `3. Salida / Atención`) son grandes rectángulos casi vacíos con 2 líneas de texto pequeño en el centro. Si añadimos una **barra de progreso visual (medidor de apertura)** e iconos gráficos dentro de cada compuerta y quitamos los banners `"Arriba: ... / Abajo: ..."`, el diagrama cobra vida.
> - En la **Diapo 09 (`audit_s9_1366.png`)**, quitar los banners `"Izquierda: 5 Dominios... / Derecha: Serie Nueva..."` libera espacio para mostrar sobre el nodo central un badge claro `"0 Épocas Locales · Inferencia en Frío"`.
> - En la **Diapo 10 (`audit_s10_1366.png`)**, los textos `"Núcleo 50% (P25–P75)"`, `"Pronóstico Puntual ŷ_t"` y `"Banda Operativa 80% (P10–P90)"` están escritos directamente encima de las curvas serpenteantes de Monte Carlo sin fondo sólido. Colocarles una **pastilla de fondo oscuro semitransparente (`rgba(4, 9, 22, 0.85)`)** alineada a la derecha del cono hace que se lean con contraste perfecto.

> **💡 Cómo hacerlo (ejemplo):**
> ```javascript
> // En 10_El_Cono_de_Incertidumbre_y_Prediccion_Conforme.html:
> // Función helper para dibujar etiquetas con pastilla de alto contraste sobre el cono:
> function drawPillLabel(ctx, text, x, y, textColor, borderColor) {
>   ctx.save();
>   ctx.font = '700 10.5px "JetBrains Mono", monospace';
>   const padX = 8, padY = 4;
>   const tw = ctx.measureText(text).width;
>   const rx = x - tw - padX * 2, ry = y - 10, rw = tw + padX * 2, rh = 20;
>   ctx.fillStyle = 'rgba(4, 9, 22, 0.88)';
>   ctx.strokeStyle = borderColor;
>   ctx.lineWidth = 1;
>   ctx.beginPath();
>   ctx.roundRect(rx, ry, rw, rh, 5);
>   ctx.fill();
>   ctx.stroke();
>   ctx.fillStyle = textColor;
>   ctx.textAlign = 'left';
>   ctx.fillText(text, rx + padX, y + 3.5);
>   ctx.restore();
> }
> ```

- **AC de la Tarea:**
  - [X] Eliminados los banners `.canvas-split-hint` (`"Arriba:/Abajo:"`, `"Izquierda:/Derecha:"`) en las Diapos 8, 9 y 10.
  - [X] En Diapo 8, las 3 compuertas muestran barras visuales de nivel que responden al slider de apertura de memoria ($f_t$).
  - [X] En Diapo 10, todas las etiquetas del cono tienen pastilla de fondo oscuro (`roundRect`) y no se confunden con las trayectorias de Monte Carlo.
- **Tests de la Tarea:**
  - **Test Unitario:** Verificar presencia de `drawPillLabel` (o `roundRect` de fondo en etiquetas) en Diapo 10 y barras de compuerta en Diapo 8.
  - **Test de Simulación de Usuario:** Capturas en Chromium a `1366×768` de Diapos 8, 9 y 10 verificando contraste y limpieza visual.

##### [X] A9.2.3.1 — Enriquecer compuertas en Diapo 08 y flujo Zero-Shot en Diapo 09 retirando banners redundantes
- **Objetivo:** Mejorar la densidad informativa visual de los diagramas en Diapos 8 y 9.
- **Input:** `8_Era_3_Deep_Learning_y_Parches.html` y `9_Era_4_Modelos_Fundacionales_Zero_Shot.html`.
- **Output:** Archivos actualizados con medidores visuales en las compuertas y sin banners redundantes.
- **Proceso:**
  1. Eliminar los recuadros `"Arriba: ... / Abajo: ..."` en Diapo 8 e `"Izquierda: ... / Derecha: ..."` en Diapo 9.
  2. Dibujar dentro de cada caja de compuerta en Diapo 8 una barra horizontal de porcentaje y fórmula compacta.
- **Tests:**
  - **Test Unitario:** Comprobar que no hay errores de ejecución JS en Diapos 8 y 9.
  - **Test de Simulación de Usuario:** Capturas a `1366×768` de Diapos 8 y 9.
- **AC:** Diagramas de Era 3 y Era 4 más grandes, limpios y auto-explicativos.

##### [X] A9.2.3.2 — Aplicar pastillas de alto contraste a las etiquetas del Cono de Incertidumbre en Diapo 10
- **Objetivo:** Evitar que las líneas de Monte Carlo dificulten la lectura de las etiquetas del cono en la Diapo 10.
- **Input:** `docs/notebooklm/seccion_1/prototipos/10_El_Cono_de_Incertidumbre_y_Prediccion_Conforme.html`.
- **Output:** Archivo actualizado con etiquetas encapsuladas en pastillas de fondo oscuro y sin banners superiores redundantes.
- **Proceso:**
  1. Eliminar los 2 banners `"Izquierda: Realidad Observada... / Derecha: Cono..."` sobre el canvas.
  2. Encapsular las etiquetas `Núcleo 50% (P25–P75)`, `Pronóstico Puntual ŷ_t`, `Banda Operativa 80% (P10–P90)` y `Velo 99%` en pastillas con fondo `rgba(4, 9, 22, 0.88)` y borde semántico.
- **Tests:**
  - **Test Unitario:** Verificar uso de `roundRect` para las etiquetas del canvas en Diapo 10.
  - **Test de Simulación de Usuario:** Captura a `1366×768` de Diapo 10 comprobando legibilidad perfecta.
- **AC:** Etiquetas del cono 100% nítidas sobre cualquier nivel de volatilidad del slider.

#### [X] T9.2.4 — Diapo 11 (`11_Arquitectura_de_Decision_y_Cierre_Ejecutivo.html`): Eliminación del Vacío Central y Adición de Medidores Comparativos en las 4 Vías
- **Objetivo de la Tarea:** Eliminar el hueco negro vacío en la mitad de las 4 columnas de la Diapo 11 (`audit_s11_1366.png`), insertar en cada Vía un bloque visual de **3 barras comparativas** (`📊 Escala de Datos N`, `⚡ Costo Cómputo`, `🚀 Extrapolación`) y compactar los bloques `Condición / Ventaja / Límite` a 1 línea concisa cada uno.
- **Entregable:** `docs/notebooklm/seccion_1/prototipos/11_Arquitectura_de_Decision_y_Cierre_Ejecutivo.html` rediseñado sin espacios muertos.

> **🧠 Explicación:** En la captura actual de la Diapo 11 (`audit_s11_1366.png`), cada una de las 4 columnas (`.lane-card`) tiene arriba el título y los chips de modelos, luego un **vacío negro de ~130px de alto**, y abajo 3 cajas de texto (`CONDICIÓN`, `VENTAJA`, `LÍMITE`). Esto ocurre porque el contenedor usa `justify-content: space-between` sin un elemento visual intermedio. Al cambiar a una distribución continua (`justify-content: flex-start; gap: 8px`) e insertar en ese espacio un **panel gráfico de 3 barras de nivel (Medidores de Arquitectura)** para comparar visualmente cuántos datos pide cada familia, cuánta GPU consume y si extrapola tendencias, las 4 columnas pasan de ser texto plano con huecos a un **dashboard comparativo ejecutivo** sin un solo píxel desperdiciado.

> **💡 Cómo hacerlo (ejemplo):**
> ```html
> <!-- Bloque de medidores visuales a insertar dentro de cada .lane-card en Diapo 11 -->
> <div class="lane-meters">
>   <div class="meter-row">
>     <span class="meter-lbl">📊 Datos (N)</span>
>     <div class="meter-track"><div class="meter-fill" style="width: 25%; background: var(--ockham);"></div></div>
>     <span class="meter-val">&lt; 500</span>
>   </div>
>   <div class="meter-row">
>     <span class="meter-lbl">⚡ Cómputo</span>
>     <div class="meter-track"><div class="meter-fill" style="width: 15%; background: var(--lab);"></div></div>
>     <span class="meter-val">CPU μs</span>
>   </div>
>   <div class="meter-row">
>     <span class="meter-lbl">🚀 Extrapola</span>
>     <div class="meter-track"><div class="meter-fill" style="width: 75%; background: var(--phi);"></div></div>
>     <span class="meter-val">Con Techo L</span>
>   </div>
> </div>
> ```
> ```css
> .lane-meters {
>   display: flex;
>   flex-direction: column;
>   gap: 5px;
>   padding: 8px 10px;
>   border-radius: 8px;
>   background: rgba(5, 11, 24, 0.78);
>   border: 1px solid rgba(148, 163, 184, 0.16);
> }
> .meter-row { display: grid; grid-template-columns: 76px 1fr 62px; align-items: center; gap: 6px; font: 600 9.5px/1 var(--mono); }
> .meter-track { height: 6px; border-radius: 999px; background: rgba(148, 163, 184, 0.14); overflow: hidden; }
> .meter-fill { height: 100%; border-radius: 999px; }
> ```

- **AC de la Tarea:**
  - [X] Eliminado el hueco vacío central en las 4 columnas de la Diapo 11.
  - [X] Cada una de las 4 Vías muestra el bloque `.lane-meters` con las 3 barras comparativas (`Datos (N)`, `Cómputo`, `Extrapola`).
  - [X] Las cajas `CONDICIÓN`, `VENTAJA` y `LÍMITE` tienen máximo 1–2 líneas escaneables y tamaño de fuente legible (`clamp(10.5px, 0.78vw, 12px)`).
- **Tests de la Tarea:**
  - **Test Unitario:** Comprobar que existen exactamente 4 bloques `.lane-meters` (12 `.meter-row`) en `11_Arquitectura_de_Decision_y_Cierre_Ejecutivo.html`.
  - **Test de Simulación de Usuario:** Capturas de Diapo 11 a `1366×768` y `1920×1080` verificando distribución vertical continua sin huecos negros ni desbordes.

##### [X] A9.2.4.1 — Insertar `.lane-meters` en las 4 Vías y ajustar el layout flex de `.lane-card` en Diapo 11
- **Objetivo:** Reemplazar el espacio muerto central de las 4 columnas por medidores gráficos comparativos.
- **Input:** `docs/notebooklm/seccion_1/prototipos/11_Arquitectura_de_Decision_y_Cierre_Ejecutivo.html`.
- **Output:** Archivo actualizado con medidores visuales y textos compactados.
- **Proceso:**
  1. Cambiar el layout vertical de `.lane-card` para eliminar `justify-content: space-between` que separaba el tope del fondo.
  2. Añadir `.lane-meters` en Vía 1 (`<500`, `CPU μs`, `Techo L`), Vía 2 (`10³–10⁵`, `CPU ms`, `No (Meseta)`), Vía 3 (`>10⁵`, `GPU O((L/P)²)`, `Sí (Fluida)`) y Vía 4 (`Cold-Start`, `0 Entreno`, `Sí + Cono SCP`).
  3. Sintetizar los textos de `CONDICIÓN`, `VENTAJA` y `LÍMITE` en las 4 columnas.
- **Tests:**
  - **Test Unitario:** Verificar presencia de las 12 filas `.meter-row` en el archivo HTML.
  - **Test de Simulación de Usuario:** Captura en Chromium a `1366×768` de la Diapo 11.
- **AC:** Las 4 columnas de la Diapo 11 lucen equilibradas, visuales y sin espacios muertos.

---

### [X] SF9.3 — Rediseño Pedagógico-Visual y Corrección de Solapamientos en la Sección 3 (Diapositivas 19 a 23)

- **Objetivo:** Corregir el 100% de los recortes y solapamientos gráficos detectados en la Sección 3 (Diapos 19, 20, 21, 22 y 23) y transformar las cajas de texto anidadas dentro de `.sim-card` en tarjetas KPI visuales y diagramas biofísicos limpios.
- **Entregable:** Prototipos `19`, `20`, `21`, `22` y `23` en `docs/notebooklm/seccion_3/prototipos/` corregidos y verificados.
- **AC de la Sub fase:**
  - [X] Cero texto cortado en el detalle inferior de los 5 escalones de la Diapo 20.
  - [X] Cero solapamiento entre el texto `"Retraso (τ) 6-8 meses"` y el engranaje en la Diapo 21.
  - [X] Cero etiquetas truncadas (`"Florac..."`) dentro del reloj fenológico de la Diapo 22.
  - [X] Cero solapamiento entre el botón `"Ir al Caso Jaén →"` y el texto en la Diapo 23, y cero barra de scroll vertical izquierda.
- **Tests de la Sub fase:**
  - **Test Unitario:** Verificación de estilos CSS/DOM y ausencia de colisiones de `boundingClientRect` en los elementos interactivos de las Diapos 19 a 23.
  - **Test de Simulación de Usuario:** Capturas en Chromium headless a `1366×768` y `1920×1080` de las Diapos 19 a 23.

#### [X] T9.3.1 — Diapos 19 y 20 (`19_c_mo_el_agro...` y `20_del_almanaque_al_sat_lite.html`): Espejo Histórico con Callouts Limpios y Corrección del Recorte en los 5 Escalones
- **Objetivo de la Tarea:** Eliminar los banners superiores redundantes en las Diapos 19 y 20; simplificar las cajas flotantes del espejo histórico en Diapo 19; y reemplazar el recuadro inferior cortado de la Diapo 20 (`audit_s20_1366.png`) por una fila de **3 tarjetas KPI horizontales** (`⏱️ Frecuencia`, `📡 Sensor / Escala`, `🎯 Impacto Operativo`) que nunca se corten verticalmente.
- **Entregable:** `19_c_mo_el_agro_invent_el_forecasting.html` y `20_del_almanaque_al_sat_lite.html` actualizados.

> **🧠 Explicación:** En la Diapo 20 (`audit_s20_1366.png`), arriba del gráfico hay 2 cajas de instrucciones (*"📈 Arriba: Curva Exponencial... / 🔬 Abajo: Haz clic o desliza..."*) que empujan el canvas hacia abajo. Como consecuencia, el recuadro rojo inferior que describe el escalón activo tiene muy poca altura y **corta por la mitad la segunda viñeta** (*"• Reto: 500 variables (p) frente a solo N=24 cosechas anuales..."*). Si eliminamos los 2 banners de instrucciones superiores (ganando `48px` de altura) y convertimos el recuadro inferior en un **grid horizontal de 3 tarjetas KPI compactas de 1 línea**, toda la información cabe con holgura en `1366×768` y es mucho más fácil de leer que un bloque de viñetas largas.

> **💡 Cómo hacerlo (ejemplo):**
> ```html
> <!-- En 20_del_almanaque_al_sat_lite.html: reemplazar el bloque inferior que se cortaba por un grid de 3 KPIs: -->
> <div class="step-kpi-strip" id="stepKpiStrip">
>   <div class="step-kpi-cell">
>     <span class="step-kpi-lbl">⏱️ FRECUENCIA Y ESCALA</span>
>     <strong class="step-kpi-val" id="kpiFreq">1 dato / día / píxel (10m)</strong>
>   </div>
>   <div class="step-kpi-cell">
>     <span class="step-kpi-lbl">✅ LOGRO OPERATIVO</span>
>     <strong class="step-kpi-val" id="kpiGain">Fusión Clima (CHIRPS) + Suelo + Satélite</strong>
>   </div>
>   <div class="step-kpi-cell warn">
>     <span class="step-kpi-lbl">⚠️ RETO MATEMÁTICO</span>
>     <strong class="step-kpi-val" id="kpiRisk">p = 500 variables vs N = 24 cosechas</strong>
>   </div>
> </div>
> ```
> ```css
> .step-kpi-strip {
>   display: grid;
>   grid-template-columns: repeat(3, 1fr);
>   gap: 8px;
>   padding: 7px 10px;
>   border-radius: 10px;
>   background: rgba(8, 16, 34, 0.9);
>   border: 1px solid rgba(56, 239, 255, 0.3);
>   flex-shrink: 0;
> }
> .step-kpi-lbl { display: block; font: 600 8.5px/1.1 var(--mono); color: var(--muted); }
> .step-kpi-val { display: block; font: 700 clamp(10px, 0.78vw, 11.5px)/1.25 var(--sans); color: #edf5ff; margin-top: 2px; }
> ```

- **AC de la Tarea:**
  - [X] En Diapo 19 se eliminan los 2 banners superiores redundantes y las tarjetas superpuestas sobre el valle ancestral/IA se reducen a callouts compactos de 2 líneas.
  - [X] En Diapo 20 desaparecen los 2 banners superiores redundantes y el panel inferior muestra las 3 celdas `.step-kpi-cell` sin ningún texto cortado en `1366×768`.
- **Tests de la Tarea:**
  - **Test Unitario:** Comprobar en Diapo 20 que el contenedor de detalle inferior no tiene desborde (`scrollHeight <= clientHeight`).
  - **Test de Simulación de Usuario:** Capturas en Chromium a `1366×768` de Diapos 19 y 20 verificando que todas las líneas inferiores se leen completas.

##### [X] A9.3.1.1 — Limpiar banners y compactar callouts del espejo histórico en Diapo 19
- **Objetivo:** Despejar la ilustración del valle ancestral vs gemelo digital en la Diapo 19.
- **Input:** `docs/notebooklm/seccion_3/prototipos/19_c_mo_el_agro_invent_el_forecasting.html`.
- **Output:** Archivo actualizado con mayor área de dibujo y callouts concisos.
- **Proceso:**
  1. Retirar los 2 banners superiores `"Izquierda: 10,000 a.C... / Derecha: Presente..."` dentro de `.sim-card`.
  2. Compactar las 2 cajas inferiores dentro del canvas a 2 líneas breves de alto contraste.
- **Tests:**
  - **Test Unitario:** Verificar ausencia de errores JS en Diapo 19.
  - **Test de Simulación de Usuario:** Captura a `1366×768` de Diapo 19.
- **AC:** Ilustración del espejo histórico despejada y de lectura rápida.

##### [X] A9.3.1.2 — Reemplazar el recuadro inferior cortado por `.step-kpi-strip` de 3 columnas en Diapo 20
- **Objetivo:** Corregir definitivamente el texto cortado en la parte inferior del gráfico de los 5 escalones en la Diapo 20.
- **Input:** `docs/notebooklm/seccion_3/prototipos/20_del_almanaque_al_sat_lite.html`.
- **Output:** Archivo actualizado con 3 tarjetas KPI horizontales por escalón y sin banners redundantes.
- **Proceso:**
  1. Retirar los 2 banners superiores `"Arriba: Curva Exponencial... / Abajo: Haz clic..."`.
  2. Sustituir el cuadro de viñetas inferior que se truncaba en el Canvas/DOM por un grid de 3 celdas KPI (`Frecuencia/Escala`, `Logro Operativo`, `Reto/Límite`) alimentado dinámicamente al cambiar de escalón (1 a 5).
- **Tests:**
  - **Test Unitario:** Verificar que para los 5 escalones las 3 celdas KPI se renderizan sin truncamiento (`scrollHeight <= clientHeight`).
  - **Test de Simulación de Usuario:** Captura a `1366×768` de Diapo 20 verificando que el Escalón 5 se ve 100% íntegro.
- **AC:** Cero líneas cortadas en la Diapo 20 a `1366×768` y `1920×1080`.

#### [X] T9.3.2 — Diapo 21 (`21_f_sica_biol_gica_y_el_l_mite_algor_tmico.html`): Puente de Retraso ($\tau = 6\text{–}8\text{m}$) sin Solape en Engranaje y Zonas de Umbral VPD
- **Objetivo de la Tarea:** Corregir el solapamiento del texto `"Retraso (τ) 6-8 meses"` sobre los dientes del engranaje central en la Diapo 21 (`audit_s21_1366.png`), eliminar los 2 banners superiores redundantes, y colorear en el gráfico derecho la **Zona Óptima (`VPD < 1.8 kPa`)** vs la **Zona de Aborto Floral (`VPD > 1.8 kPa / >32 °C`)**.
- **Entregable:** `docs/notebooklm/seccion_3/prototipos/21_f_sica_biol_gica_y_el_l_mite_algor_tmico.html` actualizado.

> **🧠 Explicación:** En la captura de la Diapo 21 (`audit_s21_1366.png`), el texto blanco `"Retraso (τ) 6-8 meses"` está dibujado directamente encima de los trazos amarillos del engranaje central sin un fondo opaco, haciéndolo ilegible. Colocando una **pastilla circular o rectangular con fondo oscuro `#040916` y borde ámbar** sobre el centro del engranaje (o justo debajo de él como puente temporal `[Ago-Oct] ──► [May-Jul]`), el número `τ = 6–8 meses` resalta con nitidez total. Asimismo, en el gráfico derecho, sombrear en verde suave la zona bajo el umbral y en rojo carmesí la zona de colapso biológico hace evidente por qué una regresión lineal falla ante un umbral no lineal de temperatura/VPD.

> **💡 Cómo hacerlo (ejemplo):**
> ```javascript
> // En el dibujo del engranaje de 21_f_sica_biol_gica_y_el_l_mite_algor_tmico.html:
> // Dibujar placa central sólida sobre el engranaje antes de escribir el texto:
> ctx.save();
> ctx.fillStyle = 'rgba(4, 9, 22, 0.94)';
> ctx.strokeStyle = 'rgba(255, 192, 92, 0.75)';
> ctx.lineWidth = 1.5;
> ctx.beginPath();
> ctx.roundRect(cx - 48, cy - 16, 96, 32, 8);
> ctx.fill();
> ctx.stroke();
> ctx.fillStyle = '#ffc05c';
> ctx.font = '700 10.5px "JetBrains Mono"';
> ctx.textAlign = 'center';
> ctx.fillText('Lag τ = 6–8m', cx, cy - 2);
> ctx.fillStyle = '#edf5ff';
> ctx.font = '500 9px "Inter"';
> ctx.fillText('Memoria oculta', cx, cy + 10);
> ctx.restore();
> ```

- **AC de la Tarea:**
  - [X] Eliminados los 2 banners superiores `"Izquierda: Estímulo... / Derecha: Curva Sigmoide..."` dentro de `.sim-card`.
  - [X] El texto del engranaje cuenta con una placa sólida de alto contraste y no pisa los dientes del engranaje.
  - [X] El gráfico de umbral derecho incluye sombreado de zona segura (verde) y zona de colapso/aborto floral (rojo).
- **Tests de la Tarea:**
  - **Test Unitario:** Verificar la presencia del `roundRect` de fondo en el centro del engranaje y las regiones sombreadas en el gráfico derecho.
  - **Test de Simulación de Usuario:** Captura a `1366×768` de la Diapo 21 comprobando lectura limpia del engranaje y de la curva de colapso.

##### [X] A9.3.2.1 — Agregar placa de alto contraste al engranaje $\tau$ y zonas coloreadas al gráfico VPD en Diapo 21
- **Objetivo:** Eliminar el solapamiento del engranaje y hacer visualmente explicativo el umbral de aborto floral.
- **Input:** `docs/notebooklm/seccion_3/prototipos/21_f_sica_biol_gica_y_el_l_mite_algor_tmico.html`.
- **Output:** Archivo actualizado sin solapamientos y con regiones de umbral coloreadas.
- **Proceso:**
  1. Eliminar los 2 banners superiores redundantes dentro del panel derecho.
  2. Añadir la placa `roundRect` oscura sobre el centro del engranaje para rotular `Lag τ = 6–8m`.
  3. Añadir rellenos translúcidos verde/rojo en el gráfico de umbral derecho para distinguir fotosíntesis normal vs aborto floral.
- **Tests:**
  - **Test Unitario:** Comprobar sintaxis JS sin errores en Diapo 21.
  - **Test de Simulación de Usuario:** Captura en Chromium a `1366×768` de Diapo 21.
- **AC:** Cero solapamiento en el engranaje y umbral VPD visualmente claro.

#### [X] T9.3.3 — Diapo 22 (`22_reloj_fenol_gico_del_caf.html`): Ampliación del Reloj Botánico con Etiquetas Externas Limpias y Diagnóstico Compacto
- **Objetivo de la Tarea:** Corregir el truncamiento y solape de las palabras `"Florac..."`, `"Llenado"` y `"Cosecha"` dentro del reloj fenológico (`audit_s22_1366.png`), eliminar los 2 banners superiores redundantes para aumentar el radio del reloj en $\ge 20\%$, y simplificar el panel derecho de diagnóstico en **3 tarjetas ejecutivas escaneables de 1 línea** (`🌱 Fisiología`, `🔥 Umbral Fatal`, `🤖 Regla IA`).
- **Entregable:** `docs/notebooklm/seccion_3/prototipos/22_reloj_fenol_gico_del_caf.html` actualizado.

> **🧠 Explicación:** En la captura actual de la Diapo 22 (`audit_s22_1366.png`), el anillo interior del reloj fenológico es tan estrecho que la palabra `"Floración"` se corta como `"Florac"` pisando los bordes del sector, y `"Cosecha"` pisa la línea divisoria vertical. Además, los 2 banners superiores (*"Izquierda: Reloj Fenológico... / Derecha: Fisiología..."*) le quitan altura al reloj, y la tarjeta derecha repite 3 párrafos densos. Si quitamos los 2 banners superiores, el reloj gana ~45px de diámetro; y si dibujamos las etiquetas de las 3 ventanas (`1. Floración (56%)`, `2. Llenado (r=0.75)`, `3. Cosecha`) en **pastillas con fondo oscuro (`roundRect`) bien posicionadas** y sintetizamos el panel derecho en 3 filas KPI directas, la diapositiva se vuelve impecable.

> **💡 Cómo hacerlo (ejemplo):**
> ```javascript
> // En 22_reloj_fenol_gico_del_caf.html:
> // En lugar de escribir texto suelto que desborda el arco estrecho, dibujar una pastilla centrada en el ángulo medio de cada ventana o en el borde exterior:
> function drawPhaseBadge(ctx, cx, cy, radius, angleRad, text, borderColor, isActive) {
>   const x = cx + Math.cos(angleRad) * radius;
>   const y = cy + Math.sin(angleRad) * radius;
>   ctx.save();
>   ctx.font = (isActive ? '700 ' : '600 ') + '10px "JetBrains Mono", monospace';
>   const tw = ctx.measureText(text).width + 12;
>   const th = 18;
>   ctx.fillStyle = isActive ? 'rgba(10, 22, 44, 0.96)' : 'rgba(4, 9, 22, 0.88)';
>   ctx.strokeStyle = borderColor;
>   ctx.lineWidth = isActive ? 1.8 : 1.1;
>   ctx.beginPath();
>   ctx.roundRect(x - tw / 2, y - th / 2, tw, th, 5);
>   ctx.fill();
>   ctx.stroke();
>   ctx.fillStyle = '#edf5ff';
>   ctx.textAlign = 'center';
>   ctx.textBaseline = 'middle';
>   ctx.fillText(text, x, y);
>   ctx.restore();
> }
> ```

- **AC de la Tarea:**
  - [X] Eliminados los 2 banners superiores redundantes dentro de `.sim-card` en la Diapo 22.
  - [X] Ninguna etiqueta del reloj fenológico (`Floración`, `Llenado`, `Cosecha`, ni los 12 meses) aparece cortada ni superpuesta.
  - [X] Las 3 cajas del panel de diagnóstico derecho (`Proceso Fisiológico`, `Umbral Crítico`, `Traducción IA`) tienen máximo 1–2 líneas concisas cada una.
- **Tests de la Tarea:**
  - **Test Unitario:** Verificar en el código de la Diapo 22 que no se trunquen strings de fases y que las pastillas se dibujen con `roundRect`.
  - **Test de Simulación de Usuario:** Capturas en Chromium a `1366×768` y `1920×1080` de la Diapo 22 comprobando que las 3 etiquetas del reloj se leen completas.

##### [X] A9.3.3.1 — Ampliar radio del reloj fenológico, encapsular etiquetas de fases y compactar panel derecho en Diapo 22
- **Objetivo:** Resolver el truncamiento de `"Florac..."` y hacer escaneable la ficha fisiológica derecha.
- **Input:** `docs/notebooklm/seccion_3/prototipos/22_reloj_fenol_gico_del_caf.html`.
- **Output:** Archivo actualizado con reloj ampliado, etiquetas en pastillas limpias y ficha derecha concisa.
- **Proceso:**
  1. Eliminar los 2 banners superiores dentro de `.sim-card`.
  2. Ajustar el cálculo de `outerR` / `innerR` para aprovechar el espacio ganado y usar `drawPhaseBadge` para mostrar `Floración`, `Llenado` y `Cosecha` sin recortes.
  3. Reducir a 1 línea directa cada uno de los 3 sub-bloques de la tarjeta derecha.
- **Tests:**
  - **Test Unitario:** Comprobar sintaxis JS de `22_reloj_fenol_gico_del_caf.html`.
  - **Test de Simulación de Usuario:** Captura a `1366×768` de la Diapo 22.
- **AC:** Reloj fenológico nítido, grande y con cero textos truncados.

#### [X] T9.3.4 — Diapo 23 (`23_precisi_n_actual_y_las_tres_trampas.html`): Eliminación de Scrollbar, Corrección de Solape en "Prueba de Fuego" y Tarjetas `❌ Error vs ✅ Remedio`
- **Objetivo de la Tarea:** Corregir el solapamiento del botón `"Ir al Caso Jaén →"` sobre el texto de `"🔥 LA PRUEBA DE FUEGO"` (`audit_s23_1366.png`), eliminar los 2 banners superiores redundantes dentro de `.sim-card`, y formatear las 3 tarjetas de trampas con contraste visual directo `❌ Trampa` vs `✅ Remedio`.
- **Entregable:** `docs/notebooklm/seccion_3/prototipos/23_precisi_n_actual_y_las_tres_trampas.html` sin solapamientos ni barras de scroll.

> **🧠 Explicación:** En la captura de la Diapo 23 (`audit_s23_1366.png`), dentro de la columna derecha del gráfico, la cuarta tarjeta inferior (*"🔥 LA PRUEBA DE FUEGO"*) tiene un botón naranja `"Ir al Caso Jaén →"` posicionado encima del texto *"La teoría es hermosa, pero mañana la mediremos en Jaén..."*, tapando el final de la oración. Esto ocurre porque el botón no está en una columna separada del contenedor flex/grid. Cambiando esa tarjeta a `display: grid; grid-template-columns: minmax(0, 1fr) auto; align-items: center; gap: 10px` y quitando los 2 banners superiores redundantes (`"Izquierda: Stack 3D... / Derecha: Las 3 Trampas..."`), las 3 tarjetas de trampas y el banner de prueba de fuego disponen de espacio suficiente sin pisarse jamás.

> **💡 Cómo hacerlo (ejemplo):**
> ```css
> /* En 23_precisi_n_actual_y_las_tres_trampas.html: corregir layout del banner inferior derecho */
> .fire-test-card {
>   display: grid;
>   grid-template-columns: minmax(0, 1fr) auto;
>   align-items: center;
>   gap: 10px;
>   padding: 8px 12px;
>   border-radius: 10px;
>   border: 1px solid rgba(255, 192, 92, 0.4);
>   background: linear-gradient(135deg, rgba(60, 28, 8, 0.65), rgba(12, 18, 34, 0.92));
> }
> .fire-test-btn {
>   position: static !important; /* Nunca position: absolute sobre el texto */
>   white-space: nowrap;
>   flex-shrink: 0;
> }
> ```

- **AC de la Tarea:**
  - [X] El botón `"Ir al Caso Jaén →"` no se superpone con ningún carácter del texto de `"🔥 LA PRUEBA DE FUEGO"` ni en `1366×768` ni en `1920×1080`.
  - [X] Eliminados los 2 banners superiores `"Izquierda: Stack 3D... / Derecha: Las 3 Trampas..."` dentro de `.sim-card`.
  - [X] Cada una de las 3 tarjetas de trampas muestra claramente `❌ Error:` y `✅ Remedio:` en 1 línea cada uno sin recortes.
- **Tests de la Tarea:**
  - **Test Unitario:** Evaluación en DOM headless comprobando que `textRect.right <= btnRect.left` dentro del contenedor de Prueba de Fuego.
  - **Test de Simulación de Usuario:** Captura en Chromium a `1366×768` de la Diapo 23 verificando ausencia de scrollbar izquierda y ausencia de solape en el botón derecho.

##### [X] A9.3.4.1 — Corregir grid de "Prueba de Fuego", eliminar banners redundantes y compactar las 3 tarjetas de trampas en Diapo 23
- **Objetivo:** Dejar la Diapo 23 libre de solapamientos y barras de scroll en cualquier resolución.
- **Input:** `docs/notebooklm/seccion_3/prototipos/23_precisi_n_actual_y_las_tres_trampas.html`.
- **Output:** Archivo actualizado con layout grid limpio en el banner inferior y tarjetas `❌ / ✅` escaneables.
- **Proceso:**
  1. Eliminar los 2 banners superiores redundantes dentro del panel derecho.
  2. Aplicar `display: grid; grid-template-columns: minmax(0, 1fr) auto; align-items: center; gap: 10px` al contenedor de `"🔥 LA PRUEBA DE FUEGO"` y asegurar `position: static` en el botón `"Ir al Caso Jaén →"`.
  3. Formatear las 3 tarjetas de trampas (`Trampa NDVI`, `Trampa τ`, `Trampa N=24`) con 2 líneas limpias (`❌` y `✅`).
- **Tests:**
  - **Test Unitario:** Verificar ausencia de `position: absolute` en el botón de Prueba de Fuego.
  - **Test de Simulación de Usuario:** Captura en Chromium a `1366×768` de la Diapo 23.
- **AC:** Cero solapamiento y cero scrollbars en la Diapo 23.

---

### [X] SF9.4 — Compilación del Deck Maestro y Auditoría Visual Multi-Resolución

- **Objetivo:** Compilar los 12 prototipos optimizados dentro de `presentacion.html` e `index.html` y ejecutar una auditoría automatizada (script + capturas Chromium a `1366×768` y `1920×1080`) que certifique cero barras de scroll, cero solapamientos y reducción $\ge 40\%$ de texto.
- **Entregable:** `presentacion.html`, `index.html`, script `scripts/audit_f9_desaturacion.py` y capturas `screenshots/f9_s{5..11,19..23}_{1366,1920}.png`.
- **AC de la Sub fase:**
  - [X] `back/build_deck.py` compila sin errores generando `presentacion.html` e `index.html`.
  - [X] `scripts/audit_f9_desaturacion.py` pasa al 100% sin violaciones.
  - [X] Las 24 capturas PNG (`12 diapos × 2 resoluciones`) confirman visualmente el acabado gerencial.
- **Tests de la Sub fase:**
  - **Test Unitario:** Ejecución de `.venv/bin/python scripts/audit_f9_desaturacion.py`.
  - **Test de Simulación de Usuario:** Renderizado y captura en Chromium headless de las 12 diapositivas en `1366×768` y `1920×1080`.

#### [X] T9.4.1 — Compilación Integral del Deck Offline (`back/build_deck.py`) y Verificación de Notas del Orador
- **Objetivo de la Tarea:** Ejecutar el compilador `back/build_deck.py` para inyectar en Base64 los 12 prototipos rediseñados de las Secciones 1 y 3 junto con las notas actualizadas de `front/deck_notes.py`.
- **Entregable:** `presentacion.html` e `index.html` actualizados en la raíz del repositorio.

> **🧠 Explicación:** Como `presentacion.html` e `index.html` son aplicaciones *single-file* 100% autónomas que embeben cada prototipo mediante `data:text/html;base64,...`, cualquier mejora realizada en `docs/notebooklm/seccion_1/prototipos/` o `seccion_3/prototipos/` requiere ejecutar `back/build_deck.py` para que los iframes del deck principal reflejen los cambios.

> **💡 Cómo hacerlo (ejemplo):**
> ```bash
> .venv/bin/python back/build_deck.py
> ```

- **AC de la Tarea:**
  - [X] El comando `.venv/bin/python back/build_deck.py` termina con código de salida `0`.
  - [X] `presentacion.html` e `index.html` tienen exactamente el mismo tamaño y contienen los 12 iframes actualizados.
- **Tests de la Tarea:**
  - **Test Unitario:** Verificar que el hash Base64 de cada uno de los 12 archivos HTML esté presente dentro de `presentacion.html`.
  - **Test de Simulación de Usuario:** Abrir `presentacion.html` en Chromium headless y verificar que las 30 diapositivas cargan sin errores de consola.

##### [X] A9.4.1.1 — Ejecutar `back/build_deck.py` y validar sincronización de Base64 en `presentacion.html` e `index.html`
- **Objetivo:** Regenerar los bundles finales de la presentación.
- **Input:** Los 12 prototipos HTML modificados y `front/deck_notes.py`.
- **Output:** `presentacion.html` e `index.html` compilados.
- **Proceso:**
  1. Ejecutar `.venv/bin/python back/build_deck.py`.
  2. Comprobar que los 12 prototipos codificados en Base64 se inyectaron sin cadenas vacías.
- **Tests:**
  - **Test Unitario:** Script rápido que comprueba que ningún `src="data:text/html;base64,"` esté vacío en `presentacion.html`.
  - **Test de Simulación de Usuario:** Carga del deck en navegador headless.
- **AC:** Deck compilado y 100% autónomo offline.

#### [X] T9.4.2 — Auditoría Automatizada DOM + Capturas Chromium (`1366×768` y `1920×1080`)
- **Objetivo de la Tarea:** Crear y ejecutar `scripts/audit_f9_desaturacion.py` y generar las capturas de pantalla en Chromium headless a `1366×768` y `1920×1080` para las Diapos 5–11 y 19–23, verificando visualmente que se cumplan todos los criterios de desaturación y diseño explicativo.
- **Entregable:** `scripts/audit_f9_desaturacion.py` y capturas `screenshots/f9_s{5..11,19..23}_{1366,1920}.png`.

> **🧠 Explicación:** La verificación en dos niveles —un script estático que audita conteos de palabras y ausencia de elementos prohibidos (`.speaker-box` largos, `.canvas-split-hint` redundantes) más la inspección visual de capturas reales en `1366×768` (la resolución más restrictiva de proyector/laptop) y `1920×1080`— garantiza que ningún recorte o barra de scroll pase desapercibido antes de dar por cerrada la Fase 9.

> **💡 Cómo hacerlo (ejemplo):**
> ```bash
> # 1. Ejecutar auditoría estática de desaturación:
> .venv/bin/python scripts/audit_f9_desaturacion.py
>
> # 2. Capturar las 12 diapositivas en 1366x768 y 1920x1080 con Chromium headless:
> mkdir -p screenshots
> for s in 5 6 7 8 9 10 11 19 20 21 22 23; do
>   chromium --headless=new --no-sandbox --disable-gpu --screenshot=screenshots/f9_s${s}_1366.png --window-size=1366,768 "file://$(pwd)/presentacion.html#${s}"
>   chromium --headless=new --no-sandbox --disable-gpu --screenshot=screenshots/f9_s${s}_1920.png --window-size=1920,1080 "file://$(pwd)/presentacion.html#${s}"
> done
> ```

- **AC de la Tarea:**
  - [X] `scripts/audit_f9_desaturacion.py` retorna `exit code 0` (0 etapas $> 110$ palabras, 0 `"GUÍA DE EXPOSICIÓN"`, 0 `.canvas-split-hint` redundantes).
  - [X] Las 24 capturas en `screenshots/f9_s*_{1366,1920}.png` muestran cero barras de scroll verticales, cero textos cortados y diagramas limpios.
- **Tests de la Tarea:**
  - **Test Unitario:** Ejecución de `.venv/bin/python scripts/audit_f9_desaturacion.py`.
  - **Test de Simulación de Usuario:** Inspección visual de las capturas `f9_s5_1366.png` a `f9_s23_1366.png` y `1920.png`.

##### [X] A9.4.2.1 — Crear y ejecutar `scripts/audit_f9_desaturacion.py` e inspeccionar las 24 capturas en Chromium
- **Objetivo:** Certificar objetiva y visualmente el cierre de la Fase 9.
- **Input:** Los 12 prototipos HTML y `presentacion.html`.
- **Output:** `scripts/audit_f9_desaturacion.py` en verde y 24 capturas PNG verificadas.
- **Proceso:**
  1. Escribir `scripts/audit_f9_desaturacion.py` validando conteos de palabras y reglas DOM en los 12 archivos HTML.
  2. Ejecutar el bucle de capturas con `chromium --headless=new` a `1366×768` y `1920×1080`.
  3. Inspeccionar las capturas generadas y marcar los checkboxes en `docs/task/tareas.md` y `docs/task/fases/fase_9_desaturacion_visual_s1_s3.md`.
- **Tests:**
  - **Test Unitario:** `.venv/bin/python scripts/audit_f9_desaturacion.py`.
  - **Test de Simulación de Usuario:** Revisión completa de las 24 capturas PNG generadas.
- **AC:** Auditoría 100% en verde en ambas resoluciones.
