"""
Archivo: test_deck_plain_numbers.py
Fecha de modificación: 28/10/2026
Autor: Alex Prieto Romani

Descripción:
    Valida la tabla de cifras llanas del deck: cantidad mínima de entradas, longitud de las
    frases, consistencia del redondeo contra data/ y conservación de las cifras canónicas
    (el valor exacto debe seguir presente en los prototipos).

Acciones Principales:
    - Verifica al menos 20 entradas y frases de máximo 10 palabras.
    - Verifica que check_all() no reporte errores y que las claves obligatorias existan.
    - Verifica que cada cifra canónica presente en HEAD siga presente en el prototipo.

Estructura Interna:
    - `test_minimum_entries`: Comprueba el tamaño de PLAIN.
    - `test_plain_phrases_within_word_limit`: Comprueba la longitud de las frases.
    - `test_check_all_has_no_errors`: Comprueba el redondeo contra las fuentes.
    - `test_required_keys_present`: Comprueba las claves obligatorias.
    - `test_canonical_figures_preserved`: Comprueba que no desaparecen cifras exactas.

Entradas / Dependencias:
    - front/deck_plain_numbers.py, data/ y los prototipos HTML (git para comparar con HEAD).

Salidas / Efectos:
    - Ninguna. Solo reporta resultados de pytest.

Ejecución:
    python -m pytest back/test_deck_plain_numbers.py -q
"""

import subprocess
import sys
from pathlib import Path

import pytest

RAIZ_PROYECTO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ_PROYECTO))

from front.deck_plain_numbers import (
    MAX_PLAIN_WORDS,
    PLAIN,
    check_all,
    resolve,
)

MIN_ENTRIES = 20
REQUIRED_KEYS = (
    "rmse_extratrees",
    "dm_p_timesfm",
    "roya_caida",
    "r_ndvi",
    "r_lluvia_floracion",
    "mae_tendencia",
    "mae_ndvi",
    "mae_fusion",
    "cobertura_cono",
    "cpu_extratrees",
)
CANONICAL_FIGURES = (
    "1.880", "1.883", "0.027", "0.1536", "0.751", "0.7483", "3.723", "5.448", "35.38",
    "18.46", "0.25", "0.71", "71.4", "2.458", "2.583", "0.600", "0.7564", "10.0", "22.7", "56",
)  # fmt: skip
PROTOTYPES = (
    "docs/notebooklm/seccion_1/prototipos/6_Era_1_La_parsimonia_lineal_v3.html",
    "docs/notebooklm/seccion_1/prototipos/10_El_Cono_de_Incertidumbre_y_Prediccion_Conforme.html",
    "docs/notebooklm/seccion_2/prototipos/12_Caso_1_Auditoria_Iquitos.html",
    "docs/notebooklm/seccion_2/prototipos/15_Benchmark_14_Modelos_Tierra_vs_Supercomputo.html",
    "docs/notebooklm/seccion_2/prototipos/17_Pipeline_Codigo_Diferencias_ExtraTrees.html",
    "docs/notebooklm/seccion_3/prototipos/22_reloj_fenol_gico_del_caf.html",
    "docs/notebooklm/seccion_3/prototipos/23_precisi_n_actual_y_las_tres_trampas.html",
    "docs/notebooklm/seccion_4/prototipos/25_Datos_24_Campanias_Jaen.html",
    "docs/notebooklm/seccion_4/prototipos/26_Trampa_Satelite_NDVI_vs_Clima.html",
    "docs/notebooklm/seccion_4/prototipos/27_Validacion_WalkForward_Benchmark_Jaen.html",
)


def _head_text(relative_path: str) -> str | None:
    """Devuelve el contenido del archivo en HEAD, o None si git no lo entrega."""
    result = subprocess.run(
        ["git", "show", f"HEAD:{relative_path}"],
        cwd=RAIZ_PROYECTO,
        capture_output=True,
        check=False,
    )
    return result.stdout.decode("utf-8") if result.returncode == 0 else None


def test_minimum_entries() -> None:
    """Verifica que PLAIN tenga al menos 20 entradas completas."""
    assert len(PLAIN) >= MIN_ENTRIES
    assert all({"src", "show", "plain"} <= set(entry) for entry in PLAIN.values())


def test_plain_phrases_within_word_limit() -> None:
    """Verifica que cada frase llana tenga como máximo 10 palabras."""
    too_long = [
        k for k, v in PLAIN.items() if len(v["plain"].split()) > MAX_PLAIN_WORDS
    ]
    assert not too_long


def test_check_all_has_no_errors() -> None:
    """Verifica que cada cifra visible sea el redondeo de su fuente."""
    assert check_all() == []


def test_required_keys_present() -> None:
    """Verifica las claves obligatorias y el valor exacto de algunas fuentes."""
    assert set(REQUIRED_KEYS) <= set(PLAIN)
    assert resolve(PLAIN["rmse_extratrees"]["src"]) == pytest.approx(1.88)
    assert resolve(PLAIN["cobertura_cono"]["src"]) == pytest.approx(71.4, abs=0.05)


@pytest.mark.parametrize("relative_path", PROTOTYPES)
def test_canonical_figures_preserved(relative_path: str) -> None:
    """Verifica que cada cifra canónica presente en HEAD siga presente en el prototipo."""
    before = _head_text(relative_path)
    if before is None:
        pytest.skip("HEAD no disponible")
    after = (RAIZ_PROYECTO / relative_path).read_text(encoding="utf-8")
    lost = [fig for fig in CANONICAL_FIGURES if fig in before and fig not in after]
    assert not lost, f"cifras exactas perdidas: {lost}"
