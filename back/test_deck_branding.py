"""
Archivo: test_deck_branding.py
Fecha de modificación: 28/10/2026
Autor: Alex Prieto Romani

Descripción:
    Valida los fondos por acto, la agenda y los subtítulos de los separadores del deck
    definidos en front/deck_branding.py.

Acciones Principales:
    - Verifica que los cinco fondos de acto existan y pesen 300 KB o menos.
    - Verifica que los minutos de AGENDA sumen AGENDA_TOTAL_MINUTES (35).
    - Verifica que cada pregunta de la agenda tenga 16 palabras o menos.
    - Verifica que cada subtítulo de separador tenga 20 palabras o menos.

Estructura Interna:
    - `test_act_backgrounds_exist_and_weigh_under_limit`: Comprueba existencia y peso de los fondos.
    - `test_agenda_minutes_sum_to_total`: Comprueba la suma de minutos.
    - `test_agenda_questions_within_word_limit`: Comprueba el largo de las preguntas.
    - `test_separator_subtitles_within_word_limit`: Comprueba el largo de los subtítulos.
"""

import sys
from pathlib import Path

RAIZ_PROYECTO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ_PROYECTO))

from front.deck_branding import (
    ACT_BG_PATHS,
    AGENDA,
    AGENDA_TOTAL_MINUTES,
    SEPARATOR_SUBTITLES,
)

MAX_BG_BYTES = 300 * 1024
MAX_QUESTION_WORDS = 16
MAX_SUBTITLE_WORDS = 20


def test_act_backgrounds_exist_and_weigh_under_limit():
    """Comprueba que los cinco fondos por acto existan y no superen 300 KB."""
    assert len(ACT_BG_PATHS) == 5
    for act, rel_path in ACT_BG_PATHS.items():
        bg_path = RAIZ_PROYECTO / rel_path
        assert bg_path.exists(), f"Falta el fondo del acto {act}: {rel_path}"
        assert bg_path.stat().st_size <= MAX_BG_BYTES, f"Fondo del acto {act} supera 300 KB"


def test_agenda_minutes_sum_to_total():
    """Comprueba que la suma de minutos de la agenda coincida con el total de la charla."""
    assert len(AGENDA) == 5
    assert sum(item["minutes"] for item in AGENDA) == AGENDA_TOTAL_MINUTES == 35


def test_agenda_questions_within_word_limit():
    """Comprueba que cada pregunta de la agenda tenga 16 palabras o menos."""
    for item in AGENDA:
        word_count = len(item["question"].split())
        assert word_count <= MAX_QUESTION_WORDS, f"Pregunta {item['number']} tiene {word_count} palabras"


def test_separator_subtitles_within_word_limit():
    """Comprueba que cada subtítulo de separador tenga 20 palabras o menos."""
    for act, subtitle in SEPARATOR_SUBTITLES.items():
        word_count = len(subtitle.split())
        assert word_count <= MAX_SUBTITLE_WORDS, f"Subtítulo del acto {act} tiene {word_count} palabras"


def test_agenda_takeaways_within_word_limit():
    """Comprueba que cada línea de apoyo de la agenda tenga 10 palabras o menos."""
    for item in AGENDA:
        word_count = len(item["takeaway"].split())
        assert word_count <= 10, f"Línea de apoyo {item['number']} tiene {word_count} palabras"
