# Fase 12: Claridad Pedagógica para Audiencia No Estadística y Pulido Profesional de Deck y Videos

> **Documento de Fase:** `docs/reference/fases/fase_12_claridad_no_estadistica_deck_videos.md`
> **Archivos objetivo (deck):** `front/prototype_engine.py`, `front/deck_slides_p1.py`, `front/deck_slides_p2.py`, `front/deck_styles.py`, `front/deck_notes.py`, `back/build_deck.py`, los 21 prototipos de `docs/notebooklm/seccion_{1,2,3,4}/prototipos/`, `presentacion.html`, `index.html`
> **Archivos objetivo (video):** `video/seccion_*/diapo_*/video_*/{scene_template.html,build_scene.py,render.sh,capture.mjs}` (9 videos) y nuevo `video/_pipeline/`
> **Validadores nuevos:** `scripts/audit_f12_claridad.py`
> **Estado:** `[ ] Pendiente` (planificada el 28 de octubre de 2026 — auditoría previa a codear)

---

## 1. Diagnóstico de Auditoría (28-10-2026, Chromium headless @1920×1080 + keyframes de los 9 videos)

Público objetivo real: **personas sin formación estadística** (Iquitos Data Fest, Aula Magna). El deck actual está pulido técnicamente (F7–F11) pero habla para estadísticos.

| # | Problema Detectado | Evidencia medida | Diapositivas / Videos |
|---|---|---|---|
| **D1** | **Jerga sin traducir.** Términos como *Lyapunov, Diebold-Mariano, MASE/MSIW, conformal, O(L²), VPD kPa, cuantil, holdout, 4D-Var* aparecen sin definición. El glosario emergente prometido en `T5.2.2` **no existe** (0 `data-term`/`<abbr>`/tooltips en `presentacion.html`). | Conteo de términos técnicos por prototipo: Diapo 21 = **161**, Diapo 9 = **132**, Diapo 10 = **98**, Diapo 23 = **96**, Diapos 7/8 = **86**, Diapo 15 = **81**, Diapo 27 = **73**. | 7, 8, 9, 10, 14, 15, 17, 20, 21, 23, 26, 27 |
| **D2** | **Sobrecarga: no hay "una idea por pantalla".** 18 prototipos × 4 etapas = **72 pantallas** en ~35 min; cada pantalla muestra cabecera + barra de etapas + ficha técnica + 2 columnas + píldora. 300–600 palabras visibles por prototipo. | Palabras visibles: Diapo 6 (v2) = 607, Diapo 17 = 507, Diapo 23 = 495, Diapo 21 = 488, Diapo 22 = 480. | 5–17, 19–23, 25–27 |
| **D3** | **Cifras crudas sin significado cotidiano.** `p = 0.918`, `r = 0.1536`, `RMSE 1.880 °C`, `MASE 0.362`, `q̂ = 6.23 qq/ha` con 3–4 decimales y sin comparación ("±2 °C ≈ un termómetro de farmacia"). | 20 bloques con RMSE/MAE/p/cuantiles en el deck; ninguno con frase de traducción. | 10, 13, 14, 15, 16, 26, 27, 29 |
| **D4** | **Jerarquía invertida y taxonomía mezclada.** El mensaje principal (`💡 Idea Clave`) está al pie en tipografía pequeña; los títulos alternan *"VÍA 1"*, *"Era 2"*, *"Acto 2"*, *"Sección 3"*, *"Etapa 4 de 4"*, *"Pilar 1 de 4"*. Botones internos *"Pase a Diapo 14 →"* duplican la navegación del deck. | Captura de las 30 diapos: en ninguna de las 18 interactivas el titular legible a 5 m es el mensaje; 11 botones *"Pase a Diapo"* / *"Ir a"*. | 5–11, 12–17, 19–23, 25–27 |
| **D5** | **Videos ilegibles en proyección y mudos.** Tipografía de 9–13 px sobre lienzo 1600×900 (≈1.2 % del alto), gráfico central ocupa <40 % del lienzo, sin narración ni subtítulos: **9 videos × 30 s = 4.5 min de silencio** con texto diminuto. | `font-size` en `scene_template.html`: 141 reglas ≤ 13 px, mínimo 9 px; `muted` en los 9 `<video>`; 0 `<track>`. | 9 videos (Diapos 5, 7, 9, 10, 19, 21, 26, 27, 29) |
| **D6** | **Pipeline de video no reproducible en Windows y duplicado.** `capture.mjs` idéntico en las 9 carpetas (mismo md5), `render.sh` usa `.venv/bin/python`, `/tmp` y `spawn("chromium")`; `ffmpeg` no está en PATH. 3 MP4 legacy versionados (`anatomia_senal_v1/v2/v3`, ~8 MB). | md5 único ×9; 9/9 `render.sh` con rutas Linux; `git ls-files video | grep _v` = 3. | `video/**` |
| **D7** | **Apertura poco profesional.** La misma foto de la iglesia se repite en 6 diapos (1, 4, 18, 24, 28, 30); Diapo 2 (ponente) deja ~60 % vacío; Diapo 3 (agenda) son 5 cajas enormes con 1 línea cada una. | Capturas 01–04, 18, 24, 28, 30. | 1, 2, 3, 4, 18, 24, 28, 30 |
| **D8** | **Cierre denso.** Diapo 29 presenta 3 columnas de 7 bloques con "axiomas", "evidencia" y "regla operativa"; el público no retiene 21 ítems. | Captura 29: 3 × 7 bloques, 190 palabras. | 29 |

---

## [/] Fase 12 — Claridad Pedagógica para Audiencia No Estadística y Pulido Profesional de Deck y Videos

- **Objetivo:** Convertir el deck y los 9 videos en una charla que una persona **sin estadística** entienda y recuerde: una idea por pantalla, jerga traducida en el momento (glosario emergente + analogías), cifras con significado cotidiano, jerarquía visual donde el mensaje es el titular, videos legibles a 5 m con subtítulos, y un pipeline de video reproducible en Windows/Linux con un solo comando.
- **Entregable global:** `front/deck_glossary.py` + inyector de tooltips en `front/prototype_engine.py`, los 21 prototipos reescritos en lenguaje llano (titular = Idea Clave, ≤ 3 etapas, taxonomía única), apertura/secciones/cierre rediseñados, 9 videos re-renderizados con tipografía ≥ 22 px, subtítulos quemados y pista `.vtt`, pipeline unificado `video/_pipeline/`, validador `scripts/audit_f12_claridad.py` en verde, y bundles `presentacion.html` / `index.html` recompilados y verificados en 1920×1080 y 1366×768.
- **AC global de la Fase:**
  - [ ] Cada uno de los 21 prototipos tiene ≤ 25 términos técnicos sin tooltip y cada término del glosario muestra definición ≤ 15 palabras + analogía al pasar el mouse / tocar.
  - [ ] Ninguna cifra visible tiene más de 1 decimal (salvo tablas marcadas `data-expert`), y cada cifra de error/correlación/p-valor va acompañada de una frase en lenguaje llano.
  - [ ] El titular de cada prototipo es la Idea Clave (≤ 12 palabras, verbo + resultado) legible a 5 m (≥ 34 px en 1080p); máximo 3 etapas por diapo en la "ruta corta"; 0 botones *"Pase a Diapo"*.
  - [ ] Los 9 videos tienen tipografía mínima ≥ 22 px (1600×900), gráfico ≥ 60 % del lienzo, subtítulos quemados por beat y `narration.vtt`; `python video/_pipeline/render.py <carpeta>` regenera cualquier MP4 en Windows y Linux.
  - [ ] Prueba de comprensión con 3 personas no estadísticas: ≥ 4/5 respuestas correctas cada una; ensayo cronometrado de la ruta corta ≤ 35 min.
- **Tests de la Fase:**
  - **Test Unitario:** `scripts/audit_f12_claridad.py` (jerga sin tooltip ≤ 25 por prototipo, Idea Clave ≤ 12 palabras, 0 cifras con ≥ 2 decimales fuera de `data-expert`, 0 botones de navegación interna, `font-size` mínimo ≥ 22 px en `scene_template.html`, existencia de `narration.vtt` y `subtitles` por video, `capture.mjs` único en `video/_pipeline/`).
  - **Test de Simulación de Usuario:** Recorrido Chromium headless en 1920×1080 y 1366×768 sobre las 30 diapos: hover sobre 3 términos por prototipo muestra tooltip, titular ≥ 34 px, `scrollHeight <= clientHeight + 2`, 0 errores de consola; reproducción de cada video gate con `<track>` activo y captura de 3 keyframes por video reescalados al 25 % (simulación de 5 m) con OCR legible; cuestionario de comprensión con 3 personas.

---

### [X] SF12.1 — Capa de Traducción: Glosario Emergente, Analogías y Cifras con Significado

- **Objetivo:** Que ningún término ni cifra quede sin traducción para el público general, sin borrar el rigor (el detalle experto se conserva en tooltip o en bloques `data-expert`).
- **Entregable:** `front/deck_glossary.py` (≤ 40 términos), inyector en `front/prototype_engine.py`, `front/deck_plain_numbers.py` (tabla cifra → frase) y los 21 prototipos con tooltips y frases llanas.
- **AC de la Sub fase:**
  - [ ] 100 % de los términos del inventario de `T12.1.1` tienen entrada en el glosario y tooltip visible en los prototipos.
  - [ ] Cada bloque con RMSE/MAE/r/p/cuantil muestra la frase llana equivalente al lado de la cifra.
- **Tests de la Sub fase:**
  - **Test Unitario:** `audit_f12_claridad.py --glosario` compara el inventario de jerga contra `deck_glossary.py` y falla si hay término sin definición o definición > 15 palabras.
  - **Test de Simulación de Usuario:** Playwright hace `hover` sobre `.gl-term` en cada prototipo y verifica `tooltip.isVisible()` y texto no vacío en 1366×768.

#### [X] T12.1.1 — Inventario de Jerga y Glosario Central (`front/deck_glossary.py`)
- **Objetivo de la Tarea:** Extraer automáticamente los términos técnicos de los 21 prototipos, consolidarlos en ≤ 40 entradas con definición ≤ 15 palabras + analogía cotidiana, y fijar el umbral de jerga por prototipo.
- **Entregable:** `front/deck_glossary.py` (dict `GLOSSARY = {termino: {"def": ..., "analogia": ...}}`) y `scripts/audit_f12_claridad.py --inventario` que imprime el conteo por prototipo.

> **🧠 Explicación:** El público no estadístico abandona la lectura al segundo término que no entiende (efecto "carga extraña" de Sweller). Un glosario central evita 21 definiciones divergentes y permite que el compilador inyecte la misma explicación en cualquier prototipo actual o futuro. La analogía (p-valor alto = "empate técnico, como dos corredores que llegan al mismo tiempo") es lo que la gente recuerda; la definición formal queda para el experto que la quiera leer.

> **💡 Cómo hacerlo (ejemplo):**
> ```python
> # front/deck_glossary.py
> GLOSSARY = {
>     "p-valor": {"def": "Probabilidad de ver esa diferencia solo por azar.",
>                 "analogia": "p > 0.05 = empate técnico entre dos corredores."},
>     "RMSE": {"def": "Error típico del pronóstico en las unidades del dato.",
>              "analogia": "RMSE 1.9 °C ≈ la precisión de un termómetro de farmacia."},
>     "holdout": {"def": "Datos finales que el modelo nunca vio al entrenar.",
>                 "analogia": "El examen final con preguntas nuevas."},
> }
> ```
> ```bash
> python scripts/audit_f12_claridad.py --inventario   # jerga por prototipo y términos sin glosario
> ```

- **AC de la Tarea:**
  - [ ] Glosario con ≤ 40 entradas, todas con `def` ≤ 15 palabras y `analogia` no vacía.
  - [ ] El inventario cubre los 21 prototipos y lista 0 términos huérfanos.
- **Tests de la Tarea:**
  - **Test Unitario:** `pytest`-style assert en `audit_f12_claridad.py`: cada entrada cumple longitud; términos del inventario ⊆ claves del glosario.
  - **Test de Simulación de Usuario:** Lectura en voz alta de 10 analogías a 1 persona no estadística; ≥ 8/10 explicadas de vuelta correctamente (registro en bitácora).

#### [X] T12.1.2 — Inyector Automático de Tooltips en `front/prototype_engine.py`
- **Objetivo de la Tarea:** Que el compilador envuelva cada término del glosario presente en el HTML visible de un prototipo en `<span class="gl-term" data-def data-analogia>` con tooltip CSS puro (sin JS adicional), y lo haga para cualquier HTML futuro.
- **Entregable:** Función `inject_glossary(html, glossary)` en `front/prototype_engine.py`, CSS `.gl-term` + `.gl-tip` en el tema maestro, llamada desde `back/build_deck.py`.

> **🧠 Explicación:** Inyectar en compilación (y no editar 21 archivos a mano) garantiza consistencia y cero drift: si cambia una definición, se recompila. Se evita tocar `<script>`, `<style>`, atributos y nodos ya marcados; solo la primera aparición por etapa se marca para no llenar la pantalla de subrayados. Tooltip CSS (`:hover`/`:focus-visible`) funciona offline y con teclado (accesibilidad básica).

> **💡 Cómo hacerlo (ejemplo):**
> ```python
> import re, html as h
> def inject_glossary(doc: str, glossary: dict) -> str:
>     def mark(m):
>         t = m.group(0); e = glossary[t.lower()]
>         return (f'<span class="gl-term" tabindex="0" data-def="{h.escape(e["def"])}" '
>                 f'data-analogia="{h.escape(e["analogia"])}">{t}</span>')
>     pat = re.compile(r'(?<![\w-])(' + '|'.join(map(re.escape, glossary)) + r')(?![\w-])', re.I)
>     # ponytail: solo texto fuera de <script>/<style>; primera aparición por bloque .stage
>     parts = re.split(r'(<script.*?</script>|<style.*?</style>|<[^>]+>)', doc, flags=re.S)
>     return ''.join(p if p.startswith('<') else pat.sub(mark, p, count=1) for p in parts)
> ```
> ```css
> .gl-term{border-bottom:1px dotted var(--accent);cursor:help;position:relative}
> .gl-term:hover::after,.gl-term:focus-visible::after{content:attr(data-def) " · " attr(data-analogia);
>   position:absolute;left:0;top:1.4em;z-index:50;max-width:36ch;padding:.5em .7em;font-size:.8em;
>   background:var(--panel);border:1px solid var(--accent);border-radius:8px;white-space:normal}
> ```

- **AC de la Tarea:**
  - [ ] Recompilar con `python back/build_deck.py` deja ≥ 1 `.gl-term` por prototipo y 0 dentro de `<script>`/`<style>`/atributos.
  - [ ] Tooltip visible en hover y con teclado (Tab + foco), sin recorte en bordes de pantalla.
- **Tests de la Tarea:**
  - **Test Unitario:** Test de `inject_glossary` con un HTML de 10 líneas (término en texto, en `<script>`, en atributo) → solo el del texto queda marcado.
  - **Test de Simulación de Usuario:** Playwright: `hover` y `focus` sobre 3 `.gl-term` por prototipo en 1366×768; `boundingBox` del tooltip dentro del viewport.

#### [X] T12.1.3 — Reescritura en Lenguaje Llano de Titulares, Leads e Ideas Clave (21 prototipos)
- **Objetivo de la Tarea:** Reescribir en cada prototipo el titular de cada etapa, el párrafo `lead` y la `💡 Idea Clave` con la regla "verbo + resultado, sin siglas, ≤ 12 palabras el titular / ≤ 22 el lead", conservando las cifras canónicas auditadas (F3, F4, F11).
- **Entregable:** 21 prototipos reescritos + `front/deck_notes.py` sincronizado (las versiones técnicas de las frases van a las notas del ponente).

> **🧠 Explicación:** El titular es lo único que lee una persona desde la fila 10. *"Cuantil Local vs. Global y la Victoria Zero-Shot en ERCOT"* no comunica nada al público general; *"Un modelo que nunca vio Texas acertó mejor que el entrenado allí"* sí. El rigor no se pierde: la formulación técnica se mueve a tooltip o a las notas `[N]`. Las cifras no se tocan (DoD 3: integridad de datos reales).

> **💡 Cómo hacerlo (ejemplo):**
> ```text
> ANTES (Diapo 15): "Benchmark de 14 modelos: Tierra (CPU) vs. Supercómputo"
> DESPUÉS:          "14 modelos compitieron: ganó el más simple y barato"
> ANTES (Diapo 10 · Idea Clave): "Zero-Shot regala el 80 % de la historia a la calibración conforme para blindar intervalos."
> DESPUÉS:                       "Un pronóstico honesto da un rango, no un número."
> ```
> ```bash
> python scripts/audit_f12_claridad.py --titulares   # falla si titular > 12 palabras o contiene sigla sin glosario
> ```

- **AC de la Tarea:**
  - [ ] 100 % de titulares ≤ 12 palabras y 100 % de leads ≤ 22 palabras; 0 siglas fuera del glosario.
  - [ ] Todas las cifras canónicas (38.0 °C, 2,557 días, 1.880 °C, −56 %, r = 0.75, 4.51 qq/ha, etc.) siguen presentes y sin alterar.
- **Tests de la Tarea:**
  - **Test Unitario:** `audit_f12_claridad.py --titulares` + comparación de cifras canónicas contra `data/caso_1/benchmark_punchana.csv`, `data/caso_2/cafe_jaen_hipotesis.json`.
  - **Test de Simulación de Usuario:** Lectura de los 21 titulares a 2 personas no estadísticas: cada una explica en una frase qué dice ≥ 18/21 diapos.

#### [X] T12.1.4 — Cifras con Significado: Tabla Canónica Cifra → Frase (`front/deck_plain_numbers.py`)
- **Objetivo de la Tarea:** Para cada cifra de error, correlación, p-valor o cuantil visible, mostrar al lado una frase cotidiana equivalente y reducir a 1 decimal lo visible (el valor completo queda en `title`/tooltip o en bloques `data-expert`).
- **Entregable:** `front/deck_plain_numbers.py` (`PLAIN = {"rmse_extratrees": ("1.9 °C", "como un termómetro de farmacia"), ...}`) inyectado por `build_deck.py` en los prototipos de las Diapos 10, 13–16, 26, 27 y 29.

> **🧠 Explicación:** "RMSE 1.880 °C, p = 0.918" no significa nada para un agricultor o un gerente; "se equivoca ±2 °C, igual que el termómetro de tu casa; los dos modelos empatan" sí. La tabla centralizada evita cifras cableadas a mano (regla de F5) porque cada entrada referencia la fuente CSV/JSON y se verifica en test.

> **💡 Cómo hacerlo (ejemplo):**
> ```python
> # front/deck_plain_numbers.py
> PLAIN = {
>   "rmse_extratrees": {"src": "data/caso_1/benchmark_punchana.csv#ExtraTrees.rmse_1d",
>                       "show": "±1.9 °C", "plain": "como el termómetro de tu casa"},
>   "dm_p_timesfm":    {"src": "data/caso_1/benchmark_punchana.csv#TimesFM.dm_p",
>                       "show": "p = 0.7", "plain": "empate técnico"},
>   "roya_caida":      {"src": "data/caso_2/cafe_jaen_hipotesis.json#H4.caida_pct",
>                       "show": "−56 %", "plain": "la mitad de la cosecha desapareció y el satélite no lo vio"},
> }
> ```

- **AC de la Tarea:**
  - [ ] 0 cifras visibles con ≥ 2 decimales fuera de `data-expert`.
  - [ ] Cada entrada de `PLAIN` coincide con su fuente (tolerancia de redondeo a 1 decimal).
- **Tests de la Tarea:**
  - **Test Unitario:** Test que carga `PLAIN`, lee cada `src` y compara el valor redondeado con `show`.
  - **Test de Simulación de Usuario:** Captura de las Diapos 13, 15, 16, 26 y 27 en 1366×768: cada bloque de cifra muestra la frase llana sin solape (Playwright + inspección visual).

---

### [/] SF12.2 — Jerarquía Visual y Ritmo: Una Idea por Pantalla

- **Objetivo:** Que el mensaje sea el titular, que haya como máximo 3 etapas por diapo en la ruta por defecto, una sola taxonomía de nombres, y una apertura/cierre con aspecto profesional y variado.
- **Entregable:** 18 prototipos con cabecera "hero" (Idea Clave arriba), ruta corta/experta en `prototype_engine.py`, Diapos 1–4, 18, 24, 28–30 rediseñadas, 0 botones de navegación interna.
- **AC de la Sub fase:**
  - [ ] Titular ≥ 34 px en 1080p en los 18 prototipos; etapas visibles por defecto ≤ 3.
  - [ ] Una sola taxonomía: `Acto N · Diapo M` (sin "VÍA", "Era", "Pilar", "Etapa X de 4" en cabeceras).
- **Tests de la Sub fase:**
  - **Test Unitario:** `audit_f12_claridad.py --jerarquia` (regex de taxonomías prohibidas; conteo de `.stage[data-route="corta"]` ≤ 3; 0 `button:contains("Pase a")`).
  - **Test de Simulación de Usuario:** Playwright mide `getComputedStyle(h1).fontSize` ≥ 34 px y recorre la ruta corta completa con `→` en ≤ 54 pulsaciones (30 diapos + etapas).

#### [ ] T12.2.1 — Cabecera "Hero": la Idea Clave como Titular y Taxonomía Única
- **Objetivo de la Tarea:** Mover la `💡 Idea Clave` al tope de cada prototipo como titular grande (≥ 34 px), degradar el título técnico a subtítulo, y normalizar la cabecera a `Acto N · Diapo M · <tema>` desde `prototype_engine.py`.
- **Entregable:** Regla de transformación en `prototype_engine.py` (`promote_takeaway_to_hero`) + CSS `.hero-title` en el tema maestro; 18 prototipos recompilados.

> **🧠 Explicación:** Hoy el ojo cae primero en "VÍA 3: Deep Learning y Parches · De LSTM y TFT a la Revolución PatchTST" y el mensaje útil ("agrupar días en bloques abarató 256× el cálculo") está al pie en 12 px. Invertir la jerarquía (mensaje arriba, nombre técnico abajo) es el cambio de mayor impacto por línea de código, y hacerlo en el compilador lo aplica a los 18 sin editar cada HTML.

> **💡 Cómo hacerlo (ejemplo):**
> ```python
> def promote_takeaway_to_hero(doc: str, acto: int, diapo: int) -> str:
>     take = re.search(r'class="executive-takeaway"[^>]*>(.*?)</', doc, re.S).group(1)
>     hero = (f'<header class="hero"><div class="hero-kicker">Acto {acto} · Diapo {diapo}</div>'
>             f'<h1 class="hero-title">{take}</h1></header>')
>     doc = re.sub(r'<header class="(?:sim-header|top-bar)[^>]*>.*?</header>', hero, doc, count=1, flags=re.S)
>     return re.sub(r'\b(VÍA|Era|Pilar|Etapa)\s+\d+( de \d+)?\b', '', doc)  # ponytail: taxonomías viejas fuera
> ```
> ```css
> .hero-title{font-size:clamp(28px,2.4vw,44px);line-height:1.1;font-weight:700;max-width:28ch}
> ```

- **AC de la Tarea:**
  - [ ] 18/18 prototipos con `.hero-title` ≥ 34 px en 1920×1080 y ≥ 28 px en 1366×768, sin desborde.
  - [ ] 0 coincidencias de taxonomías viejas en cabeceras.
- **Tests de la Tarea:**
  - **Test Unitario:** Test de `promote_takeaway_to_hero` sobre un fixture mínimo; regex de taxonomías = 0 en los 18 HTML compilados.
  - **Test de Simulación de Usuario:** Capturas `screenshots/f12_s{05..27}_{1366,1920}.png` y medición de `fontSize` con Playwright.

#### [ ] T12.2.2 — Ruta Corta (≤ 3 etapas) y Ruta Experta (tecla `D`)
- **Objetivo de la Tarea:** Marcar en cada prototipo qué etapas son esenciales (`data-route="corta"`, máx. 3) y cuáles son profundización (`data-route="experta"`); por defecto el deck recorre solo la ruta corta y la tecla `D` activa las etapas expertas.
- **Entregable:** Atributos `data-route` en los 18 prototipos, lógica en `prototype_engine.py` (filtra la barra de etapas) y `front/deck_slides_p*.py` (tecla `D` global), ensayo ≤ 35 min.

> **🧠 Explicación:** 72 pantallas en 35 min son 29 s por pantalla: imposible de digerir para no expertos. Reducir a ≤ 54 pantallas por defecto, sin borrar el contenido experto, respeta a ambos públicos. El filtro vive en el compilador para no mantener dos versiones de cada HTML.

> **💡 Cómo hacerlo (ejemplo):**
> ```html
> <!-- en el prototipo -->
> <section class="stage" data-route="corta">…</section>
> <section class="stage" data-route="experta">…</section>
> ```
> ```js
> // deck: tecla D alterna ruta
> document.addEventListener('keydown', e => { if (e.key === 'd' || e.key === 'D')
>   document.documentElement.toggleAttribute('data-expert'); });
> ```
> ```css
> html:not([data-expert]) .stage[data-route="experta"], html:not([data-expert]) .stage-tab[data-route="experta"]{display:none}
> ```

- **AC de la Tarea:**
  - [ ] Ruta corta: ≤ 3 etapas por prototipo, ≤ 54 pantallas totales; tecla `D` muestra las expertas sin recompilar.
  - [ ] Ensayo cronometrado de la ruta corta ≤ 35 min (registro en `front/deck_notes.py` y bitácora).
- **Tests de la Tarea:**
  - **Test Unitario:** Conteo de `data-route="corta"` ≤ 3 por prototipo; el `postMessage` de etapas ignora las expertas cuando `data-expert` no está.
  - **Test de Simulación de Usuario:** Playwright recorre con `→` y cuenta pantallas; pulsa `D` y verifica que aparecen las etapas expertas de la Diapo 10.

#### [X] T12.2.3 — Apertura y Secciones Profesionales (Diapos 1–4, 18, 24, 28, 30)
- **Objetivo de la Tarea:** Un fondo distinto por acto (5 variantes del arte oficial: tonos/recortes, no la misma foto ×6), Diapo 2 con foto + 3 datos grandes + QR LinkedIn, Diapo 3 agenda con icono + frase de 1 línea + minutos por bloque, separadores con "pregunta del acto" como titular.
- **Entregable:** `front/deck_branding.py` con 5 fondos (`docs/images/front/bg_acto_{1..5}.jpg`, ≤ 300 KB c/u), `front/deck_slides_p1.py`/`p2.py` actualizados.

> **🧠 Explicación:** La repetición del mismo fondo en 6 diapos se percibe como plantilla sin terminar; variar tono/recorte por acto crea sensación de progreso. La agenda con minutos y una pregunta por bloque ("¿Puede un modelo barato ganarle a Google?") fija expectativas en lenguaje de la audiencia, no en jerga ("Foundation Models Zero-Shot").

> **💡 Cómo hacerlo (ejemplo):**
> ```python
> # front/deck_branding.py
> ACT_BG = {1: "bg_acto_1.jpg", 2: "bg_acto_2.jpg", 3: "bg_acto_3.jpg", 4: "bg_acto_4.jpg", 5: "bg_acto_5.jpg"}
> AGENDA = [  # (icono, pregunta en lenguaje llano, minutos)
>   ("📈", "¿Qué hay dentro de una serie de tiempo y qué modelos existen?", 12),
>   ("🌡️", "Caso 1 · ¿Puede un modelo barato ganarle a Google prediciendo el clima de Iquitos?", 8),
>   ("🌱", "¿Cómo pronosticaba el campo antes de la IA?", 6),
>   ("☕", "Caso 2 · ¿Ve el satélite la cosecha de café?", 6),
>   ("🧭", "¿Qué me llevo a casa?", 3),
> ]
> ```
> ```bash
> python -c "from PIL import Image, ImageEnhance; ..."  # generar 5 variantes de tono desde bg_cover_official.png
> ```

- **AC de la Tarea:**
  - [ ] 5 fondos distintos, cada uno ≤ 300 KB; agenda con minutos que suman 35.
  - [ ] Diapo 2 sin área vacía > 25 % del alto (medida con `scripts/pagina/audit_layout.py`).
- **Tests de la Tarea:**
  - **Test Unitario:** Test de tamaño de archivo y de suma de minutos en `AGENDA`.
  - **Test de Simulación de Usuario:** `scripts/pagina/audit_layout.py` sobre Diapos 1–4, 18, 24, 28, 30 (0 vacíos > 31 px) + capturas.

#### [ ] T12.2.4 — Retiro de Navegación Interna Duplicada y Cierre en 3 Frases (Diapos 5–27 y 29)
- **Objetivo de la Tarea:** Eliminar los botones *"Pase a Diapo N →"* / *"Ir a…"* de los prototipos (la navegación la lleva el deck con `→`), y rediseñar la Diapo 29 como 3 frases grandes (una por lección) con la evidencia de cada caso como subtítulo de 1 línea.
- **Entregable:** Regla `strip_internal_nav` en `prototype_engine.py`; Diapo 29 reescrita en `front/deck_slides_p2.py`.

> **🧠 Explicación:** Dos sistemas de navegación confunden al ponente en vivo y al público (¿qué pasa si hago clic?). En el cierre, 21 bloques no se recuerdan; 3 frases sí ("Respeta el tiempo", "El valor está en el rango", "Primero la física, luego el algoritmo").

> **💡 Cómo hacerlo (ejemplo):**
> ```python
> def strip_internal_nav(doc: str) -> str:
>     return re.sub(r'<button[^>]*>(?:Pase a|Ir a|Ver )[^<]*</button>', '', doc)
> ```
> ```html
> <section class="closing-3">
>   <h2>1 · Respeta el orden del tiempo</h2><p>Entrenar mirando el futuro da notas falsas. Iquitos: 2,557 días, examen ciego de 90.</p>
>   <h2>2 · El valor está en el rango, no en el número</h2><p>Un pronóstico honesto dice "entre 29 y 36 °C", no "32.7 °C".</p>
>   <h2>3 · Primero la física, después el algoritmo</h2><p>El satélite vio hojas verdes; la cosecha de Jaén cayó a la mitad.</p>
> </section>
> ```

- **AC de la Tarea:**
  - [ ] 0 botones de navegación interna en los 21 prototipos compilados.
  - [ ] Diapo 29 con 3 titulares ≥ 36 px y ≤ 60 palabras en total.
- **Tests de la Tarea:**
  - **Test Unitario:** Regex de botones = 0; conteo de palabras de la Diapo 29 ≤ 60.
  - **Test de Simulación de Usuario:** Recorrido con teclado `→` por las 30 diapos sin clics; captura de la Diapo 29 en ambas resoluciones.

---

### [/] SF12.3 — Videos Legibles a 5 m, Subtitulados y Pipeline Reproducible

- **Objetivo:** Que los 9 videos se lean desde el fondo del aula, cuenten su mensaje aunque no haya audio, y se regeneren con un solo comando en Windows o Linux desde un pipeline único.
- **Entregable:** `video/_pipeline/{capture.mjs,render.py,README.md}`, 9 `scene_template.html` con escala tipográfica de video, subtítulos quemados + `narration.vtt` por video, 9 MP4 re-renderizados, legacy MP4 fuera del repo.
- **AC de la Sub fase:**
  - [ ] `font-size` mínimo ≥ 22 px en los 9 `scene_template.html`; gráfico principal ≥ 60 % del lienzo.
  - [ ] `python video/_pipeline/render.py video/seccion_1/diapo_10/video_cono_incertidumbre` produce el MP4 en Windows y Linux; 1 solo `capture.mjs` en el repo.
- **Tests de la Sub fase:**
  - **Test Unitario:** `audit_f12_claridad.py --video` (font-size mínimo, existencia de `narration.vtt` y `subs` en template, md5 único de `capture.mjs`, 0 `*_v[0-9]*.mp4` versionados).
  - **Test de Simulación de Usuario:** Render completo de un video en Windows + `ffprobe` (1920×1080, 30 fps, 900 frames) + 3 keyframes reescalados al 25 % con OCR (`pytesseract` o inspección) legibles.

#### [ ] T12.3.1 — Escala Tipográfica de Video y Lienzo al 60 % (9 `scene_template.html`)
- **Objetivo de la Tarea:** Subir toda la tipografía de las escenas a mínimo 22 px (etiquetas) / 30 px (subtítulos de panel) / 64 px (titulares) en 1600×900, y ampliar el gráfico principal para ocupar ≥ 60 % del lienzo, re-renderizando los 9 MP4.
- **Entregable:** 9 `scene_template.html` con tokens CSS `--fs-label: 22px; --fs-sub: 30px; --fs-title: 64px` y layout del panel a ≥ 60 %.

> **🧠 Explicación:** Un texto de 12 px en 1600×900 proyectado en una pantalla de 4 m se ve de ~1 cm de alto a 10 m: invisible. La regla práctica de auditorio es ≥ 1/40 del alto del lienzo para etiquetas (22 px) y ≥ 1/14 para titulares (64 px). El gráfico pequeño centrado desperdicia el 60 % del lienzo en negro.

> **💡 Cómo hacerlo (ejemplo):**
> ```css
> :root{--fs-label:22px;--fs-sub:30px;--fs-title:64px}
> .pill,.panelHead .pk{font-size:var(--fs-label)}  .panelHead .ps,#cs{font-size:var(--fs-sub)}  #ch,#lawBig{font-size:var(--fs-title)}
> #panel{left:80px;top:140px;width:1440px;height:640px}  /* ≥ 60 % del lienzo 1600×900 */
> ```
> ```bash
> python video/_pipeline/render.py video/seccion_1/diapo_10/video_cono_incertidumbre
> ```

- **AC de la Tarea:**
  - [ ] `grep font-size` en los 9 templates: mínimo ≥ 22 px; panel principal ≥ 60 % del área.
  - [ ] 9 MP4 regenerados con `ffprobe` 1920×1080 @ 30 fps y cifras canónicas intactas.
- **Tests de la Tarea:**
  - **Test Unitario:** `audit_f12_claridad.py --video` falla ante `font-size` < 22 px.
  - **Test de Simulación de Usuario:** Keyframes `t = 8, 16, 24 s` reescalados al 25 % (simula 5 m) con texto legible; revisión en pantalla del aula si es posible.

> ⟳ Ajustado en SF12.1 — el deck se abre por `file://` y Chrome bloquea `<track src="*.vtt">` por CORS: el `<track>` debe llevar el VTT como `data:text/vtt;base64,…` (generado en `build_deck.py` desde `narration.vtt`), no una ruta.

#### [ ] T12.3.2 — Subtítulos por Beat Quemados en la Escena y Pista `narration.vtt`
- **Objetivo de la Tarea:** Cada video muestra 1 frase ≤ 10 palabras por beat (banda inferior, 30 px, fondo semitransparente) generada desde `beats.json` en `build_scene.py`, y exporta `narration.vtt` con los mismos tiempos para `<track kind="subtitles">` en el deck; opcionalmente `narration.mp3` (grabación del ponente) muxeado por `render.py`.
- **Entregable:** `beats.json` + banda `#subs` en los 9 templates, `narration.vtt` por video, `<track>` en los 9 `<video>` de `front/deck_slides_p*.py`.

> **🧠 Explicación:** Un video mudo con texto diminuto es 30 s de confusión. El subtítulo por beat convierte cada video en una micro-historia de 4 frases que cualquiera sigue; `beats.json` es la única fuente de verdad (escena y `.vtt` se generan de él, cero drift). El audio es opcional porque muchas aulas no tienen sonido fiable.

> **💡 Cómo hacerlo (ejemplo):**
> ```json
> [{"t":0.4,"dur":6,"text":"Esta es la temperatura real de Iquitos, día a día"},
>  {"t":8,"dur":8,"text":"Un pronóstico de un solo número siempre falla"},
>  {"t":17,"dur":8,"text":"Un rango honesto acertó 5 de 7 días"},
>  {"t":26,"dur":4,"text":"El valor está en la banda, no en el punto"}]
> ```
> ```python
> # build_scene.py
> beats = json.loads((SRC/"beats.json").read_text(encoding="utf-8"))
> vtt = "WEBVTT\n\n" + "\n\n".join(f"{ts(b['t'])} --> {ts(b['t']+b['dur'])}\n{b['text']}" for b in beats)
> (SRC/"narration.vtt").write_text(vtt, encoding="utf-8")
> html = html.replace("__BEATS_JSON__", json.dumps(beats, ensure_ascii=False))
> ```
> ```html
> <video …><track kind="subtitles" src="video/…/narration.vtt" srclang="es" default></video>
> ```

- **AC de la Tarea:**
  - [ ] 9 `beats.json` (3–5 beats, ≤ 10 palabras c/u); 9 `narration.vtt` válidos; subtítulo visible en todos los keyframes.
  - [ ] Los 9 `<video>` del deck llevan `<track … default>` y el gate muestra subtítulos.
- **Tests de la Tarea:**
  - **Test Unitario:** Validación de `beats.json` (longitud, solapes de tiempo) y de sintaxis `WEBVTT`.
  - **Test de Simulación de Usuario:** Playwright reproduce el gate de la Diapo 5 y verifica `video.textTracks[0].activeCues.length ≥ 1` a `t = 10 s`.

#### [X] T12.3.3 — Pipeline Único y Portable (`video/_pipeline/render.py` + `capture.mjs`)
- **Objetivo de la Tarea:** Reemplazar los 9 `render.sh` + 9 `capture.mjs` idénticos por `video/_pipeline/capture.mjs` (usa el Chromium de Playwright) y `video/_pipeline/render.py` (Python, cross-platform, `tempfile`, `ffmpeg` desde PATH o `imageio-ffmpeg`), y sacar del repo los MP4 legacy.
- **Entregable:** `video/_pipeline/{capture.mjs,render.py,README.md}`, 9 carpetas sin `render.sh`/`capture.mjs`, `.gitignore` con `video/**/*_v[0-9]*.mp4`, `git rm` de los 3 legacy.

> **🧠 Explicación:** 9 copias idénticas de un script son 9 lugares donde arreglar el mismo bug; además `.venv/bin/python`, `/tmp` y `spawn("chromium")` solo existen en Linux, así que hoy el pipeline no corre en la máquina Windows del ponente. Un `render.py` que recibe la carpeta y lee un `video.json` mínimo (`fps`, `dur_ms`, `start_ms`, `time_scale`, `dpr`, `bg`) es más corto que los 9 `.sh` juntos.

> **💡 Cómo hacerlo (ejemplo):**
> ```python
> # video/_pipeline/render.py  — uso: python video/_pipeline/render.py <carpeta_video>
> import json, shutil, subprocess, sys, tempfile, pathlib
> d = pathlib.Path(sys.argv[1]).resolve(); cfg = json.loads((d/"video.json").read_text())
> ffmpeg = shutil.which("ffmpeg") or __import__("imageio_ffmpeg").get_ffmpeg_exe()
> subprocess.check_call([sys.executable, d/"build_scene.py"])
> with tempfile.TemporaryDirectory() as fr:
>     subprocess.check_call(["node", pathlib.Path(__file__).with_name("capture.mjs"), d/"scene.html", fr,
>                            *map(str, (cfg["fps"], cfg["dur_ms"], cfg.get("start_ms",0), cfg.get("time_scale",1), cfg.get("dpr",1.2)))])
>     subprocess.check_call([ffmpeg, "-y", "-loglevel", "error", "-framerate", str(cfg["fps"]), "-i", f"{fr}/f%05d.png",
>                            "-vf", f"fade=t=in:st=0:d=0.35:color={cfg['bg']}", "-c:v", "libx264", "-preset", "slow",
>                            "-crf", "18", "-pix_fmt", "yuv420p", "-movflags", "+faststart", d/cfg["out"]])
> ```
> ```js
> // capture.mjs: ruta del Chromium de Playwright en vez de spawn("chromium")
> import { chromium } from "playwright";  // ya instalado en el repo
> const browser = await chromium.launch({ args: ["--force-device-scale-factor=1"] });
> ```

- **AC de la Tarea:**
  - [ ] `python video/_pipeline/render.py <carpeta>` regenera cualquiera de los 9 MP4 en Windows (sin WSL) y en Linux; md5 del MP4 estable entre dos corridas (determinismo).
  - [ ] 1 solo `capture.mjs` en el repo; 0 `render.sh`; 0 MP4 `_v[0-9]` versionados.
- **Tests de la Tarea:**
  - **Test Unitario:** `test_render_pipeline.py`: `video.json` válido en las 9 carpetas; `capture.mjs` único; `ffmpeg` resoluble.
  - **Test de Simulación de Usuario:** Render de `video_cono_incertidumbre` en Windows + `ffprobe` (1920×1080, 30 fps, 900 frames) y comparación de hash entre 2 corridas.

---

### [/] SF12.4 — Validación con Audiencia No Estadística, Compilación y Cierre

- **Objetivo:** Demostrar con evidencia (no con opinión) que el deck se entiende sin estadística, dejar el validador automático en verde y los bundles recompilados.
- **Entregable:** `scripts/audit_f12_claridad.py` completo, cuestionario y resultados en `docs/reference/fases/fase_12_claridad_no_estadistica_deck_videos.md` §3, `presentacion.html`/`index.html` recompilados, bitácora.
- **AC de la Sub fase:**
  - [ ] Validador en verde en los 7 modos (`--inventario --glosario --titulares --jerarquia --cifras --video --all`).
  - [ ] 3 personas no estadísticas: ≥ 4/5 aciertos cada una; ensayo ruta corta ≤ 35 min.
- **Tests de la Sub fase:**
  - **Test Unitario:** `python scripts/audit_f12_claridad.py --all` → exit 0.
  - **Test de Simulación de Usuario:** Recorrido completo Chromium 1920×1080 y 1366×768 + cuestionario presencial.

#### [X] T12.4.1 — Validador `scripts/audit_f12_claridad.py`
- **Objetivo de la Tarea:** Un solo script con subcomandos que materializa todos los tests unitarios de la Fase (jerga, glosario, titulares, jerarquía, cifras, video, pipeline) y devuelve exit code 1 ante cualquier fallo.
- **Entregable:** `scripts/audit_f12_claridad.py` (stdlib + `re` + `json`; reutiliza patrones de `scripts/audit_f10_layout_typography.py`).

> **🧠 Explicación:** Sin validador, la claridad se degrada en el siguiente ajuste "rápido". Un script determinista permite que `construir` y `verificar-dod` cierren cada Tarea con evidencia y que el Test de Fase sea un comando.

> **💡 Cómo hacerlo (ejemplo):**
> ```bash
> python scripts/audit_f12_claridad.py --all
> # [OK] jerga sin tooltip ≤ 25 en 21/21   [OK] titulares ≤ 12 palabras   [OK] 0 cifras ≥ 2 decimales
> # [OK] 0 botones 'Pase a'                [OK] video font-size ≥ 22 px    [OK] capture.mjs único
> ```

- **AC de la Tarea:**
  - [ ] Los 7 subcomandos existen, corren en < 10 s y fallan ante un fixture roto.
- **Tests de la Tarea:**
  - **Test Unitario:** Fixture HTML con 1 violación por regla → cada subcomando devuelve exit 1.
  - **Test de Simulación de Usuario:** Corrida `--all` sobre el repo compilado en verde, salida registrada en la bitácora.

#### [ ] T12.4.2 — Prueba de Comprensión con 3 Personas No Estadísticas y Ensayo Cronometrado
- **Objetivo de la Tarea:** Presentar la ruta corta a 3 personas sin estadística (ideal: 1 agrónomo, 1 administrativo, 1 estudiante de otra carrera), aplicar un cuestionario de 5 preguntas de comprensión y cronometrar.
- **Entregable:** Cuestionario y resultados en §3 de este documento; ajustes de guion en `front/deck_notes.py`.

> **🧠 Explicación:** La única prueba válida de "se entiende sin estadística" es que alguien sin estadística lo explique de vuelta. Cinco preguntas tipo "¿Por qué el satélite no vio la caída del café?" discriminan si el mensaje llegó.

> **💡 Cómo hacerlo (ejemplo):**
> ```text
> Q1 ¿Qué significa que dos modelos "empaten"?             (esperado: no se distingue cuál es mejor; el azar explica la diferencia)
> Q2 ¿Por qué un pronóstico debe dar un rango y no un número?
> Q3 ¿Qué modelo ganó en Iquitos y por qué eso importa?     (el simple/barato; no hace falta supercómputo)
> Q4 ¿Por qué el satélite no vio la crisis de la roya?      (hojas verdes arriba, sin grano abajo)
> Q5 ¿Qué harías mañana si tienes una sola serie corta?     (modelo simple, validar en orden de tiempo)
> ```

- **AC de la Tarea:**
  - [ ] 3/3 participantes con ≥ 4/5; tiempo total ≤ 35 min; hallazgos registrados.
- **Tests de la Tarea:**
  - **Test Unitario:** Hoja de resultados (`docs/reference/fases/...md` §3) con 3 filas completas y puntajes.
  - **Test de Simulación de Usuario:** La propia sesión presencial cronometrada (drawer `[N]` con temporizador).

#### [ ] T12.4.3 — Compilación Final, Auditoría Multi-Resolución y Bitácora
- **Objetivo de la Tarea:** Recompilar `presentacion.html` e `index.html`, correr `audit_f10_layout_typography.py` + `audit_f12_claridad.py --all`, generar capturas `screenshots/f12_*` y registrar la Fase en la bitácora y en los espejos (`plan_maestro.md`, `tareas.md`, `README.md`).
- **Entregable:** Bundles recompilados, 60 capturas (30 diapos × 2 resoluciones), entrada en `docs/logs/log.md`, estado `[X]` en espejos.

> **🧠 Explicación:** El cierre formal (DoD global, Apéndice A) exige que ambos validadores estén en verde y que la documentación refleje el estado real; sin este paso el roll-up de `tareas.md` queda falso.

> **💡 Cómo hacerlo (ejemplo):**
> ```bash
> python back/build_deck.py && python scripts/audit_f10_layout_typography.py && python scripts/audit_f12_claridad.py --all
> python scripts/pagina/take_screenshots.py   # ajustar lista a 1..30 y a 1366×768 / 1920×1080
> ```

- **AC de la Tarea:**
  - [ ] Ambos validadores en verde; 0 errores de consola; capturas generadas; espejos actualizados.
- **Tests de la Tarea:**
  - **Test Unitario:** Exit 0 de los dos validadores.
  - **Test de Simulación de Usuario:** Recorrido Playwright de 30 diapos en 2 resoluciones con 0 errores de consola y `scrollHeight <= clientHeight + 2`.

---

## 3. Resultados de la Prueba de Comprensión (se completa en T12.4.2)

| Participante (perfil) | Q1 | Q2 | Q3 | Q4 | Q5 | Total | Observaciones |
|---|---|---|---|---|---|---|---|
| P1 (pendiente) | | | | | | /5 | |
| P2 (pendiente) | | | | | | /5 | |
| P3 (pendiente) | | | | | | /5 | |

**Duración del ensayo (ruta corta):** pendiente · **Meta:** ≤ 35 min.
