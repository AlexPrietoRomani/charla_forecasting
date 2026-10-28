# Fase 11: Videos Deterministas por Diapositiva (Pipeline Offline + Estructura `video/`)

> **Documento de Fase:** `docs/task/fases/fase_11_videos_por_diapositiva.md`
> **Estructura de salida:** `video/seccion_{N}/diapo_{M}/video_{nombre}/` (escena + capturador + fuentes + MP4)
> **Herramientas locales:** Chromium headless (CDP) + Node ≥ 22 + ffmpeg (sin dependencias externas ni red)
> **Skill de apoyo:** `motion-design` (LottieFiles) instalada en `.opencode/skills/motion-design/`
> **Estado:** `[/] En progreso` — piloto Diapo 5 completado (18 de octubre de 2026)

---

## 1. Objetivo

Producir **videos explicativos deterministas** (repetición exacta frame a frame) para reemplazar o acompañar zonas visuales de cualquier diapositiva del deck, con todo el material fuente versionado junto al video para poder re-renderizarlo en un comando. Sin servicios externos, sin dependencias npm/pip adicionales para el render.

## 2. Arquitectura del Pipeline

```mermaid
flowchart LR
    A["Datos reales (data/caso_1)"] --> B["build_scene.py<br/>descomposición + escena"]
    B --> C["scene.html<br/>(autocontenida, fonts embebidas)"]
    C --> D["capture.mjs<br/>CDP: __setTime(ms) + screenshot"]
    D --> E["900 PNG 1600×900"]
    E --> F["ffmpeg<br/>H.264 CRF 18 yuv420p +faststart"]
    F --> G["video_NOMBRE.mp4"]
```

- **Determinismo:** la escena expone `window.__setTime(ms)`; toda la animación es función pura del tiempo (sin `Date.now()` ni azar), por lo que dos renders del mismo `scene.html` son idénticos.
- **Recorte y estirado sin re-editar la escena:** `capture.mjs` acepta `startMs` y `timeScale`; el video final puede conservar un tramo (`[start, start + dur×scale]`) y alargarlo sin tocar los keyframes.
- **Formatos estándar:** 1920×1080 @ 30 fps (escena diseñada a 1600×900 y capturada con `dpr 1.2`), H.264 CRF 18, `yuv420p`, `+faststart` (compatible con navegador y con iframes del deck).

## 3. Estructura de Carpetas

```
video/
└── seccion_1/
    └── diapo_5/
        └── video_anatomia_senal/
            ├── build_scene.py        # datos → scene.html
            ├── scene_template.html   # diseño/animación (placeholders)
            ├── scene.html            # escena autocontenida generada
            ├── capture.mjs           # CDP → frames PNG
            ├── render.sh             # un comando: build + capture + encode
            ├── fonts/                # woff2 embebidas en la escena
            ├── anatomia_senal.mp4            # versión vigente
            └── (versiones anteriores retiradas en F12; ver sección 5)
```

Reglas: **ningún video vive en `docs/`**; cada video es dueño de sus fuentes; el MP4 final queda al lado de su escena, no en un directorio global.

## 4. Proceso por Video (Checklist)

1. **Brief:** diapositiva objetivo, zona a reemplazar, duración, mensaje único.
2. **Motion design:** aplicar `motion-design` (personalidad, easings direccionales, 3 capas de movimiento, regla 1/3, stagger) antes de escribir código.
3. **Escena:** `scene_template.html` + `build_scene.py` (datos reales del caso, cifras canónicas auditadas).
4. **Render:** `./render.sh` (reproducible; `ffprobe` valida 1920×1080 @ 30 fps).
5. **QA visual:** extraer keyframes del MP4 (`ffmpeg -ss …`) y revisar solapes, cifras y ritmo.
6. **Integración:** decidir reemplazo/inserción en el deck (aún no iniciada) y verificar dimensiones del panel objetivo.

## 5. Piloto: `video_anatomia_senal` (Diapo 5 — Acto 1)

- **Contenido:** descomposición ontológica con datos reales SENAMHI Punchana (2019–2025): `Y = T + S + C + ε` con la metáfora del río (cauce, marea, régimen El Niño 2023–24, entropía); récord 38.0 °C (07·10·2023); `n = 2,557`.
- **Versión vigente:** `anatomia_senal.mp4` — **entrada de 30 s** (1920×1080 @ 30 fps, 900 frames): tramo `[4 s, 27 s]` de la escena cinemática (34 s) estirado ×1.3043 para dar más tiempo de lectura a la anatomía (`Y = T + S + C + ε`), con fade-in de 0.35 s desde el color exacto del fondo de la Diapo 5 (`#040714`) y cierre con las 4 capas y la ecuación encendidas; pensada para reproducirse al avanzar de la Diapo 4 a la 5 (después aparece la diapositiva con su explicación). El cold-open, la cita y el cierre del corte de 34 s quedan fuera.
- **Versiones anteriores:** `anatomia_senal_v3_34s.mp4` (entrada cinemática completa: cold-open, cita y cierre), `anatomia_senal_v2_30s.mp4` (tramo `[2 s, 22 s]` ×1.5, 1600×900) y `anatomia_senal_v1_completo.mp4` (primer corte de 30 s). **Retiradas del repo en F12** (`git rm`); el patrón `video/**/*_v[0-9]*.mp4` queda en `.gitignore` para que no vuelvan a versionarse.
- **Uso previsto:** entrada de la Diapo 5; tras el video aparece la diapositiva con su explicación (integración pendiente de decisión).

## 6. Criterios de Aceptación (Fase)

- [X] `render.sh` regenera el MP4 sin intervención manual (build → captura → encode).
- [X] Reproducibilidad: `ffprobe` reporta 1920×1080, 30 fps, 900 frames, H.264 `yuv420p` `+faststart`.
- [X] Entrada limpia: fade-in de 0.35 s desde el color de fondo de la Diapo 5 (`#040714`) y cierre con la composición completa (4 chips y ecuación encendidas).
- [X] Cifras canónicas auditadas dentro del video (38.0 °C, 2,557 días, ±1.37 °C, σ 2.18 °C).
- [X] Estructura `video/seccion_1/diapo_5/video_anatomia_senal/` autocontenida y versionada.
- [ ] Decisión de integración en la Diapo 5 (reproducción como entrada al avanzar de la Diapo 4 a la 5) y verificación del handoff con la diapositiva real.
- [X] Segundo video piloto en otra sección (valida que el proceso es replicable): `video_agro_origen` (Sección 3 · Diapo 19) renderizado y auditado en `video/seccion_3/diapo_19/video_agro_origen/agro_origen.mp4`.

## 7. Tests de la Fase

- **Test de render:** `./render.sh` termina en verde y `ffprobe` confirma especificaciones (1920×1080 @ 30, 900 frames).
- **Test de determinismo:** dos ejecuciones consecutivas de `capture.mjs` sobre el mismo `scene.html` producen frames idénticos (mismo hash en frames comparados).
- **Test visual:** keyframes extraídos del MP4 en `t = 0.2 s`, `2.0 s`, `23.0 s`, `27.2 s`, `29.9 s` sin solapes, con cifras correctas, fade-in desde `#040714` y cierre con las 4 capas encendidas.

---

## 8. Backlog de videos

Para evitar saturar la charla y maximizar el impacto pedagógico, los videos de **entrada cinemática (`~30 s`, 1920×1080 @ 30 fps)** se concentran en los **cambios de paradigma teórico de la Sección 1 (Acto 1) y la Sección 3 (Acto 3)**, la **demostración empírica del Caso 2 en la Sección 4 (Acto 4: la trampa del satélite NDVI en la Diapo 26 y la validación Walk-Forward en la Diapo 27)** y el **manifiesto de síntesis en la Sección 5 (Acto 5, Diapo 29)**.

### Tabla Maestra del Backlog

| Sección | Diapo | Slug | Rol | Duración | Prioridad | Estado |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| **Sección 1** *(Acto 1)* | **Diapo 05** | `video_anatomia_senal` | `entrada` *(Diapo 4 → 5)* | `30 s` *(900 f)* | **Alta** *(Piloto #1)* | `completado` *(MP4 vigente listo e integrado)* |
| **Sección 3** *(Acto 3)* | **Diapo 19** | `video_agro_origen` | `entrada` *(Diapo 18 → 19)* | `30 s` *(900 f)* | **Alta** *(Piloto #2 · SF11.3)* | `completado` *(MP4 vigente listo e integrado)* |
| **Sección 1** *(Acto 1)* | **Diapo 07** | `video_puente_tabular` | `entrada` *(Diapo 6 → 7)* | `30 s` *(900 f)* | **Alta** | `completado` *(MP4 vigente listo e integrado)* |
| **Sección 3** *(Acto 3)* | **Diapo 21** | `video_fisica_biologica` | `entrada` *(Diapo 20 → 21)* | `30 s` *(900 f)* | **Alta** | `completado` *(MP4 vigente listo e integrado)* |
| **Sección 1** *(Acto 1)* | **Diapo 09** | `video_zero_shot_tsfm` | `entrada` *(Diapo 8 → 9)* | `30 s` *(900 f)* | **Media** | `completado` *(MP4 vigente listo e integrado)* |
| **Sección 1** *(Acto 1)* | **Diapo 10** | `video_cono_incertidumbre` | `entrada` *(Diapo 9 → 10)* | `30 s` *(900 f)* | **Media** | `completado` *(MP4 vigente listo e integrado)* |
| **Sección 5** *(Acto 5)* | **Diapo 29** | `video_sintesis_cierre` | `entrada` *(Diapo 28 → 29)* | `25 s` *(750 f)* | **Baja** *(Opcional)* | `completado` *(MP4 vigente listo e integrado)* |
| **Sección 4** *(Acto 4)* | **Diapo 26** | `video_trampa_ndvi` | `entrada` *(Diapo 25 → 26)* | `30 s` *(900 f)* | **Alta** *(SF11.5)* | `completado` *(MP4 vigente listo e integrado)* |
| **Sección 4** *(Acto 4)* | **Diapo 27** | `video_walkforward_jaen` | `entrada` *(Diapo 26 → 27)* | `30 s` *(900 f)* | **Media** *(SF11.5)* | `completado` *(MP4 vigente listo e integrado)* |

---

## 9. Fichas de Producción por Video (Plantilla Obligatoria)

### 9.1 Ficha 0 (Calibración / Piloto Real): `video_anatomia_senal` (Sección 1 · Diapo 05)
- **ID:** `video_anatomia_senal` — `video/seccion_1/diapo_5/video_anatomia_senal/`
- **Diapositiva:** Sección 1, Diapo 5, `"ANATOMÍA DE LA SEÑAL: ¿Qué es una Serie Temporal? · Física Causal vs. Ruido"` (Acto 1)
- **Rol del video:** `"entrada"` (se reproduce al avanzar Diapo 4 → 5 y luego aparece la diapo)
- **Objetivo pedagógico:** Entender $Y(t) = T(t) + S(t) + C(t) + \varepsilon(t)$ como la descomposición aditiva de una serie temporal real antes de explorar el simulador interactivo 2D/3D.
- **Duración objetivo:** `30 s` (`900 frames` @ 30 fps; tramo `[4 s, 27 s]` de la escena de 34 s estirado $\times 1.3043$)
- **Guion por beats:**
  - **Cold-open:** Fade-in de `0.35 s` desde `#040714` hacia el título y el lienzo de la señal observada $Y(t)$ en Punchana (`2019–2025`).
  - **Desarrollo 1 (Señal bruta y récord):** Trazado de los `2,557` días diarios marcando el pico histórico de `38.0 °C` (`07·10·2023`).
  - **Desarrollo 2 (Descomposición en 4 capas):** Separación progresiva de `T(t)` (Tendencia / cauce), `S(t)` (Estacionalidad anual `±1.37 °C`), `C(t)` (Ciclo / anomalía El Niño 2023–24) y `ε(t)` (Residuo estocástico `σ = 2.18 °C`) con sus tarjetas y métricas.
  - **Cierre:** Síntesis con las 4 capas encendidas simultáneamente y la ecuación estructural `Y = T + S + C + ε` iluminada.
- **Cifras canónicas que deben aparecer, con fuente:**
  - Récord `38.0 °C` del `07·10·2023` (fuente: `data/caso_1/senamhi_diario.csv`, fila `2023-10-07`).
  - `n = 2,557` días continuos `2019–2025` (fuente: `data/caso_1/senamhi_diario.csv`).
  - Amplitud estacional `S ±1.37 °C` y desviación del residuo `σ 2.18 °C` (fuente: descomposición sobre `data/caso_1/senamhi_diario.csv` en `video/seccion_1/diapo_5/video_anatomia_senal/build_scene.py`).
- **Material base:**
  - Prototipo origen: `docs/notebooklm/seccion_1/prototipos/5_Anatomia_de_la_senal_temporal_v3.html`.
  - Datos CSV: `data/caso_1/senamhi_diario.csv`.
  - Fórmulas y textos exactos: `"ANATOMÍA DE LA SEÑAL"`, `"Y(t) = T(t) + S(t) + C(t) + ε(t)"`, `"T(t) Tendencia"`, `"S(t) Estacionalidad"`, `"C(t) Ciclo / Régimen"`, `"ε(t) Residuo"`, `"38.0 °C (07·10·2023)"`, `"n = 2,557 días"`.
- **Handoff:** Color de fondo exacto del slide destino `#040714`; inicia con fade-in de `0.35 s` desde `#040714` y termina con composición completa encendida (el fade-out de `0.45 s` hacia el simulador lo ejecuta el contenedor `#cinematicVideoGate` de la Diapo 5).
- **Integración en el deck:** Se dispara automáticamente al avanzar de la Diapo 4 a la Diapo 5 (`#cinematicVideoGate` en `T10.1.3`); al terminar (`ended`) o al pulsar `→` / `"Pasar al Simulador Interactivo →"`, se desvanece revelando la Diapo 5 interactiva y queda accesible en el botón `"🎬 Intro"` de la `.flowbar`.
- **Dependencias y prioridad:** Depende del rediseño de altura/tipografía de la Diapo 5 (`T10.2.1`) y del inyector `T10.1.3`; prioridad **alta**; piloto de referencia.
- **Aceptación específica:**
  - [X] `ffprobe` confirma `1920×1080` @ `30 fps`, `900 frames` (`30.0 s`), H.264 `yuv420p` `+faststart`.
  - [X] Las 4 cifras canónicas (`38.0 °C`, `2,557 días`, `±1.37 °C`, `σ 2.18 °C`) aparecen sin solapes de texto.
  - [X] Primer frame parte de `#040714` y último frame conserva las 4 capas + ecuación encendidas.
- **Estado:** `completado` (MP4 vigente renderizado en `video/seccion_1/diapo_5/video_anatomia_senal/anatomia_senal.mp4`; pendiente únicamente conectar su reproducción en el deck vía `T10.1.3` / `T11.2.3`).

---

### 9.2 Ficha 1 (Segundo Piloto · SF11.3): `video_agro_origen` (Sección 3 · Diapo 19)
- **ID:** `video_agro_origen` — `video/seccion_3/diapo_19/video_agro_origen/`
- **Diapositiva:** Sección 3, Diapo 19, `"Cómo el agro inventó el forecasting antes que la IA · De las cabañuelas a la malla neuronal"` (Acto 3)
- **Rol del video:** `"entrada"` (se reproduce al avanzar Diapo 18 → 19 como gran apertura de la Sección 3 y luego aparece la diapo)
- **Objetivo pedagógico:** Comprender que la agricultura inventó la predicción empírica hace milenios leyendo bioindicadores con rezago biológico ($\tau = 6\text{ a }8\text{ meses}$), y que los satélites e IA actuales son la evolución instrumental de ese mismo principio físico.
- **Duración objetivo:** `30 s` (`900 frames` @ 30 fps)
- **Guion por beats:**
  - **Cold-open:** Fade-in de `0.35 s` desde `#040812` con el sello `"ACTO 3 · LA FRONTERA AGRÍCOLA"` y la pregunta `"¿Quién inventó realmente el Forecasting?"`.
  - **Desarrollo 1 (El Espejo Ancestral):** A la izquierda emerge el surco andino / observador ancestral registrando bioindicadores (`"Almanaque (Bioindicadores)"`, floración y lluvias de primavera) con un arco temporal que salta `τ = 6 a 8 meses` hacia la cosecha futura.
  - **Desarrollo 2 (La Evolución en 5 Hitos: 1950 → 2026):** Línea de tiempo acelerada que ilumina los 5 escalones de resolución: `"Hito 1 · Calendarios y Almanaques (Estacional)"` $\to$ `"Hito 2 · Estaciones Experimentales (Semanal/Mensual)"` $\to$ `"Hito 3 · Agrometeorología Operativa (Diaria)"` $\to$ `"Hito 4 · Revolución Satelital (Cada 5–12 días)"` $\to$ `"Hito 5 · Agricultura de Precisión (Tiempo Real)"`.
  - **Desarrollo 3 (El Gemelo Digital en Jaén):** A la derecha se despliega la malla satelital sobre las `24 campañas (2001–2024)` de café en Jaén (`MODIS NDVI/EVI` + `ERA5`), conectando la floración (`Ago–Oct`) con la cosecha (`Mar–Jul`).
  - **Cierre:** Queda encendida la dualidad `"Almanaque (Bioindicadores) ⟷ Gemelo Digital (Sensores + IA)"` junto a la ecuación `"Cosecha Yₜ = f( Clima en Floración Xₜ₋τ ) con τ = 6 a 8 meses"`, lista para entregar el control al espejo interactivo de la Diapo 19.
- **Cifras canónicas que deben aparecer, con fuente:**
  - `N = 24 campañas (2001–2024)` en Jaén, Cajamarca (`-5.7049° Lat, -79.0104° Lon`, `600–1,800 msnm`) (fuente: `data/caso_2/README.md` y `data/caso_2/cafe_jaen_campanias.csv`).
  - Rezago biológico `τ = 6 a 8 meses` entre ventana de floración (`Ago–Oct`) y cosecha (`Mar–Jul`) (fuente: `data/caso_2/README.md` y `docs/notebooklm/seccion_3/prototipos/19_c_mo_el_agro_invent_el_forecasting.html`).
  - Salto de resolución `"De 1 dato/año a 1 dato/día/píxel"` y frecuencia satelital `"Cada 5–12 días"` (fuente: `docs/notebooklm/seccion_3/prototipos/19_c_mo_el_agro_invent_el_forecasting.html` y `20_del_almanaque_al_sat_lite.html`).
- **Material base:**
  - Prototipo origen: `docs/notebooklm/seccion_3/prototipos/19_c_mo_el_agro_invent_el_forecasting.html`.
  - Datos CSV: `data/caso_2/cafe_jaen_campanias.csv` (columnas `campania`, `lluvia_flor_mm`, `ndvi_anual`, `rendimiento_qq_ha`).
  - Fórmulas y textos exactos: `"Cómo el agro inventó el forecasting antes que la IA"`, `"Almanaque (Bioindicadores) ⟷ Gemelo Digital (Sensores + IA)"`, `"Cosecha Yₜ = f( Clima en Floración Xₜ₋τ ) con τ = 6 a 8 meses"`, `"N = 24 campañas (2001–2024)"`.
- **Handoff:** Color de fondo exacto del slide destino `#040812` (`--bg: #040812` en los prototipos de la Sección 3); inicia con fade-in de `0.35 s` desde `#040812` y termina en frame de composición completa con el espejo dual encendido.
- **Integración en el deck:** Se dispara al avanzar de la Diapo 18 (portada de Sección 03) a la Diapo 19; al concluir, `#cinematicVideoGate` hace fade-out (`0.45 s`) hacia el prototipo interactivo de la Diapo 19.
- **Dependencias y prioridad:** Valida la replicabilidad del pipeline en `SF11.3` y se acopla con la limpieza de la Diapo 19 en `T10.4.1`; prioridad **alta** (Candidato #1 para `SF11.3`).
- **Aceptación específica:**
  - [X] `ffprobe` valida `1920×1080` @ `30 fps`, `900 frames` (`30.000 s`), H.264 `yuv420p` `+faststart` (`agro_origen.mp4`, ~2.20 MB).
  - [X] Fondo inicial y final armónico con `#040812` (fade-in de `0.35 s` desde `#040812`; cero flash negro/gris al pasar a la Diapo 19).
  - [X] Muestra la ecuación exacta `"Cosecha Yₜ = f( Clima en Floración Xₜ₋τ ) con τ = 6 a 8 meses"` y los 5 hitos sin truncamiento ni solape (QA de keyframes en `t = 0.2 s`, `5 s`, `14 s`, `23 s`, `29.8 s`).
  - [X] Usa datos reales de `data/caso_2/cafe_jaen_campanias.csv` (`2001–2024`: malla satelital `24` columnas, línea `NDVI anual`, barras `rendimiento_qq_ha` 2010–2016 y 2018–2024 con ausencias en gris).
- **Estado:** `completado` — `agro_origen.mp4` (30 s · 900 f · 1920×1080 @ 30 fps, H.264 `yuv420p` `+faststart`) renderizado en `video/seccion_3/diapo_19/video_agro_origen/`; QA visual superado (cierre dual `ALMANAQUE ⟷ GEMELO DIGITAL` + ecuación sin solapes, corrección de especificidad CSS del cierre verificada en keyframes); pendiente únicamente conectar su reproducción en el deck (`Diapo 18 → 19`).

---

### 9.3 Ficha 2: `video_puente_tabular` (Sección 1 · Diapo 07)
- **ID:** `video_puente_tabular` — `video/seccion_1/diapo_7/video_puente_tabular/`
- **Diapositiva:** Sección 1, Diapo 7, `"VÍA 2: El Puente Tabular · El Truco de los Lags y Árboles (LightGBM, XGBoost)"` (Acto 1)
- **Rol del video:** `"entrada"` (se reproduce al avanzar Diapo 6 → 7 y luego aparece la diapo)
- **Objetivo pedagógico:** Visualizar mecánicamente cómo una serie continua se transforma en una matriz supervisada de retrasos (`Lags`) para entrenar árboles GBDT, y por qué las particiones ortogonales de los árboles jamás pueden extrapolar fuera del máximo histórico (produciendo una `"Meseta Plana"`).
- **Duración objetivo:** `30 s` (`900 frames` @ 30 fps)
- **Guion por beats:**
  - **Cold-open:** Fade-in de `0.35 s` desde `#040714` con el rótulo `"VÍA 2 · EL PUENTE TABULAR"` y la curva diaria de temperatura de Punchana (`data/caso_1/senamhi_diario.csv`).
  - **Desarrollo 1 (La Ventana Deslizante → Matriz de Lags):** Una ventana deslizante recorre la curva continua extrayendo `yₜ₋₇`, `yₜ₋₁` y `Media₇`, proyectándolos con flechas luminosas hacia las columnas de una tabla supervisada: `"Vector Xₜ = [ yₜ₋₁, yₜ₋₇, Media₇, Promoₜ, Climaₜ ] ──▶ yₜ₊ₕ"`.
  - **Desarrollo 2 (El Dominio en Datos Tabulares — Walmart M5):** Los nodos de un ensamble `LightGBM / XGBoost` particionan el espacio de características y muestran el hito `"LightGBM( Lags + Rolling_Mean + Precio + Promo ) ──▶ 30,490 SKUs"` (y en Punchana: `ExtraTrees RMSE 1.88 °C en 0.25 s`).
  - **Desarrollo 3 (La Trampa del Árbol / Techo Ortogonal):** Cuando la serie real supera el tope de entrenamiento (`tope_entrenamiento = 34.0 °C` rumbo al récord de `38.0 °C` del `07·10·2023`), la predicción del árbol en niveles choca contra una barrera horizontal roja (`~31.4–32.3 °C`) mostrando la regla: `"Si X_nuevo > X_máx_histórico ──▶ Árbol devuelve constante (Meseta Plana)"`.
  - **Cierre:** Comparación final entre la `"Meseta Plana"` del árbol en niveles y el rescate mediante diferencias ($\Delta y_t = y_t - y_{t-1}$), dejando la composición encendida para pasar al simulador de la Diapo 7.
- **Cifras canónicas que deben aparecer, con fuente:**
  - Récord `38.0 °C` (`07·10·2023`) y `n = 2,557` días (fuente: `data/caso_1/senamhi_diario.csv`).
  - Experimento de extrapolación con tope `34.0 °C`: valores reales de `34.8 °C` (`2023-09-16`) y `35.6 °C` (`2023-09-22`) donde `pred_arbol_niveles` queda estancado en `31.44 °C` y `31.57 °C` mientras `pred_arbol_diferencias` sube a `33.69 °C`–`34.53 °C` (fuente: `data/caso_1/experimento_extrapolacion.csv`).
  - Referencia M5 Forecasting: `30,490 SKUs` (fuente: `docs/notebooklm/seccion_1/prototipos/7_Era_2_El_puente_tabular.html`, Makridakis et al., 2022).
- **Material base:**
  - Prototipo origen: `docs/notebooklm/seccion_1/prototipos/7_Era_2_El_puente_tabular.html`.
  - Datos CSV: `data/caso_1/experimento_extrapolacion.csv` y `data/caso_1/senamhi_diario.csv`.
  - Fórmulas y textos exactos: `"VÍA 2: El Puente Tabular · El Truco de los Lags y Árboles (LightGBM, XGBoost)"`, `"Vector Xₜ = [ yₜ₋₁, yₜ₋₇, Media₇, Promoₜ, Climaₜ ] ──▶ yₜ₊ₕ"`, `"Si X_nuevo > X_máx_histórico ──▶ Árbol devuelve constante (Meseta Plana)"`.
- **Handoff:** Color de fondo exacto del slide destino `#040714`; fade-in de `0.35 s` desde `#040714` y cierre con composición completa encendida (curva + tabla de lags + muro de extrapolación).
- **Integración en el deck:** Se reproduce automáticamente al avanzar de la Diapo 6 a la Diapo 7 (`#cinematicVideoGate`); al terminar o pulsar `→` da paso a la Etapa 1 de la Diapo 7.
- **Dependencias y prioridad:** Independiente de otros videos; se integra con `T10.1.3` y `T10.2.2`; prioridad **alta**.
- **Aceptación específica:**
  - [X] `ffprobe` valida `1920×1080` @ `30 fps`, `900 frames` (`30.000 s`), H.264 `yuv420p` `+faststart` (`puente_tabular.mp4`, ~2.74 MB).
  - [X] Animación clara de los puntos `yₜ₋₁` y `yₜ₋₇` (y `Media₇`) viajando de la curva a las celdas de la tabla supervisada (fila estrella `yₜ₊ₕ = 38.0 °C`) sin cruzar texto.
  - [X] Trazado fiel de `data/caso_1/experimento_extrapolacion.csv` mostrando el tope `34.0 °C` y la meseta plana de `pred_arbol_niveles` (~31.4–32.5 °C) frente al rescate por diferencias (hasta 37.46 °C).
- **Estado:** `completado` — `puente_tabular.mp4` (30 s · 900 f · 1920×1080 @ 30 fps, H.264 `yuv420p` `+faststart`) renderizado en `video/seccion_1/diapo_7/video_puente_tabular/`; QA superado (fila estrella de la matriz con `yₜ₊ₕ = 38.0 °C`, vector canónico completo bajo la tabla, techo de 34.0 °C y regla de meseta sin solapes); pendiente conectar su reproducción en el deck (`Diapo 6 → 7`).

---

### 9.4 Ficha 3: `video_fisica_biologica` (Sección 3 · Diapo 21)
- **ID:** `video_fisica_biologica` — `video/seccion_3/diapo_21/video_fisica_biologica/`
- **Diapositiva:** Sección 3, Diapo 21, `"Física biológica · Las 3 leyes que obligan a la IA a aprender botánica"` (Acto 3)
- **Rol del video:** `"entrada"` (se reproduce al avanzar Diapo 20 → 21 y luego aparece la diapo)
- **Objetivo pedagógico:** Demostrar visualmente por qué un modelo puramente estadístico o satelital fracasa en agricultura si ignora las 3 leyes biofísicas: el retraso de fase ($\tau = 6\text{–}8\text{ meses}$), los umbrales no lineales fatales ($T > 32\,^\circ\text{C}$ / $\text{VPD} > 1.8\text{ kPa}$) y la maldición de la dimensionalidad ($N = 24$ campañas).
- **Duración objetivo:** `30 s` (`900 frames` @ 30 fps)
- **Guion por beats:**
  - **Cold-open:** Fade-in de `0.35 s` desde `#040812` con el título `"FÍSICA BIOLÓGICA · EL LÍMITE ALGORÍTMICO"` y las 3 leyes encendiéndose como pilares.
  - **Desarrollo 1 (Ley 1 — El Engranaje de Retraso $\tau = 6\text{–}8\text{ meses}$):** Un pulso climático en la ventana de floración (`Ago–Oct`, $X_{t-\tau}$) mueve un engranaje de memoria biológica que tarda `τ = 6 a 8 meses` en manifestarse en la cosecha ($Y_t$, `Mar–Jul`), mientras el satélite óptico ve el follaje verde estable (`NDVI ~0.74`, variación de solo `+1.4%` en 2014).
  - **Desarrollo 2 (Ley 2 — Umbral Fatal de Sed Atmosférica y Calor):** El termómetro cruza `T > 32°C` y el déficit de presión de vapor supera `"VPD = eₛ(T) − eₐ > 1.8 kPa"`, disparando el `"Cierre Estomático y Aborto Floral"` (y en el choque biológico de 2014, el rendimiento cae `-56.0%` hasta `10.0 qq/ha`).
  - **Desarrollo 3 (Ley 3 — `"N=24 no perdona"`):** Contraposición visual entre `"500 Variables Crudas sobre N=24 = Overfit"` (ruido espurio) frente a la agregación guiada por fenología (`lluvia_flor_mm` con correlación $r = 0.7511$ y `def_hidrico_flor_mm` con $r = 0.7564$).
  - **Cierre:** Quedan encendidas las 3 ecuaciones canónicas de la Diapo 21 sobre fondo `#040812` para entregar el relevo al simulador interactivo.
- **Cifras canónicas que deben aparecer, con fuente:**
  - `N = 24 campañas (2001–2024)` en Jaén y rezago `τ = 6–8 meses` (fuente: `data/caso_2/cafe_jaen_campanias.csv` y `data/caso_2/README.md`).
  - Saturación e invisibilidad del NDVI: `NDVI ~0.74` (`CV = 2.32%`, correlación débil `r = 0.1536`, `p = 0.60`), y caída de cosecha en 2014 de `-56.0%` (`10.0 qq/ha`) con variación de NDVI de apenas `+1.4%` (`0.7483`) (fuente: `data/caso_2/cafe_jaen_hipotesis.json`, hipótesis `H1_saturacion` y `H4_roya_invisibilidad`).
  - Señal climática en floración (`Ago–Oct`): correlación con lluvia en floración `r = 0.7511`, déficit hídrico `r = 0.7564`, temperatura máxima en floración `r = -0.5606` (fuente: `data/caso_2/cafe_jaen_hipotesis.json`, hipótesis `H2_fenologia`).
  - Umbrales biofísicos del prototipo: `"VPD > 1.8 kPa"` y `"T > 32°C"` (fuente: `docs/notebooklm/seccion_3/prototipos/21_f_sica_biol_gica_y_el_l_mite_algor_tmico.html`).
- **Material base:**
  - Prototipo origen: `docs/notebooklm/seccion_3/prototipos/21_f_sica_biol_gica_y_el_l_mite_algor_tmico.html`.
  - Datos CSV/JSON: `data/caso_2/cafe_jaen_campanias.csv` y `data/caso_2/cafe_jaen_hipotesis.json`.
  - Fórmulas y textos exactos: `"Estímulo (Xₜ₋τ) ──[ Engranaje τ = 6–8m ]──▶ Cosecha Yₜ (Colapsa si VPD > 1.8)"`, `"VPD = eₛ(T) − eₐ > 1.8 kPa ó T > 32°C ──▶ Cierre Estomático y Aborto Floral"`, `"500 Variables Crudas sobre N=24 = Overfit │ Restricción Fenológica = Error ÷ 4"`.
- **Handoff:** Color de fondo exacto del slide destino `#040812`; fade-in de `0.35 s` desde `#040812` y cierre con las 3 leyes biofísicas encendidas.
- **Integración en el deck:** Se dispara al avanzar de la Diapo 20 a la Diapo 21 (`#cinematicVideoGate`); al finalizar o pulsar `→` muestra la Etapa 1 de la Diapo 21.
- **Dependencias y prioridad:** Se acopla con `T10.1.3` y `T10.4.1`; prioridad **alta**.
- **Aceptación específica:**
  - [X] `ffprobe` valida `1920×1080` @ `30 fps`, `900 frames`, H.264 `yuv420p` `+faststart`.
  - [X] Contraste visual explícito entre la línea plana del satélite (`NDVI ~0.74`, `+1.4%`) y el desplome real de cosecha (`-56.0%`, `10.0 qq/ha` en 2014) — barras de cosecha 2010–2024 con 2014 en rojo bajo la curva NDVI.
  - [X] El rótulo `Lag τ = 6–8m` se dibuja dentro de una pastilla opaca sin solapar los dientes ni el eje del engranaje.
- **Estado:** `completado` — `fisica_biologica.mp4` (30 s · 900 f · 2.75 MB) auditado; pendiente integración en el deck.

---

### 9.5 Ficha 4: `video_zero_shot_tsfm` (Sección 1 · Diapo 09)
- **ID:** `video_zero_shot_tsfm` — `video/seccion_1/diapo_9/video_zero_shot_tsfm/`
- **Diapositiva:** Sección 1, Diapo 9, `"VÍA 4: Revolución Zero-Shot y Foundation Models · TimesFM, Chronos, Moirai, Lag-Llama y TimeGPT"` (Acto 1)
- **Rol del video:** `"entrada"` (se reproduce al avanzar Diapo 8 → 9 y luego aparece la diapo)
- **Objetivo pedagógico:** Entender cómo los Modelos Fundacionales de Series Temporales (`TSFM`) aprenden una gramática universal sobre billones de puntos (`27B–100B pts`) mediante tokenización discreta (`Chronos`) o parches continuos (`TimesFM`) para predecir una serie nueva en modo *Zero-Shot* (`0% Train local`).
- **Duración objetivo:** `30 s` (`900 frames` @ 30 fps)
- **Guion por beats:**
  - **Cold-open:** Fade-in de `0.35 s` desde `#040714` con el título `"VÍA 4 · REVOLUCIÓN ZERO-SHOT (TSFM)"` y la fórmula `"Preentreno (27B–100B pts) + Contexto C ──▶ Inferencia Zero-Shot"`.
  - **Desarrollo 1 (Preentrenamiento Multidominio Masivo):** Flujos de series de múltiples dominios (energía, clima, transporte, finanzas) convergen en un núcleo neuronal preentrenado sobre `27B–100B puntos` (corpus LOTSA / Chronos / TimesFM).
  - **Desarrollo 2 (Duelo de Lectura: Tokens vs. Parches):** La pantalla divide el mecanismo en dos vías paralelas: arriba `"Chronos = 4,096 Tokens (Cross-Entropy)"` cuantizando valores reales en vocabulario discreto; abajo `"TimesFM = Parches Continuos (MSE)"` agrupando tramos temporales en vectores densos.
  - **Desarrollo 3 (Inferencia Zero-Shot en Punchana):** Entra como contexto `C` la serie de temperatura de Punchana (`n = 2,557 días`) sin ajustar pesos (`0% Train`) y ambos modelos emiten el pronóstico directo (`TimesFM RMSE 1d = 1.883 °C`, `Chronos RMSE 1d = 1.903 °C`, empatando estadísticamente con el mejor modelo local `p = 0.7095` y `p = 0.6523`).
  - **Cierre:** Quedan iluminadas las 5 arquitecturas (`TimesFM`, `Chronos`, `Moirai`, `Lag-Llama`, `TimeGPT`) y el puente hacia la calibración conforme (`"Zero-Shot (0% Train) + 80% Datos en Calibración (SCP) ──▶ Garantía MCR ≥ 90%"`).
- **Cifras canónicas que deben aparecer, con fuente:**
  - Escala de preentrenamiento `"27B–100B pts"` y `"4,096 Tokens"` (fuente: `docs/notebooklm/seccion_1/prototipos/9_Era_4_Modelos_Fundacionales_Zero_Shot.html` — Ansari et al., 2024; Woo et al., 2024; Das et al., 2024).
  - Desempeño Zero-Shot en Punchana (`n = 2,557 días`): `TimesFM (Google) Zero-Shot` (`RMSE 1d = 1.883 °C`, `MAE 1d = 1.457 °C`, `p = 0.7095`) y `Chronos (Amazon) Zero-Shot` (`RMSE 1d = 1.903 °C`, `MAE 1d = 1.418 °C`, `p = 0.6523`) frente a `ExtraTrees` (`RMSE 1d = 1.880 °C`) (fuente: `data/caso_1/benchmark_punchana.csv`).
- **Material base:**
  - Prototipo origen: `docs/notebooklm/seccion_1/prototipos/9_Era_4_Modelos_Fundacionales_Zero_Shot.html`.
  - Datos CSV: `data/caso_1/benchmark_punchana.csv` y `data/caso_1/senamhi_forecast_7d.csv`.
  - Fórmulas y textos exactos: `"Preentreno (27B–100B pts) + Contexto C ──▶ Inferencia Zero-Shot"`, `"Chronos = 4,096 Tokens (Cross-Entropy) │ TimesFM = Parches Continuos (MSE)"`, `"Zero-Shot (0% Train) + 80% Datos en Calibración (SCP) ──▶ Garantía MCR ≥ 90%"`.
- **Handoff:** Color de fondo exacto del slide destino `#040714`; fade-in de `0.35 s` desde `#040714` y cierre con composición completa encendida.
- **Integración en el deck:** Se reproduce al avanzar de la Diapo 8 a la Diapo 9 (`#cinematicVideoGate`); al terminar o pulsar `→` revela la Etapa 1 de la Diapo 9.
- **Dependencias y prioridad:** Se integra con `T10.1.3` y `T10.2.2`; prioridad **media**.
- **Aceptación específica:**
  - [X] `ffprobe` valida `1920×1080` @ `30 fps`, `900 frames`, H.264 `yuv420p` `+faststart`.
  - [X] Diferenciación visual nítida entre cuantización en celdas discretas (`Chronos = 4,096 Tokens`) y empaquetado de segmentos continuos (`TimesFM = Parches Continuos`) — escalera amber con 20 tokens vs. curva continua con 6 parches y vectores.
  - [X] Cifras exactas de `data/caso_1/benchmark_punchana.csv` (`1.883 °C`, `1.903 °C`, `1.880 °C`) sin solapes.
- **Estado:** `completado` — `zero_shot_tsfm.mp4` (30 s · 900 f · 2.85 MB) auditado; pendiente integración en el deck.

---

### 9.6 Ficha 5: `video_cono_incertidumbre` (Sección 1 · Diapo 10)
- **ID:** `video_cono_incertidumbre` — `video/seccion_1/diapo_10/video_cono_incertidumbre/`
- **Diapositiva:** Sección 1, Diapo 10, `"DIAPOSITIVA 10: La Ilusión de la Certeza y el Cono de Incertidumbre · Lyapunov ─▶ 5 Pasos SCP ─▶ ERCOT ─▶ Pase a Diapo 11"` (Acto 1)
- **Rol del video:** `"entrada"` (se reproduce al avanzar Diapo 9 → 10 y luego aparece la diapo)
- **Objetivo pedagógico:** Comprender por qué todo pronóstico puntual ($\hat{y}_{t+h}$) es ciego ante el crecimiento caótico del error en el horizonte y cómo *Split Conformal Prediction (SCP)* construye bandas empíricas calibradas ($P_{10}\text{–}P_{90}$) sin asumir normalidad gaussiana.
- **Duración objetivo:** `30 s` (`900 frames` @ 30 fps)
- **Guion por beats:**
  - **Cold-open:** Fade-in de `0.35 s` desde `#040714` con el título `"LA ILUSIÓN DE LA CERTEZA Y EL CONO DE INCERTIDUMBRE"` y una línea solitaria de pronóstico puntual $\hat{y}_{t+h}$ avanzando del día `t+1` al `t+7`.
  - **Desarrollo 1 (La Divergencia del Horizonte):** La línea puntual choca con un friaje repentino en Punchana (`27.2 °C` el `2025-12-28` en `senamhi_forecast_7d.csv` frente a `~32.8–35.0 °C` puntual), abriéndose en múltiples trayectorias divergentes según la ley `"σ(h) ∝ σ₁ · √h ──▶ Bandas P25–P75 (50%) y P10–P90 (80%)"`.
  - **Desarrollo 2 (El Escudo Matemático SCP en 3 Fórmulas):** Los residuos históricos de calibración se ordenan en un histograma empírico y proyectan el cuantil libre de distribución: `"Sᵢ = |f̂(xᵢ) − yᵢ| ──▶ q̂ = cuantil₁₋α(S_Cal) ──▶ I(x) = [ f̂(x) ± q̂ ]"`.
  - **Desarrollo 3 (El Cono Operacional P10–P90 en Punchana):** Se despliega el abanico `P10–P90` real de 7 días (`2025-12-25` a `2025-12-31`, banda `29.55 °C – 37.42 °C` de `senamhi_forecast_7d.csv`) con pastillas legibles para `"Núcleo 50%"`, `"Pronóstico Puntual"` y `"Banda 80% (P10–P90)"`.
  - **Cierre:** El cono queda encendido con las fórmulas de SCP listas para dar paso al simulador interactivo de la Diapo 10.
- **Cifras canónicas que deben aparecer, con fuente:**
  - Serie base de Punchana: `n = 2,557 días`, récord `38.0 °C` (`07·10·2023`), `σ = 2.18 °C` (fuente: `data/caso_1/senamhi_diario.csv`).
  - Horizonte de 7 días (`2025-12-25` a `2025-12-31`): banda empírica `ci_lower_p10` (`29.55 °C` a `31.24 °C`) y `ci_upper_p90` (`35.73 °C` a `37.42 °C`), y choque de friaje observado de `27.2 °C` (`2025-12-28`) (fuente: `data/caso_1/senamhi_forecast_7d.csv`).
  - Benchmark ERCOT citado en el prototipo: `"ERCOT-2232: Chronos-Bolt (MASE 0.362, MSIW 0.312) vs. LightGBM (1.195)"` (fuente: `docs/notebooklm/seccion_1/prototipos/10_El_Cono_de_Incertidumbre_y_Prediccion_Conforme.html`).
- **Material base:**
  - Prototipo origen: `docs/notebooklm/seccion_1/prototipos/10_El_Cono_de_Incertidumbre_y_Prediccion_Conforme.html`.
  - Datos CSV: `data/caso_1/senamhi_forecast_7d.csv` y `data/caso_1/senamhi_diario.csv`.
  - Fórmulas y textos exactos: `"σ(h) ∝ σ₁ · √h ──▶ Bandas P25–P75 (50%) y P10–P90 (80%)"`, `"Sᵢ = |f̂(xᵢ) − yᵢ| ──▶ q̂ = cuantil₁₋α(S_Cal) ──▶ I(x) = [ f̂(x) ± q̂ ]"`.
- **Handoff:** Color de fondo exacto del slide destino `#040714`; fade-in de `0.35 s` desde `#040714` y cierre con el abanico `P10–P90` encendido.
- **Integración en el deck:** Se dispara al avanzar de la Diapo 9 a la Diapo 10 (`#cinematicVideoGate`); al concluir o pulsar `→` revela la Etapa 1 de la Diapo 10.
- **Dependencias y prioridad:** Se integra con `T10.1.3` y `T10.2.2`; prioridad **media**.
- **Aceptación específica:**
  - [X] `ffprobe` valida `1920×1080` @ `30 fps`, `900 frames`, H.264 `yuv420p` `+faststart` — verificado (`30.000 s`, `900 f`, H.264 High, `2,336,152 B`).
  - [X] Las etiquetas del cono (`"Núcleo 50%"`, `"Pronóstico Puntual"`, `"Banda 80% (P10–P90)"`) llevan pastillas opacas (`roundRect`) y no se pisan con las trayectorias — resueltas como leyenda en `y=344` (arriba del plot `y=380`), sin solape con bandas, línea puntual ni observaciones.
  - [X] Grafica los cuantiles reales `ci_lower_p10` y `ci_upper_p90` de `data/caso_1/senamhi_forecast_7d.csv` — banda 80% construida con los 7 pares reales (`29.55–37.42 °C`); núcleo 50% = `f̂ ± 0.45·q̂` (`q̂ = 3.09 °C`).
- **Estado:** `completado` — `cono_incertidumbre.mp4` (30 s · 900 f · 1920×1080 @ 30 fps · 2.34 MB); cold con línea puntual `t+1→t+7`, P1 divergencia + ley `σ(h) ∝ σ₁·√h`, P2 histograma + 3 fórmulas SCP + línea ERCOT, P3 cono real P10–P90 con friaje `27.2 °C`, cierre con las 3 fórmulas y `ERCOT-2232`; handoff `#040714`.

---

### 9.7 Ficha 6 (Opcional · Cierre Ejecutivo): `video_sintesis_cierre` (Sección 5 · Diapo 29)
- **ID:** `video_sintesis_cierre` — `video/seccion_5/diapo_29/video_sintesis_cierre/`
- **Diapositiva:** Sección 5, Diapo 29, `"Conclusiones"` (Acto 5 · Conclusiones)
- **Rol del video:** `"entrada"` (se reproduce al avanzar Diapo 28 → 29 y luego aparecen las 3 tarjetas de conclusiones de la Diapo 29)
- **Objetivo pedagógico:** Condensar en 25 segundos la evidencia empírica de toda la conferencia (los `2,557` días climáticos de Iquitos y las `24` campañas cafetaleras de Jaén) en los 3 axiomas ejecutivos innegociables antes de fijar el tablero final de conclusiones.
- **Duración objetivo:** `25 s` (`750 frames` @ 30 fps; más compacto que los videos teóricos porque actúa como recapitulación ejecutiva ágil antes del bloque de preguntas)
- **Guion por beats:**
  - **Cold-open:** Fade-in de `0.35 s` desde `#03050F` con las dos ondas protagonistas del deck convergiendo: arriba el río atmosférico de Punchana (`n = 2,557 días`, récord `38.0 °C`), abajo el pulso fenológico del café en Jaén (`N = 24 campañas`).
  - **Desarrollo 1 (Axioma 1 — Causalidad y Ockham):** Se ilumina la primera columna `"🎯 Respeta la causalidad del tiempo"`: validación temporal rodante y victoria de `ExtraTrees` en CPU (`RMSE 1.88 °C` en `0.25 s`) empatando con modelos gigantes.
  - **Desarrollo 2 (Axioma 2 — La Banda sobre el Punto):** Se ilumina la segunda columna `"🧠 El valor está en la banda, no en el punto"`: la línea puntual se abre en el cono calibrado `P10–P90` ante la entropía atmosférica ($\sigma = 2.18\,^\circ\text{C}$).
  - **Desarrollo 3 (Axioma 3 — Física antes que Algoritmo):** Se ilumina la tercera columna `"🚀 Próximo paso: física antes que algoritmo"`: el satélite óptico anual saturado (`NDVI ~0.74`, ciego al `-56.0%` de la roya en 2014) es superado por el balance hídrico en floración (`r = 0.7564`, `τ = 6–8 meses`).
  - **Cierre:** Las 3 tarjetas quedan alineadas en las mismas coordenadas del grid `.conclusions-3col-grid` de la Diapo 29 para un handoff imperceptible.
- **Cifras canónicas que deben aparecer, con fuente:**
  - Caso 1 (Punchana): `n = 2,557 días`, récord `38.0 °C` (`07·10·2023`), `σ = 2.18 °C` (`data/caso_1/senamhi_diario.csv`), `ExtraTrees` en CPU `0.25 s` con `RMSE 1.88 °C` (`data/caso_1/benchmark_punchana.csv`).
  - Caso 2 (Jaén): `N = 24 campañas` (`data/caso_2/cafe_jaen_campanias.csv`), caída de `-56.0%` (`10.0 qq/ha` en 2014) con `NDVI ~0.74` y correlación hídrica en floración `r = 0.7564` (`data/caso_2/cafe_jaen_hipotesis.json`).
- **Material base:**
  - Diapo origen: `front/deck_slides_p2.py` (líneas 235–264, `data-index="29"`).
  - Datos CSV/JSON: `data/caso_1/benchmark_punchana.csv` y `data/caso_2/cafe_jaen_hipotesis.json`.
  - Textos exactos: `"Conclusiones"`, `"🎯 Respeta la causalidad del tiempo"`, `"🧠 El valor está en la banda, no en el punto"`, `"🚀 Próximo paso: física antes que algoritmo"`.
- **Handoff:** Color de fondo exacto del slide destino `#03050F` (`--bg-dark: #03050F` en `front/deck_styles.py`); fade-in de `0.35 s` desde `#03050F` y cierre encajando con las 3 columnas de la Diapo 29.
- **Integración en el deck:** Se dispara al avanzar de la Diapo 28 (portada Sección 05) a la Diapo 29; al terminar hace fade-out suave dejando las 3 tarjetas DOM de la Diapo 29 activas.
- **Dependencias y prioridad:** Opcional; depende de haber completado primero los videos de teoría de las Secciones 1 y 3; prioridad **baja**.
- **Aceptación específica:**
  - [X] `ffprobe` valida `1920×1080` @ `30 fps`, `750 frames` (`25.0 s`), H.264 `yuv420p` `+faststart` — verificado (`25.000 s`, `750 f`, H.264 High, `2,076,140 B`).
  - [X] Fondo `#03050F` idéntico al de `front/deck_styles.py` en la Diapo 29 — `body` y fade-in del render usan `0x03050F`.
  - [X] Presenta los 3 títulos exactos (`"Respeta la causalidad del tiempo"`, `"El valor está en la banda, no en el punto"`, `"Próximo paso: física antes que algoritmo"`) con sus cifras verificadas — beats 01/02/03 con `RMSE 1.88 °C · 0.25 s`, `P10–P90 29.55–37.42 °C · q̂ = 3.09 °C` y `r = 0.7564 · NDVI +1.4% vs −56.0% (2014)`.
- **Estado:** `completado` — `sintesis_cierre.mp4` (25 s · 750 f · 1920×1080 @ 30 fps · 2.08 MB); cold de dos ondas (`n = 2,557` + `N = 24`) convergiendo en nodo común, ventanas rodantes de 6 folds, mini-cono P10–P90, NDVI vs. rendimiento, y cierre con las 3 tarjetas canónicas del grid de la Diapo 29 (`🎯 Respeta la causalidad del tiempo`, `🧠 El valor está en la banda, no en el punto`, `🚀 Próximo paso: física antes que algoritmo`); handoff `#03050F`.

---

### 9.8 Ficha 7: `video_trampa_ndvi` (Sección 4 · Diapo 26)
- **ID:** `video_trampa_ndvi` — `video/seccion_4/diapo_26/video_trampa_ndvi/`
- **Diapositiva:** Sección 4, Diapo 26, `"La trampa del satélite: NDVI vs estrés hídrico"` (Acto 4 · Trampa del NDVI)
- **Rol del video:** `"entrada"` (se reproduce al avanzar Diapo 25 → 26 y luego aparece la Diapo 26 interactiva)
- **Objetivo pedagógico:** Demostrar visualmente por qué el satélite óptico (`MODIS NDVI`, `250 m`) satura en las copas de árboles de sombra (`NDVI ~0.74`, `r = 0.1536, p = 0.600`) y fue ciego al colapso de `-56.0%` (`10.0 qq/ha`) en la epidemia de roya de 2014, mientras que el balance hídrico en la ventana fenológica de floración (`Ago–Oct`, `r = 0.7564, p = 0.002`) explica la variabilidad productiva real.
- **Duración objetivo:** `30 s` (`900 frames` @ 30 fps)
- **Guion por beats:**
  - **Cold-open:** Fade-in de `0.35 s` desde `#040812` con el título `"CASO 2 · LA TRAMPA DEL SATÉLITE: NDVI vs. ESTRÉS HÍDRICO"` y el subtítulo `"Jaén (Cajamarca) · 24 campañas (2001–2024) · MODIS 250 m vs. ERA5"`.
  - **Desarrollo 1 (Panel 1 — Anatomía del Falso Positivo Satelital):** El haz del satélite `MODIS Terra/Aqua (250 m)` rebota en el dosel superior de árboles de sombra (*Inga spp.*) y maleza devolviendo una lectura plana `"NDVI ~0.74 · CV = 2.32% (Dosel Saturado)"`, mientras bajo la sombra el cafeto sufre el choque de la roya en **`2014`** (`10.0 qq/ha · −56.0%` con `NDVI = 0.7483 · +1.4%`).
  - **Desarrollo 2 (Panel 2 — Duelo de Dispersión Empírica):** El lienzo se divide en dos diagramas de dispersión con los datos reales de `data/caso_2/cafe_jaen_campanias.csv`: a la izquierda, `ndvi_anual` vs. `rendimiento_qq_ha` muestra una nube sin pendiente (`r = 0.1536, p = 0.600 — Pendiente Nula`); a la derecha, `def_hidrico_flor_mm` (`P − PET` en `Ago–Oct`) ordena linealmente las campañas (`r = 0.7564, p = 0.002`, junto con `lluvia_flor_mm r = 0.7511`).
  - **Desarrollo 3 (Panel 3 — Contraste de Señal Biológica):** Barras comparativas de correlación con el rendimiento real en Jaén (`MODIS NDVI Anual: r = +0.1536 [Ruido Saturado]`, `Tmax Floración: r = −0.5606`, `Lluvia Floración Ago–Oct: r = +0.7511`, `Balance Hídrico Floración Ago–Oct: r = +0.7564`).
  - **Cierre:** Síntesis ejecutiva con las dos tarjetas `"SATÉLITE ÓPTICO ANUAL (NDVI ~0.74 · r = 0.154 · Ciego a Roya −56%)"` ⟷ `"CLIMA EN FLORACIÓN AGO–OCT (Déficit r = 0.756 · Lluvia r = 0.751)"` sobre `#040812`.
- **Cifras canónicas que deben aparecer, con fuente:**
  - `N = 24 campañas` (`2001–2024`), caída en **`2014`** a **`10.0 qq/ha`** (**`-56.0%`**) con **`NDVI = 0.7483`** (**`+1.4%`**) y pico de **`35.38 qq/ha`** en **`2020`** (fuente: `data/caso_2/cafe_jaen_campanias.csv` y `data/caso_2/cafe_jaen_hipotesis.json`).
  - Correlaciones auditadas: `NDVI anual r = 0.1536 (p = 0.600, CV = 2.32%)`, `Balance Hídrico Floración r = 0.7564 (p = 0.002)`, `Lluvia Floración r = 0.7511 (p = 0.002)`, `Tmax Floración r = −0.5606` (fuente: `data/caso_2/cafe_jaen_hipotesis.json`).
- **Material base:**
  - Prototipo destino: `docs/notebooklm/seccion_4/prototipos/26_Trampa_Satelite_NDVI_vs_Clima.html` (y `front/components/anatomy/anatomy_cafe_sombra_ndvi.svg`).
  - Datos CSV/JSON: `data/caso_2/cafe_jaen_campanias.csv` y `data/caso_2/cafe_jaen_hipotesis.json`.
  - Textos exactos: `"CASO 2 · LA TRAMPA DEL SATÉLITE"`, `"MODIS NDVI Anual: r = 0.1536 (p = 0.600 · Dosel Saturado)"`, `"2014: 10.0 qq/ha (−56.0%) con NDVI 0.7483 (+1.4%)"`, `"Balance Hídrico Floración (Ago–Oct): r = 0.7564 (p = 0.002)"`.
- **Handoff:** Color de fondo exacto del slide destino `#040812`; fade-in de `0.35 s` desde `#040812` y cierre con composición completa encendida.
- **Integración en el deck:** Se reproduce al avanzar de la Diapo 25 a la Diapo 26 (`#cinematicVideoGate26`); al terminar o pulsar `→` revela el simulador interactivo de la Diapo 26 y queda disponible en el botón `"🎬 Intro"`.
- **Dependencias y prioridad:** Se integra con `T10.6.2`; prioridad **alta**.
- **Aceptación específica:**
  - [X] `ffprobe` valida `1920×1080` @ `30 fps`, `900 frames` (`30.0 s`), H.264 `yuv420p` `+faststart` (3.46 MB, 900 f exactos).
  - [X] Los dos diagramas de dispersión usan los pares reales de `data/caso_2/cafe_jaen_campanias.csv` y destacan en coral el punto de `2014 (10.0 qq/ha · −56.0%)` sin solapar etiquetas con puntos ni rectas de tendencia.
  - [X] Todas las cifras coinciden exactamente con `data/caso_2/cafe_jaen_hipotesis.json` (`2014`, `0.7483`, `r = 0.1536`, `r = 0.7564`, `r = 0.7511`).
- **Estado:** `completado` — `trampa_ndvi.mp4` (30 s · 900 f · 1920×1080 @ 30 fps · 3.46 MB); integrado en `#cinematicVideoGate26` de Diapo 26 con handoff `#040812`.

---

### 9.9 Ficha 8: `video_walkforward_jaen` (Sección 4 · Diapo 27)
- **ID:** `video_walkforward_jaen` — `video/seccion_4/diapo_27/video_walkforward_jaen/`
- **Diapositiva:** Sección 4, Diapo 27, `"Demostración: validación Walk-Forward en Jaén"` (Acto 4 · Validación Jaén)
- **Rol del video:** `"entrada"` (se reproduce al avanzar Diapo 26 → 27 y luego aparece la Diapo 27 interactiva)
- **Objetivo pedagógico:** Mostrar cómo se evalúan honestamente 16 arquitecturas sobre muestras agrícolas pequeñas (`N = 24`) mediante **validación expansiva Walk-Forward sin fuga temporal** (`8 campañas de test: 2016, 2018–2024`), evidenciando el triunfo de la parsimonia fenológica (`Random Forest d=2 MAE = 3.72 qq/ha` y `Solo Déficit Hídrico MAE = 3.90 qq/ha`) frente al colapso del satélite óptico anual (`MAE = 5.45 qq/ha`, error de `18.25 qq/ha` en el récord de `2020`).
- **Duración objetivo:** `30 s` (`900 frames` @ 30 fps)
- **Guion por beats:**
  - **Cold-open:** Fade-in de `0.35 s` desde `#040812` con el título `"DEMOSTRACIÓN · VALIDACIÓN WALK-FORWARD EN JAÉN"` y el subtítulo `"8 campañas de prueba ciega (2016, 2018–2024) · 16 modelos enfrentados"`.
  - **Desarrollo 1 (Panel 1 — El Protocolo Walk-Forward Expansivo):** Se despliegan las 8 ventanas expansivas año a año (`Train ≤ t−1 ──▶ Test t` desde `2016` hasta `2024`), demostrando que ninguna cosecha futura contamina el entrenamiento.
  - **Desarrollo 2 (Panel 2 — Trayectorias Out-of-Sample y el Choque de 2020):** Se trazan las series reales de `data/caso_2/cafe_jaen_predicciones_modelos.csv`: la curva observada SIEA (`rendimiento_real`, que alcanza el récord de **`35.38 qq/ha`** en **`2020`**), seguida por `M12 Random Forest (d=2)` y `M08 Solo Déficit Hídrico`, mientras la curva roja `M05 Solo NDVI Anual (Saturado)` se queda estancada en `17.13 qq/ha` (`Error 2020 = 18.25 qq/ha`).
  - **Desarrollo 3 (Panel 3 — Podio del Benchmark de 16 Modelos):** Ranking horizontal con los errores `mae_walkforward` de `data/caso_2/benchmark_cafe.csv`: `1.° M12 Random Forest Parsimonioso (d=2): 3.72 qq/ha (45.2 ms CPU)`, `2.° M08 Solo Déficit Hídrico Floración: 3.90 qq/ha`, `3.° M16 Zero-Shot Heurístico: 4.12 qq/ha`, `5.° M11 ElasticNet Multimodal: 4.33 qq/ha` vs. `14.° M05 Solo NDVI Anual: 5.45 qq/ha (+31.7% peor)`.
  - **Cierre:** Tarjeta dual de síntesis `"FÍSICA FENOLÓGICA + ÁRBOLES (MAE 3.72–3.90 qq/ha)"` ⟷ `"SATÉLITE ÓPTICO SIN BIOLOGÍA (MAE 5.45 qq/ha · Error 18.25 en 2020)"` sobre `#040812`.
- **Cifras canónicas que deben aparecer, con fuente:**
  - 8 campañas de test Walk-Forward (`2016, 2018, 2019, 2020, 2021, 2022, 2023, 2024`) y récord observado en `2020` de **`35.38 qq/ha`** (fuente: `data/caso_2/cafe_jaen_predicciones_modelos.csv`).
  - Errores `MAE Walk-Forward` auditados sobre 16 modelos: `M12 Random Forest Parsimonioso (d=2) = 3.723 qq/ha` (`RMSE 5.41 qq/ha`, `45.16 ms CPU`), `M08 Solo Déficit Hídrico Floración = 3.903 qq/ha` (`RMSE 4.925 qq/ha`), `M16 Zero-Shot Heurístico = 4.116 qq/ha`, `M11 ElasticNet Multimodal = 4.332 qq/ha`, `M01 Persistencia Naive = 4.381 qq/ha`, `M05 Solo NDVI Anual (Saturado) = 5.448 qq/ha` (`error_abs_2020 = 18.25 qq/ha`) (fuente: `data/caso_2/benchmark_cafe.csv`).
- **Material base:**
  - Prototipo destino: `docs/notebooklm/seccion_4/prototipos/27_Validacion_WalkForward_Benchmark_Jaen.html`.
  - Datos CSV: `data/caso_2/benchmark_cafe.csv` y `data/caso_2/cafe_jaen_predicciones_modelos.csv`.
  - Textos exactos: `"VALIDACIÓN WALK-FORWARD EXPANSIVA (2016–2024)"`, `"M12: Random Forest Parsimonioso (d=2) · MAE 3.72 qq/ha"`, `"M08: Solo Déficit Hídrico Floración · MAE 3.90 qq/ha"`, `"M05: Solo NDVI Anual (Saturado) · MAE 5.45 qq/ha (Error 2020: 18.25 qq/ha)"`.
- **Handoff:** Color de fondo exacto del slide destino `#040812`; fade-in de `0.35 s` desde `#040812` y cierre con composición completa encendida.
- **Integración en el deck:** Se reproduce al avanzar de la Diapo 26 a la Diapo 27 (`#cinematicVideoGate27`); al terminar o pulsar `→` revela el simulador interactivo de la Diapo 27 y queda disponible en el botón `"🎬 Intro"`.
- **Dependencias y prioridad:** Se integra con `T10.6.2`; prioridad **media**.
- **Aceptación específica:**
  - [X] `ffprobe` valida `1920×1080` @ `30 fps`, `900 frames` (`30.0 s`), H.264 `yuv420p` `+faststart` (3.60 MB, 900 f exactos).
  - [X] Las trayectorias del Panel 2 grafican los valores exactos de `data/caso_2/cafe_jaen_predicciones_modelos.csv` (`2020 observado = 35.38 qq/ha`, `NDVI = 17.13 qq/ha`) con pastillas opacas que no tapan las curvas.
  - [X] Las barras del Panel 3 muestran los valores exactos de `data/caso_2/benchmark_cafe.csv` (`3.723`, `3.903`, `4.116`, `4.332`, `5.448 qq/ha`) sin recortar nombres de modelos.
- **Estado:** `completado` — `walkforward_jaen.mp4` (30 s · 900 f · 1920×1080 @ 30 fps · 3.60 MB); integrado en `#cinematicVideoGate27` de Diapo 27 con handoff `#040812`.



