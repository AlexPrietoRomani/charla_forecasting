"""
Archivo: test_prototype_engine_hero.py
Fecha de modificación: 28/10/2026
Autor: Alex Prieto Romani

Descripción:
    Valida los pasos de claridad de front/prototype_engine.py (F12): promoción de la
    Idea Clave a titular héroe, eliminación de la navegación interna entre diapositivas
    y unificación de taxonomías (VÍA, Era, Pilar, Etapa, Acto) en cabeceras y fichas.

Acciones Principales:
    - Verifica el titular héroe con kicker, título y subtítulo desde un fixture.
    - Verifica que strip_internal_nav conserva un marcador oculto si el JS usa el id.
    - Verifica que unify_taxonomy limpia rótulos sin dejar separadores dobles.

Estructura Interna:
    - `FIXTURE_HTML`: Prototipo mínimo con cabecera, barra de etapas, ficha y botones.
    - `test_promote_takeaway_to_hero_builds_kicker_title_sub`: Comprueba el titular.
    - `test_strip_internal_nav_*`: Comprueban la eliminación de botones de navegación.
    - `test_unify_taxonomy_*`: Comprueban la limpieza de taxonomías.
    - `test_normalize_applies_all_steps`: Comprueba el encadenado en el motor.

Entradas / Dependencias:
    - front/prototype_engine.py

Salidas / Efectos:
    - Ninguna. Solo reporta resultados de pytest.

Ejecución:
    python -m pytest back/test_prototype_engine_hero.py -q
"""

import re
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from front.prototype_engine import (
    normalize_prototype_html,
    promote_takeaway_to_hero,
    strip_internal_nav,
    unify_taxonomy,
)

FIXTURE_HTML = """<!doctype html>
<html><head><title>t</title></head>
<body>
<main id="slideFrame">
  <header class="topbar">
    <div>
      <p class="eyebrow">Cuando la fórmula no alcanza</p>
      <h1>De series a tablas: <span class="era">el puente</span></h1>
    </div>
    <div class="via-card"><div class="via-title"><span>FICHA OPERATIVA VÍA 2</span></div></div>
  </header>
  <nav>
    <button class="proc-node"><span class="proc-year">Quiebre ─▶ Era 2</span></button>
    <button class="proc-node"><span class="step-title">Etapa 3 de 4 · Redes</span></button>
  </nav>
  <aside>
    <div class="executive-takeaway" id="speakerBox">
      <strong>💡 Idea Clave:</strong> <span id="speakerQuote">Deslizar ventanas convierte una serie en tabla.</span>
    </div>
    <button id="goNext" type="button">Pase a Diapo 16 →</button>
    <button type="button">Ir al Caso Jaén →</button>
    <button id="keep" type="button">Siguiente etapa</button>
  </aside>
</main>
<script>document.getElementById('goNext').addEventListener('click', function () {});</script>
</body></html>"""


def test_promote_takeaway_to_hero_builds_kicker_title_sub():
    out = promote_takeaway_to_hero(FIXTURE_HTML, acto=1, diapo=7)
    assert '<div class="hero-kicker">Acto 1 · Diapo 7 · Cuando la fórmula no alcanza</div>' in out
    assert (
        '<h1 class="hero-title" data-hero-src="speakerQuote">'
        "Deslizar ventanas convierte una serie en tabla.</h1>"
    ) in out
    assert '<div class="hero-sub">De series a tablas: el puente</div>' in out
    assert '<header class="topbar hero">' in out
    assert '<body class="has-hero">' in out
    assert out.count("<h1") == 1


def test_promote_takeaway_to_hero_without_message_is_noop():
    doc = "<body><h1>Solo título</h1></body>"
    assert promote_takeaway_to_hero(doc, acto=2, diapo=12) == doc


def test_strip_internal_nav_removes_button_without_js_reference():
    out = strip_internal_nav(FIXTURE_HTML)
    assert "Ir al Caso" not in out
    assert "Siguiente etapa" in out


def test_strip_internal_nav_keeps_hidden_id_used_by_js():
    out = strip_internal_nav(FIXTURE_HTML)
    assert "Pase a Diapo" not in out
    assert '<button id="goNext" hidden></button>' in out
    assert "getElementById('goNext')" in out


def test_unify_taxonomy_cleans_labels_without_double_separators():
    doc = (
        '<span class="step-title">VÍA 3 · Deep Learning</span>'
        '<span class="proc-year">Quiebre ─▶ Era 2</span>'
        '<span class="stage-tag">Etapa 1 de 4 · · Lags</span>'
        '<span class="eyebrow">Pilar 2 de 4</span>'
    )
    out = unify_taxonomy(doc)
    assert '<span class="step-title">Deep Learning</span>' in out
    assert '<span class="proc-year">Quiebre</span>' in out
    assert '<span class="stage-tag">Lags</span>' in out
    assert '<span class="eyebrow"></span>' in out
    assert not re.search(r"\b(VÍA|Era|Pilar|Etapa)\s+\d", out)


def test_unify_taxonomy_ignores_body_text():
    doc = '<p class="lead">Fue la Era 2 del pronóstico.</p>'
    assert unify_taxonomy(doc) == doc


def test_normalize_applies_all_steps():
    out = normalize_prototype_html(FIXTURE_HTML, slide_num=7, section_num=1)
    assert "hero-title" in out
    assert "Pase a Diapo" not in out
    assert "FICHA OPERATIVA VÍA" not in out
    assert 'id="deck-hero-css"' in out
    assert 'id="deck-hero-js"' in out
