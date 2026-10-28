"""
Archivo: test_prototype_engine_glossary.py
Fecha de modificación: 28/10/2026
Autor: Alex Prieto Romani

Descripción:
    Valida el inyector de glosario de front/prototype_engine.py: marca solo la primera
    mención visible por bloque de etapa, respeta script, style, atributos y titulares,
    y escapa las comillas de los atributos data-def y data-analogia.

Acciones Principales:
    - Verifica el marcado de texto visible y la omisión de zonas no visibles.
    - Verifica el reinicio de la primera aparición por tarjeta .stage-card.
    - Verifica el escape de atributos y la idempotencia del inyector.

Estructura Interna:
    - `FIXTURE_HTML`: Prototipo mínimo con etapa, script, atributo y titular.
    - `test_marks_first_visible_occurrence_per_stage`: Comprueba el marcado por etapa.
    - `test_skips_script_style_attributes_and_headings`: Comprueba las zonas excluidas.
    - `test_escapes_quotes_in_data_attributes`: Comprueba el escape de comillas.
    - `test_without_stages_marks_first_per_document`: Comprueba el bloque único.
    - `test_alias_resolves_to_canonical_definition`: Comprueba la resolución de alias.
    - `test_inject_is_idempotent`: Comprueba que una segunda pasada no re-marca.

Entradas / Dependencias:
    - front/prototype_engine.py

Salidas / Efectos:
    - Ninguna. Solo reporta resultados de pytest.

Ejecución:
    python -m pytest back/test_prototype_engine_glossary.py -q
"""

import html
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from front.prototype_engine import (
    ENGINE_GLOSSARY_CSS,
    ENGINE_GLOSSARY_JS,
    inject_glossary,
    normalize_prototype_html,
)

FIXTURE_HTML = """<!doctype html>
<html>
<head>
<title>Fixture</title>
<style>.x { color: red; } /* p-valor dentro de CSS */</style>
</head>
<body>
<h1>Análisis del p-valor</h1>
<div class="stage-card">
  <p>El p-valor indica azar. Luego el p-valor vuelve a aparecer.</p>
  <span title="p-valor">texto</span>
  <script>var t = "p-valor";</script>
  <p>Mira el NDVI y la cosecha.</p>
</div>
<div class="stage-card">
  <p>Otra etapa menciona el p-valor otra vez.</p>
</div>
</body>
</html>"""

FIXTURE_NO_STAGE = """<html><body>
<p>El NDVI sube. El NDVI baja.</p>
<p>Y el NDVI cierra el día.</p>
</body></html>"""


def test_marks_first_visible_occurrence_per_stage() -> None:
    """Marca solo la primera mención visible de cada término dentro de cada etapa."""
    result = inject_glossary(FIXTURE_HTML)

    stage_one, stage_two = result.split('<div class="stage-card">')[1:3]
    assert stage_one.count('class="gl-term"') == 2  # p-valor + NDVI, cada uno una vez
    assert stage_two.count('class="gl-term"') == 1  # nueva etapa, primera mención otra vez


def test_skips_script_style_attributes_and_headings() -> None:
    """No marca texto dentro de script, style, atributos ni del titular h1."""
    result = inject_glossary(FIXTURE_HTML)

    assert 'var t = "p-valor";' in result
    assert "/* p-valor dentro de CSS */" in result
    assert 'title="p-valor"' in result
    assert '<h1>Análisis del p-valor</h1>' in result


def test_escapes_quotes_in_data_attributes() -> None:
    """Escapa comillas dobles y simples en data-def y data-analogia."""
    glossary = {"demo": {"def": 'Dice "hola" y \'adiós\'', "analogia": "como <tag>"}}
    result = inject_glossary("<p>Esto es demo.</p>", glossary)

    assert 'data-def="Dice &quot;hola&quot; y &#x27;adiós&#x27;"' in result
    assert 'data-analogia="como &lt;tag&gt;"' in result
    assert html.unescape('data-def="Dice &quot;hola&quot;') == 'data-def="Dice "hola"'


def test_without_stages_marks_first_per_document() -> None:
    """Sin tarjetas de etapa, el documento completo forma un solo bloque."""
    result = inject_glossary(FIXTURE_NO_STAGE)

    assert result.count('class="gl-term"') == 1
    assert result.count("NDVI") == 3


def test_alias_resolves_to_canonical_definition() -> None:
    """Un alias marca el texto original con la definición de la clave canónica."""
    result = inject_glossary("<p>El pronóstico sale hoy.</p>")

    assert 'class="gl-term"' in result
    assert "pronóstico</span>" in result
    assert 'data-def="Predicción de valores futuros a partir del historial de datos."' in result


def test_inject_is_idempotent() -> None:
    """Una segunda pasada sobre el mismo HTML no añade marcas nuevas."""
    once = inject_glossary(FIXTURE_HTML)
    twice = inject_glossary(once)

    assert once == twice


def test_tooltip_is_single_fixed_element_in_body() -> None:
    """Usa un único #gl-tip fijo en body, sin ::after ni clases de recolocación."""
    normalized = normalize_prototype_html(FIXTURE_HTML, slide_num=15, section_num=2)

    assert 'tip.id = "gl-tip"' in ENGINE_GLOSSARY_JS
    assert 'id="gl-tip"' not in normalized  # se crea en runtime, una sola vez
    assert "deck-glossary-js" in normalized and "deck-glossary-css" in normalized
    assert "::after" not in ENGINE_GLOSSARY_CSS and "::after" not in ENGINE_GLOSSARY_JS
    assert "gl-right" not in ENGINE_GLOSSARY_JS and "gl-up" not in ENGINE_GLOSSARY_JS
    assert "position: fixed" in ENGINE_GLOSSARY_CSS
