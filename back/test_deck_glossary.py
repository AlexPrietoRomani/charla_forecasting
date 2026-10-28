"""
Archivo: test_deck_glossary.py
Fecha de modificación: 28/10/2026
Autor: Alex Prieto Romani

Descripción:
    Valida la estructura del glosario del deck: tamaño, longitud de definiciones y
    analogías, convención de claves y ausencia de duplicados en terms().

Acciones Principales:
    - Verifica que GLOSSARY tenga como máximo 40 entradas.
    - Verifica límites de palabras de "def" y "analogia" y que las claves estén en minúscula.
    - Verifica que terms() no repita términos ni alias.

Estructura Interna:
    - `test_glossary_size_within_limit`: Comprueba el tope de 40 entradas.
    - `test_definitions_and_analogies_respect_word_limits`: Comprueba definiciones y analogías.
    - `test_keys_are_lowercase`: Comprueba la convención de claves.
    - `test_terms_have_no_duplicates`: Comprueba que terms() no repite entradas.

Entradas / Dependencias:
    - front/deck_glossary.py

Salidas / Efectos:
    - Ninguna. Solo reporta resultados de pytest.

Ejecución:
    python -m pytest back/test_deck_glossary.py -q
"""

import sys
from pathlib import Path

RAIZ_PROYECTO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ_PROYECTO))

from front.deck_glossary import GLOSSARY, terms

MAX_ENTRADAS = 40
MAX_PALABRAS = 15


def test_glossary_size_within_limit() -> None:
    """Verifica que el glosario no supere el tope de 40 entradas."""
    assert 0 < len(GLOSSARY) <= MAX_ENTRADAS


def test_definitions_and_analogies_respect_word_limits() -> None:
    """Verifica que cada definición y analogía tenga entre 1 y 15 palabras."""
    for clave, entrada in GLOSSARY.items():
        definicion = str(entrada["def"])
        analogia = str(entrada["analogia"])
        assert 0 < len(definicion.split()) <= MAX_PALABRAS, clave
        assert 0 < len(analogia.split()) <= MAX_PALABRAS, clave


def test_keys_are_lowercase() -> None:
    """Verifica que todas las claves del glosario estén en minúscula."""
    for clave in GLOSSARY:
        assert clave == clave.lower(), clave


def test_terms_have_no_duplicates() -> None:
    """Verifica que terms() devuelva términos y alias sin repeticiones."""
    lista = terms()
    normalizados = [termino.casefold() for termino in lista]
    assert len(normalizados) == len(set(normalizados))
    for clave in GLOSSARY:
        assert clave in lista
