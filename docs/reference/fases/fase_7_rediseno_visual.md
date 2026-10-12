# Fase 7: Rediseño Visual (Front-Design) — Márgenes, Densidad y Cero Espacios Vacíos

> **Documento de Fase:** `docs/reference/fases/fase_7_rediseno_visual.md`  
> **Archivos a tocar:** `scripts/deck_styles.py`, `scripts/deck_slides_p1.py`, `scripts/deck_slides_p2.py`, `scripts/build_deck.py`  
> **Herramientas:** `scripts/audit_layout.py` (capturas 1920×1080 en `docs/audit_layout/`), skill de front-design (si el usuario la provee/activa), skill `visualizar-datos`  
> **Estado:** `[ ] Pendiente de Ejecución` (**NO ejecutar hasta visto bueno explícito del usuario**)

---

## 1. Diagnóstico (revisión en navegador, 20 diapositivas @1920×1080)

| # | Problema | Diapositivas afectadas | Causa |
|---|----------|------------------------|-------|
| P1 | Márgenes externos casi nulos (~24 px): las tarjetas tocan el borde del viewport arriba, abajo y a los lados. | Todas | `.slide` sin padding propio; paneles pegados al marco. |
| P2 | Panel izquierdo con vacío de ~350 px entre la tarjeta "insight" y la frase-clave. | Todas (más notorio en 02, 03, 05, 08, 15, 19) | Frase-clave anclada al fondo (`margin-top:auto`) y poco contenido intermedio. |
| P3 | Tarjetas estiradas (`flex:1`) con texto diminuto (11–13 px) y 60 % de la caja vacía. | 03, 06, 18, 19, 20 | Grids/columnas que estiran alto sin escalar tipografía ni contenido. |
| P4 | Visual centrado y diminuto sobre fondo vacío. | 01 (cono), 09 (donut fenológico), 11 (malla icosaédrica + métricas), 06 (cajas LSTM/PatchTST) | SVG con tamaño fijo en contenedor `flex:1`. |
| P5 | Textos del visual ilegibles a distancia (9–12 px mono). | 03, 08, 11, 18, 19, 20 | Tipografía pensada para pantalla, no para proyector. |
| P6 | Infografías NotebookLM pequeñas (≈370 px de ancho) dentro de caja de 1100 px. | 02, 08, 15 | `max-height:210px` + `object-fit:contain`. |
| P7 | Etiquetas solapadas en SVG (`COSECHA (Mar-Jul)` pisa el donut; en 08 `NDVI ~0.80` pisa `ZONA SATURACIÓN`). | 08, 09 | Posiciones absolutas fijas. |
| P8 | Gráficos con 60 % del alto sin aprovechar jerarquía (títulos, KPIs, anotaciones). | 05, 10, 13, 14, 17 | Solo canvas, sin KPIs ni callouts alrededor. |

> Nota: la métrica automática de `audit_layout.py` mide vacío por panel; el diagnóstico definitivo es visual (capturas en `docs/audit_layout/`).

---

## 2. Principios de Diseño (Front-Design)

1. **Marco de diapositiva:** padding externo del deck `clamp(28px, 3.2vw, 64px)` lados y `clamp(20px, 2.6vh, 40px)` arriba/abajo; esquinas 20 px; sombra suave. El contenido nunca toca el borde.
2. **Escala tipográfica proyector:** cuerpo ≥ 16 px, etiquetas mono ≥ 13 px, títulos de visual ≥ 22 px, KPIs 40–64 px (Space Grotesk). Usar `clamp()` con `vw/vh`.
3. **Jerarquía por diapositiva:** 1 elemento héroe (≥ 55 % del área visual), 1–3 KPIs de apoyo, 1 anotación. Prohibido "caja con 3 líneas pequeñas".
4. **Relleno inteligente, no relleno vacío:** si falta contenido, agregar KPI gigante, mini-gráfico (sparkline/SVG), línea de tiempo o dato de contraste real; **jamás datos inventados** (solo SENAMHI, SIEA/MIDAGRI, MODIS, ERA5, papers citados).
5. **Panel izquierdo compacto y centrado verticalmente:** bloque (badge → título → tesis → chips → viñetas → insight) con `justify-content: space-between` y frase-clave como tarjeta destacada de ≥ 90 px; sin vacío > 80 px.
6. **Grillas con proporción de contenido:** `grid-auto-rows: minmax(0,1fr)` + contenido centrado/escalado; tarjetas con icono/número grande en lugar de solo texto.
7. **Movimiento:** conservar resortes `cubic-bezier(0.16,1,0.3,1)` y stagger; respetar `prefers-reduced-motion`.

---

## 3. Subfases y Tareas

### SF7.1 Marco global y sistema de espaciado (`deck_styles.py`)
- [ ] **T7.1.1** Definir tokens CSS: `--deck-pad-x`, `--deck-pad-y`, `--gap-lg`, `--radius-card`, escala tipográfica con `clamp()`.
- [ ] **T7.1.2** Aplicar padding externo a `.slide` (márgenes laterales, superior e inferior) y ajustar altura útil (`100vh - nav`).
- [ ] **T7.1.3** Rebalancear split (≈ 38 / 62) con `gap` entre paneles; panel izquierdo con scroll oculto y sin vacíos > 80 px.
- [ ] **T7.1.4** Rediseñar `.card-frase-clave` como tarjeta destacada (tamaño de cita ≥ 20 px, acento de color por acto).
- [ ] **T7.1.5** Subir tipografía base y de etiquetas mono; verificar 1920×1080, 1600×900 y 1366×768.

### SF7.2 Rediseño por diapositiva (relleno con propósito)
- [ ] **T7.2.1** Slide 01: cono de incertidumbre a ancho completo del visual + 3 KPIs (2,557 días, 24 campañas, horizonte 7 d) bajo el gráfico.
- [ ] **T7.2.2** Slide 02: infografía NotebookLM grande (≥ 60 % ancho, clic para ampliar) + simulador Canvas debajo en altura proporcional.
- [ ] **T7.2.3** Slide 03: tarjetas de 4 eras con año gigante, mini-icono SVG del mecanismo, fórmula en ≥ 15 px y barra de "datos requeridos / cómputo".
- [ ] **T7.2.4** Slide 04: leer código real y escalar el visual (α-bars y curva logística) a ancho completo con ejes legibles.
- [ ] **T7.2.5** Slide 05: añadir franja de KPIs (34.0 / 37.4 / 31.5 / 35.45 °C) sobre el gráfico; leyenda en una sola línea.
- [ ] **T7.2.6** Slide 06: diagramas LSTM vs PatchTST animados a escala completa (celdas ≥ 56 px, flechas animadas, conteo 336 → 42 tokens).
- [ ] **T7.2.7** Slide 07: tabla de Foundation Models con tipografía ≥ 15 px y fila destacada por modelo.
- [ ] **T7.2.8** Slide 08: reordenar a 3 bandas (infografía grande → 2 SVG grandes → nota); corregir solapes de etiquetas NDVI/zona saturada.
- [ ] **T7.2.9** Slide 09: donut fenológico ≥ 420 px con etiquetas fuera del anillo (sin solapes) + línea de tiempo mensual; tarjetas inferiores más altas.
- [ ] **T7.2.10** Slide 10: gráfico NOAA vs ECMWF + KPI de discrepancia media (dato de `data/caso_1/noaa_ecmwf_forecast.csv`).
- [ ] **T7.2.11** Slide 11: malla icosaédrica ≥ 420 px (icosaedro/geodésica SVG animada) y métricas ECMWF vs GraphCast con números ≥ 56 px, apiladas sin vacío.
- [ ] **T7.2.12** Slides 12–14: KPIs sobre/bajo canvas (RMSE, MAE, ganador por parsimonia) leídos desde `benchmark_punchana.csv`.
- [ ] **T7.2.13** Slide 15: infografía de dron grande + HUD de telemetría; serie SIEA con anotaciones (2014 roya, 2020 pico).
- [ ] **T7.2.14** Slides 16–17: scatter/validación con KPIs (correlación H1, MAE por modelo) y callouts; ocupar el alto completo.
- [ ] **T7.2.15** Slides 18–20: tarjetas de lecciones/decisión/cierre con numeral gigante (01–05), icono, texto ≥ 18 px; QR del repositorio ≥ 180 px.

### SF7.3 Re-uso de activos NotebookLM
- [ ] **T7.3.1** Recortar de `docs/notebooklm/slides/` fragmentos útiles (ej. cuadrantes/figuras) a `docs/notebooklm/crops/` en alta resolución y usarlos donde enriquezcan (02, 03, 08, 15).
- [ ] **T7.3.2** Lightbox con clic para ampliar infografías (zoom con resorte).

### SF7.4 QA Visual Automatizado y Manual
- [ ] **T7.4.1** Extender `scripts/audit_layout.py`: medir por slide (a) margen externo ≥ token, (b) vacío vertical máximo contiguo ≤ 80 px en panel izquierdo, (c) ocupación del visual ≥ 85 %, (d) texto mínimo ≥ 13 px, (e) solapes entre `text/label`.
- [ ] **T7.4.2** Capturas 1920×1080, 1600×900 y 1366×768 en claro y oscuro; revisar las 20 diapositivas en el navegador.
- [ ] **T7.4.3** Verificar 0 errores de consola y que cada canvas/SVG tenga datos (`verify_presentation.py`).
- [ ] **T7.4.4** Registrar en `docs/logs/log.md` el rediseño y lecciones; actualizar `docs/presentacion_slides_texto.md` si cambia texto.

---

## 4. Criterios de Aceptación (DoD Fase 7)
- [ ] Margen externo visible en los 4 lados en todas las diapositivas.
- [ ] Ningún bloque vacío contiguo > 80 px dentro de paneles; ningún visual centrado y pequeño (< 55 % del área).
- [ ] Texto mínimo ≥ 13 px y cuerpo ≥ 16 px a 1920×1080; sin solapes de etiquetas.
- [ ] Todas las cifras nuevas trazables a `data/*.csv|json` o fuentes citadas (cero datos sintéticos).
- [ ] 0 warnings de consola; funciona en claro/oscuro y en 1366×768.
- [ ] Visto bueno del usuario tras revisión visual en navegador.
