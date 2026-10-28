"""
Assets y snippets de branding oficial para Iquitos Data Fest 2026.
Contiene logos institucionales embebidos en Base64, backgrounds oficiales por acto,
la agenda del deck y código QR vectorial oficial.
"""
import base64
from pathlib import Path

# Rutas de los fondos por acto, relativas a la raíz del repositorio
ACT_BG_PATHS = {
    1: "docs/images/front/bg_acto_1.jpg",
    2: "docs/images/front/bg_acto_2.jpg",
    3: "docs/images/front/bg_acto_3.jpg",
    4: "docs/images/front/bg_acto_4.jpg",
    5: "docs/images/front/bg_acto_5.jpg",
}

# Agenda de la charla: una pregunta en lenguaje llano por acto y sus minutos
AGENDA = [
    {"number": "01", "icon": "📈", "question": "¿Qué hay dentro de una serie de tiempo y qué modelos existen?", "takeaway": "Tendencia, estacionalidad, ruido y los modelos de cada época.", "minutes": 12},
    {"number": "02", "icon": "🌡️", "question": "Caso 1 · ¿Puede un modelo barato ganarle a Google prediciendo el clima de Iquitos?", "takeaway": "Modelo sencillo frente al de Google, con datos de Iquitos.", "minutes": 8},
    {"number": "03", "icon": "🌱", "question": "¿Cómo pronosticaba el campo antes de la inteligencia artificial?", "takeaway": "Calendario, lluvias y ritmo de la planta, sin inteligencia artificial.", "minutes": 6},
    {"number": "04", "icon": "☕", "question": "Caso 2 · ¿Ve el satélite la cosecha de café?", "takeaway": "Por qué el satélite no vio la roya del café.", "minutes": 6},
    {"number": "05", "icon": "🧭", "question": "¿Qué me llevo a casa?", "takeaway": "Principios prácticos para no creerte un pronóstico a ciegas.", "minutes": 3},
]
AGENDA_TOTAL_MINUTES = 35

# Subtítulos de los separadores de acto (solo actos con separador en el deck)
SEPARATOR_SUBTITLES = {
    1: "Repasamos cómo se pasó de fórmulas simples a modelos que aprenden solos, y qué límites no cambian.",
    3: "Desde el almanaque de los agricultores hasta los satélites que miden el cultivo cada pocos días.",
    4: "Revisamos 24 campañas de café en Jaén y por qué el satélite no vio la epidemia de roya.",
    5: "Las reglas prácticas para no engañarte con un pronóstico: método, física del problema y prudencia.",
}

assert sum(item["minutes"] for item in AGENDA) == AGENDA_TOTAL_MINUTES, (
    "La suma de minutos de AGENDA debe coincidir con AGENDA_TOTAL_MINUTES"
)


def get_base64_img(rel_path):
    """Devuelve el contenido de una imagen en Base64 o cadena vacía si no existe."""
    p = Path(rel_path)
    if not p.is_absolute():
        p = Path(__file__).resolve().parent.parent / rel_path
    if p.exists():
        with open(p, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    return ""

def get_svg_text(rel_path):
    """Devuelve el texto de un SVG o cadena vacía si no existe."""
    p = Path(rel_path)
    if not p.is_absolute():
        p = Path(__file__).resolve().parent.parent / rel_path
    if p.exists():
        return p.read_text(encoding="utf-8")
    return ""

def get_separator_copy(act):
    """Devuelve la pregunta de la agenda y el subtítulo para el separador de un acto."""
    return AGENDA[act - 1]["question"], SEPARATOR_SUBTITLES[act]

def get_branding():
    """Reúne logos, fondos por acto, perfil y QR en un diccionario listo para el deck."""
    b64_header = get_base64_img("docs/images/front/logos/official_logos_strip.png")
    b64_dw = get_base64_img("docs/images/front/logos/data_wizard_badge.png")
    b64_bg_portada = get_base64_img("docs/images/front/bg_cover_official.png")
    b64_bg_slide = get_base64_img("docs/images/front/bg_content_official.png")
    b64_bg_closing = get_base64_img("docs/images/front/bg_closing_official.png")
    b64_act_bg = {act: get_base64_img(rel_path) for act, rel_path in ACT_BG_PATHS.items()}
    b64_profile = get_base64_img("docs/images/front/profile_alex.jpg")
    b64_qr = get_base64_img("docs/images/front/qr_alex_website.png")
    qr_svg = get_svg_text("docs/images/front/qr_alex_website.svg")

    return {
        "b64_header": b64_header,
        "b64_dw": b64_dw,
        "b64_bg_portada": b64_bg_portada,
        "b64_bg_slide": b64_bg_slide,
        "b64_bg_closing": b64_bg_closing,
        "b64_act_bg": b64_act_bg,
        "b64_profile": b64_profile,
        "b64_qr": b64_qr,
        "qr_svg": qr_svg
    }
