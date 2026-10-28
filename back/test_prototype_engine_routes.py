"""
Archivo: test_prototype_engine_routes.py
Fecha de modificación: 28/10/2026
Autor: Alex Prieto Romani

Descripción:
    Valida las rutas corta/experta de front/prototype_engine.py (F12): CSS y helper
    inyectados cuando hay etapas marcadas, y la regex de respaldo que limpia rótulos
    de navegación entre diapositivas que ya no son clicables.

Acciones Principales:
    - Verifica la inyección del CSS y del helper con un fixture de 4 etapas.
    - Verifica que un prototipo sin `data-route` no recibe el helper.
    - Verifica la limpieza de "Asimetría ─▶ Diapo 11" y "Pase a Diapo 16 →".

Entradas / Dependencias:
    - front/prototype_engine.py

Salidas / Efectos:
    - Ninguna. Solo reporta resultados de pytest.

Ejecución:
    python -m pytest back/test_prototype_engine_routes.py -q
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from front.prototype_engine import (
    normalize_prototype_html,
    strip_internal_nav,
)

ROUTES = ("corta", "corta", "experta", "corta")
NODES = "".join(
    f'<button class="proc-node" data-route="{route}" data-step="s{i}" aria-selected="{str(i == 0).lower()}">'
    f'<span class="proc-year">Etapa {i}</span></button>'
    for i, route in enumerate(ROUTES)
)
FIXTURE_HTML = (
    "<html><head></head><body><nav>" + NODES + "</nav>"
    '<main id="slideFrame"><h1>Titulo</h1></main></body></html>'
)


def test_routes_css_and_helper_injected() -> None:
    """El motor inyecta el CSS de rutas y el helper cuando hay etapas con data-route."""
    result = normalize_prototype_html(FIXTURE_HTML, slide_num=10, section_num=1)
    assert 'html:not([data-expert]) [data-route="experta"]' in result
    assert 'id="deck-routes-js"' in result
    assert "// ponytail:" in result


def test_routes_not_injected_without_marks() -> None:
    """Sin etapas marcadas no se inyecta helper ni CSS de rutas."""
    result = normalize_prototype_html("<html><head></head><body><h1>X</h1></body></html>", 11, 1)
    assert "deck-routes-js" not in result
    assert "deck-routes-css" not in result


def test_nav_text_fallback_cleans_stage_labels() -> None:
    """La regex de respaldo quita rótulos de pase a otra diapositiva en texto visible."""
    cleaned = strip_internal_nav('<span class="proc-year">Asimetría ─▶ Diapo 11</span>')
    assert cleaned == '<span class="proc-year">Asimetría</span>'
    cleaned = strip_internal_nav("<span>Pase a Diapo 16 →</span><i>Puente a la Diapositiva 3</i>")
    assert "Diapo" not in cleaned


def test_nav_text_fallback_keeps_following_line() -> None:
    """La regex de respaldo no consume el salto de línea que sigue a un comentario JS."""
    source = "// Banner de pase a la Diapositiva 20\nconst bannerY = 1;"
    assert "\nconst bannerY = 1;" in strip_internal_nav(source)
