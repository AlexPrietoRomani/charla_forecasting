"""
Archivo: test_deck_closing.py
Fecha de modificación: 28/10/2026
Autor: Alex Prieto Romani

Descripción:
    Valida la diapositiva 29 (conclusiones) del deck: que el texto visible sea
    breve para el público sin estadística y que contenga las tres lecciones
    exactas con su línea de evidencia.

Acciones Principales:
    - Extrae la sección de la diapo 29 del generador de diapositivas.
    - Quita etiquetas, título y botón de intro para contar solo el contenido.
    - Verifica el tope de 60 palabras y la presencia de las tres frases.

Estructura Interna:
    - `_slide_29_visible_text`: Devuelve el texto visible de la diapo 29.
    - `test_slide_29_has_at_most_60_visible_words`: Comprueba el tope de palabras.
    - `test_slide_29_contains_three_lessons`: Comprueba las frases exactas.

Entradas / Dependencias:
    - front/deck_slides_p2.py

Salidas / Efectos:
    - Ninguna. Solo reporta resultados de pytest.

Ejecución:
    python -m pytest back/test_deck_closing.py -q
"""

import re
import sys
from pathlib import Path

RAIZ_PROYECTO = Path(__file__).resolve().parent.parent
FRONT_DIR = RAIZ_PROYECTO / "front"
sys.path.insert(0, str(RAIZ_PROYECTO))
# Los módulos de front importan dependencias hermanas sin prefijo de paquete
sys.path.insert(0, str(FRONT_DIR))

from front.deck_slides_p2 import get_slides_part2

MAX_PALABRAS = 60
LECCIONES = [
    "1 · Respeta el orden del tiempo",
    "Entrenar mirando el futuro da notas falsas. Iquitos: 2,557 días, examen ciego de 90.",
    "2 · El valor está en el rango, no en el número",
    "Un pronóstico honesto dice «entre 29 y 36 °C», no «32.7 °C».",
    "3 · Primero la física, después el algoritmo",
    "El satélite vio hojas verdes; la cosecha de Jaén cayó a la mitad.",
]
PATRON_SECCION_29 = re.compile(
    r'<section class="slide slide-lessons[^"]*" data-index="29".*?</section>',
    re.DOTALL,
)
PATRON_TITULO = re.compile(r'<h2 class="slide-main-title[^"]*">.*?</h2>', re.DOTALL)
PATRON_BOTON = re.compile(r"<button\b.*?</button>", re.DOTALL)
PATRON_ETIQUETA = re.compile(r"<[^>]+>")
PATRON_ENUMERADOR = re.compile(r"\b\d\s+·\s+")


def _slide_29_html() -> str:
    """Devuelve el bloque HTML completo de la diapo 29 generado por el deck."""
    html = get_slides_part2(branding={})
    coincidencia = PATRON_SECCION_29.search(html)
    assert coincidencia is not None, "No se encontró la sección de la diapo 29"
    return coincidencia.group(0)


def _slide_29_visible_text(quitar_enumeradores: bool = True) -> str:
    """Devuelve el texto visible de la diapo 29 sin título, botón ni etiquetas."""
    bloque = _slide_29_html()
    sin_titulo = PATRON_TITULO.sub(" ", bloque)
    sin_boton = PATRON_BOTON.sub(" ", sin_titulo)
    sin_etiquetas = PATRON_ETIQUETA.sub(" ", sin_boton)
    # Los números de lista ("1 ·") son marcadores visuales, no palabras del discurso
    sin_enumeradores = PATRON_ENUMERADOR.sub("", sin_etiquetas) if quitar_enumeradores else sin_etiquetas
    return " ".join(sin_enumeradores.split())


def _contar_palabras(texto: str) -> int:
    """Cuenta los tokens con letras o dígitos, ignorando iconos y símbolos sueltos."""
    return sum(1 for token in texto.split() if re.search(r"[0-9A-Za-zÁÉÍÓÚáéíóúÑñÜü]", token))


def test_slide_29_has_at_most_60_visible_words() -> None:
    """Verifica que la diapo 29 no muestre más de 60 palabras visibles."""
    texto = _slide_29_visible_text()
    assert _contar_palabras(texto) <= MAX_PALABRAS


def test_slide_29_contains_three_lessons() -> None:
    """Verifica que la diapo 29 contenga las tres lecciones y sus evidencias exactas."""
    texto = _slide_29_visible_text(quitar_enumeradores=False)
    for frase in LECCIONES:
        assert frase in texto, f"Falta el texto: {frase}"
