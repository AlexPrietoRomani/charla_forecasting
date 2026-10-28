"""Pruebas de las reglas de la auditoría F12 con fixtures mínimos en tmp_path.

Cada regla debe fallar ante una violación concreta y pasar ante un HTML limpio.
"""

import base64
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))

from audit_f12_claridad import (
    LIMITE_SIN_TOOLTIP,
    PROTOTIPOS,
    check_bundle,
    check_cifras,
    check_glosario,
    check_inventario,
    check_jerarquia,
    check_titulares,
    check_video,
    main,
)

HTML_LIMPIO = """<!doctype html>
<html><head><style>.x { font-size: 40px; }</style>
<script>var t = "lyapunov lyapunov";</script></head>
<body>
<h1>Cómo el agro inventó el forecasting</h1>
<p class="eyebrow">Sección 3</p>
<p>La <span class="gl-term" data-def="ver">lyapunov</span> aparece aquí.</p>
<p>Datos: <span data-expert>1.880</span> casos en <code>0.1234</code>.</p>
<p>Ubicación -3.69° S, año 2013.</p>
<div class="executive-takeaway">Las cifras crecen cuando el clima cambia de forma rápida.</div>
</body></html>
"""


def _escribir(ruta: Path, contenido: str) -> Path:
    """Crea el archivo con su directorio padre y devuelve la ruta."""
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(contenido, encoding="utf-8")
    return ruta


def _ok_o_fallo(filas: list[tuple[bool, str]]) -> list[bool]:
    """Extrae solo el estado booleano de cada fila de resultado."""
    return [ok for ok, _ in filas]


@pytest.fixture
def prototipo(tmp_path: Path) -> Path:
    """Crea la ruta de un prototipo bajo la raíz temporal y lo devuelve vacío."""
    return tmp_path / PROTOTIPOS[0]


def test_html_limpio_pasa_todas_las_reglas_de_html(
    tmp_path: Path, prototipo: Path
) -> None:
    """Verifica que un HTML sin violaciones pasa inventario, cifras, titulares y jerarquía."""
    _escribir(prototipo, HTML_LIMPIO)
    archivos = [prototipo]
    assert all(_ok_o_fallo(check_inventario(tmp_path, archivos)))
    assert all(_ok_o_fallo(check_cifras(tmp_path, archivos)))
    assert all(_ok_o_fallo(check_titulares(tmp_path, archivos)))
    assert all(_ok_o_fallo(check_jerarquia(tmp_path, archivos)))


def test_inventario_falla_con_jerga_sin_tooltip(
    tmp_path: Path, prototipo: Path
) -> None:
    """Verifica que más de 25 términos sin tooltip produce FAIL."""
    cuerpo = " ".join(["lyapunov"] * (LIMITE_SIN_TOOLTIP + 1))
    _escribir(prototipo, f"<html><body><p>{cuerpo}</p></body></html>")
    assert False in _ok_o_fallo(check_inventario(tmp_path, [prototipo]))


def test_inventario_pasa_en_el_limite(tmp_path: Path, prototipo: Path) -> None:
    """Verifica que exactamente 25 términos sin tooltip todavía pasa."""
    cuerpo = " ".join(["lyapunov"] * LIMITE_SIN_TOOLTIP)
    _escribir(prototipo, f"<html><body><p>{cuerpo}</p></body></html>")
    assert all(_ok_o_fallo(check_inventario(tmp_path, [prototipo])))


def test_cifras_falla_con_1880_fuera_de_data_expert(
    tmp_path: Path, prototipo: Path
) -> None:
    """Verifica que 1.880 visible sin data-expert produce FAIL."""
    _escribir(prototipo, "<html><body><p>Hay 1.880 casos.</p></body></html>")
    filas = check_cifras(tmp_path, [prototipo])
    assert False in _ok_o_fallo(filas)
    assert "1.880" in filas[0][1]


def test_cifras_acepta_1880_dentro_de_data_expert(
    tmp_path: Path, prototipo: Path
) -> None:
    """Verifica que 1.880 dentro de data-expert o code no produce FAIL."""
    _escribir(
        prototipo,
        '<html><body><p><span data-expert="1">1.880</span> <code>1.880</code></p></body></html>',
    )
    assert all(_ok_o_fallo(check_cifras(tmp_path, [prototipo])))


def test_jerarquia_falla_con_boton_pase_a(tmp_path: Path, prototipo: Path) -> None:
    """Verifica que un botón de navegación interna produce FAIL."""
    _escribir(
        prototipo,
        '<html><body><button class="nav">Pase a la siguiente</button></body></html>',
    )
    assert False in _ok_o_fallo(check_jerarquia(tmp_path, [prototipo]))


def test_jerarquia_falla_con_via_3_en_h1(tmp_path: Path, prototipo: Path) -> None:
    """Verifica que una taxonomía vieja como VÍA 3 en h1 produce FAIL."""
    _escribir(prototipo, "<html><body><h1>VÍA 3 de 4</h1></body></html>")
    assert False in _ok_o_fallo(check_jerarquia(tmp_path, [prototipo]))


def test_jerarquia_cuenta_rutas_cortas(tmp_path: Path, prototipo: Path) -> None:
    """Verifica que más de tres etapas con data-route=corta produce FAIL."""
    etapas = "".join(
        f'<div class="stage" data-route="corta">{i}</div>' for i in range(4)
    )
    _escribir(prototipo, f"<html><body>{etapas}</body></html>")
    assert False in _ok_o_fallo(check_jerarquia(tmp_path, [prototipo]))


def test_titulares_falla_con_hero_largo_y_takeaway_largo(
    tmp_path: Path, prototipo: Path
) -> None:
    """Verifica que hero-title de 13 palabras y takeaway de 16 producen FAIL."""
    hero = " ".join(["palabra"] * 13)
    take = " ".join(["idea"] * 16)
    _escribir(
        prototipo,
        f'<html><body><div class="hero-title">{hero}</div>'
        f'<div class="executive-takeaway">{take}</div></body></html>',
    )
    assert _ok_o_fallo(check_titulares(tmp_path, [prototipo])).count(False) == 2


def test_titulares_informa_pendiente_sin_hero(tmp_path: Path, prototipo: Path) -> None:
    """Verifica que la ausencia de hero-title informa pendiente sin FAIL."""
    _escribir(prototipo, "<html><body><h1>Título corto</h1></body></html>")
    filas = check_titulares(tmp_path, [prototipo])
    assert all(_ok_o_fallo(filas))
    assert any("pendiente T12.2.1" in d for _, d in filas)


def test_glosario_falla_si_falta_el_archivo(tmp_path: Path) -> None:
    """Verifica que sin front/deck_glossary.py el glosario falla con mensaje claro."""
    filas = check_glosario(tmp_path, [])
    assert filas[0][0] is False
    assert "deck_glossary.py" in filas[0][1]


def test_glosario_valida_definiciones_y_analogias(tmp_path: Path) -> None:
    """Verifica que definiciones largas o analogías vacías producen FAIL."""
    _escribir(
        tmp_path / "front" / "deck_glossary.py",
        "GLOSSARY = {\n"
        "    'lag': {'def': ' '.join(['x'] * 16), 'analogia': 'algo'},\n"
        "    'mae': {'def': 'error medio', 'analogia': ''},\n"
        "}\n"
        "def terms():\n    return ['lag', 'mae']\n",
    )
    filas = check_glosario(tmp_path, [])
    assert _ok_o_fallo(filas).count(False) >= 2


def test_glosario_pasa_con_entradas_validas(tmp_path: Path) -> None:
    """Verifica que un glosario válido sin términos frecuentes pendientes pasa."""
    _escribir(
        tmp_path / "front" / "deck_glossary.py",
        "GLOSSARY = {'lag': {'def': 'Retraso temporal.', 'analogia': 'Eco del pasado.'}}\n",
    )
    assert all(_ok_o_fallo(check_glosario(tmp_path, [])))


def test_video_falla_con_font_size_12px(tmp_path: Path) -> None:
    """Verifica que font-size de 12px literal produce FAIL."""
    _escribir(
        tmp_path / "video/seccion_1/diapo_1/video_x/scene_template.html",
        "<style>.t { font-size: 12px; }</style>",
    )
    assert False in _ok_o_fallo(check_video(tmp_path))


def test_video_ignora_font_size_en_clamp(tmp_path: Path) -> None:
    """Verifica que font-size con clamp() no produce FAIL aunque incluya px."""
    _escribir(
        tmp_path / "video/seccion_1/diapo_1/video_x/scene_template.html",
        "<style>.t { font-size: clamp(12px, 3vw, 40px); }</style>",
    )
    assert False not in _ok_o_fallo(check_video(tmp_path))


def test_video_falla_si_falta_beats_en_una_carpeta(tmp_path: Path) -> None:
    """Verifica que una escena sin beats.json ni narration.vtt produce FAIL si otra sí los tiene."""
    estilo = "<style>.t { font-size: 24px; }</style>"
    carpeta_a = tmp_path / "video/seccion_1/diapo_1/video_a"
    carpeta_b = tmp_path / "video/seccion_1/diapo_2/video_b"
    _escribir(carpeta_a / "scene_template.html", estilo)
    _escribir(carpeta_b / "scene_template.html", estilo)
    _escribir(carpeta_a / "beats.json", "[]")
    _escribir(carpeta_a / "narration.vtt", "WEBVTT")
    assert False in _ok_o_fallo(check_video(tmp_path))


def test_video_informa_pendiente_si_faltan_en_todas(tmp_path: Path) -> None:
    """Verifica que sin beats.json ni narration.vtt en ninguna escena solo informa."""
    _escribir(
        tmp_path / "video/seccion_1/diapo_1/video_a/scene_template.html",
        "<style>.t { font-size: 24px; }</style>",
    )
    filas = check_video(tmp_path)
    assert all(_ok_o_fallo(filas))
    assert any("T12.3.2" in d for _, d in filas)


def test_video_falla_con_capturas_duplicadas(tmp_path: Path) -> None:
    """Verifica que dos capture.mjs con el mismo contenido producen FAIL."""
    _escribir(tmp_path / "video/a/capture.mjs", "export {}")
    _escribir(tmp_path / "video/b/capture.mjs", "export {}")
    assert False in _ok_o_fallo(check_video(tmp_path))


def test_video_falla_con_mp4_versionado(tmp_path: Path) -> None:
    """Verifica que un mp4 con sufijo _v<n> en el disco produce FAIL sin repo git."""
    _escribir(tmp_path / "video/a/anatomia_v2_30s.mp4", "binario")
    assert False in _ok_o_fallo(check_video(tmp_path))


def test_main_devuelve_1_ante_fallo_y_0_con_solo_informar(tmp_path: Path) -> None:
    """Verifica el código de salida: 1 ante FAIL y 0 cuando cifras solo informa."""
    assert main(["--cifras", "--root", str(tmp_path)]) == 1
    assert main(["--cifras", "--solo-informar", "--root", str(tmp_path)]) == 0


def test_main_sin_reglas_devuelve_1(tmp_path: Path) -> None:
    """Verifica que invocar sin reglas devuelve 1 y muestra la ayuda."""
    assert main(["--root", str(tmp_path)]) == 1


def test_cifras_separador_de_miles_pasa_y_1880_falla(
    tmp_path: Path, prototipo: Path
) -> None:
    """Verifica que 30,490 es separador de miles (OK) y 1.880 sigue siendo FAIL."""
    _escribir(prototipo, "<html><body><p>Caso 30,490 frente a 1.880.</p></body></html>")
    filas = check_cifras(tmp_path, [prototipo])
    assert filas[0][0] is False
    assert "1.880" in filas[0][1]
    assert "30,490" not in filas[0][1]


def test_glosario_alias_cuenta_como_termino_canonico(
    tmp_path: Path, prototipo: Path
) -> None:
    """Verifica que 'lags' con alias de 'lag' no aparece como sin entrada."""
    _escribir(
        tmp_path / "front" / "deck_glossary.py",
        "GLOSSARY = {'lag': {'def': 'Retraso temporal.', 'analogia': 'Eco.', "
        "'alias': ['lags']}}\n"
        "def terms():\n    return ['lag', 'lags']\n",
    )
    _escribir(prototipo, "<html><body><p>lags lags lags</p></body></html>")
    filas = check_glosario(tmp_path, [prototipo])
    assert all(_ok_o_fallo(filas))


def test_glosario_sin_alias_falla_por_termino_frecuente(
    tmp_path: Path, prototipo: Path
) -> None:
    """Verifica que un término frecuente sin entrada ni alias sigue en FAIL."""
    _escribir(
        tmp_path / "front" / "deck_glossary.py",
        "GLOSSARY = {'lag': {'def': 'Retraso temporal.', 'analogia': 'Eco.'}}\n"
        "def terms():\n    return ['lag', 'lags']\n",
    )
    _escribir(prototipo, "<html><body><p>lags lags lags</p></body></html>")
    assert False in _ok_o_fallo(check_glosario(tmp_path, [prototipo]))


def test_titulares_excluye_etiqueta_idea_clave(tmp_path: Path, prototipo: Path) -> None:
    """Verifica que la etiqueta 'Idea Clave' no suma palabras al takeaway."""
    cuerpo = " ".join(["idea"] * 14)
    _escribir(
        prototipo,
        f'<html><body><div class="executive-takeaway">💡 Idea Clave: {cuerpo}'
        "</div></body></html>",
    )
    assert all(_ok_o_fallo(check_titulares(tmp_path, [prototipo])))


def test_inventario_cubierto_por_glosario_no_falla(
    tmp_path: Path, prototipo: Path
) -> None:
    """Verifica que 26 términos con entrada en GLOSSARY cuentan como cubiertos."""
    _escribir(
        tmp_path / "front" / "deck_glossary.py",
        "GLOSSARY = {'lyapunov': {'def': 'Caos.', 'analogia': 'Mariposa.'}}\n"
        "def terms():\n    return ['lyapunov']\n",
    )
    cuerpo = " ".join(["lyapunov"] * (LIMITE_SIN_TOOLTIP + 1))
    _escribir(prototipo, f"<html><body><p>{cuerpo}</p></body></html>")
    filas = check_inventario(tmp_path, [prototipo])
    assert all(_ok_o_fallo(filas))
    assert "INFO bruto 26" in filas[0][1]


def test_inventario_no_cubierto_falla_aunque_bruto_sea_bajo(
    tmp_path: Path, prototipo: Path
) -> None:
    """Verifica que 26 términos sin entrada siguen en FAIL."""
    cuerpo = " ".join(["lyapunov"] * (LIMITE_SIN_TOOLTIP + 1))
    _escribir(prototipo, f"<html><body><p>{cuerpo}</p></body></html>")
    assert False in _ok_o_fallo(check_inventario(tmp_path, [prototipo]))


def _iframe(html: str) -> str:
    """Envuelve HTML como iframe data:text/html;base64 del bundle."""
    codificado = base64.b64encode(html.encode("utf-8")).decode("ascii")
    return f'<iframe src="data:text/html;base64,{codificado}"></iframe>'


def test_bundle_falla_si_un_prototipo_no_tiene_gl_term(tmp_path: Path) -> None:
    """Verifica que un iframe sin .gl-term compilado produce FAIL."""
    compilado = '<title>Diapo 1</title><span class="gl-term">lag</span>'
    sin_inyeccion = "<title>Diapo 2</title><p>sin tooltips</p>"
    presentacion = tmp_path / "presentacion.html"
    _escribir(presentacion, _iframe(compilado) + _iframe(sin_inyeccion))
    filas = check_bundle(tmp_path, presentacion)
    assert _ok_o_fallo(filas) == [True, False]
    assert "Diapo 2" in filas[1][1]


def test_bundle_pasa_si_todos_tienen_gl_term(tmp_path: Path) -> None:
    """Verifica que un bundle con .gl-term en todos los iframes pasa."""
    presentacion = tmp_path / "presentacion.html"
    _escribir(
        presentacion,
        _iframe('<span class="gl-term">lag</span>') * 2,
    )
    assert all(_ok_o_fallo(check_bundle(tmp_path, presentacion)))


def test_jerarquia_cuenta_marcas_corta_en_cualquier_elemento(
    tmp_path: Path, prototipo: Path
) -> None:
    """Verifica que data-route=corta cuenta en proc-step, no solo en .stage."""
    pasos = "".join(
        f'<div class="proc-step" data-route="corta">{i}</div>' for i in range(4)
    )
    _escribir(prototipo, f"<html><body>{pasos}</body></html>")
    assert False in _ok_o_fallo(check_jerarquia(tmp_path, [prototipo]))


def test_jerarquia_pasa_con_tres_marcas_corta(tmp_path: Path, prototipo: Path) -> None:
    """Verifica que exactamente tres marcas data-route=corta pasan el límite."""
    pasos = "".join(
        f'<div class="proc-step" data-route="corta">{i}</div>' for i in range(3)
    )
    _escribir(
        prototipo,
        f'<html><body>{pasos}<div class="proc-node" data-route="larga">x</div></body></html>',
    )
    assert all(_ok_o_fallo(check_jerarquia(tmp_path, [prototipo])))


def test_jerarquia_falla_si_proc_node_no_tiene_data_route(
    tmp_path: Path, prototipo: Path
) -> None:
    """Verifica que un prototipo con .proc-node y ninguna marca data-route falla."""
    _escribir(prototipo, '<html><body><div class="proc-node">Paso</div></body></html>')
    assert False in _ok_o_fallo(check_jerarquia(tmp_path, [prototipo]))
