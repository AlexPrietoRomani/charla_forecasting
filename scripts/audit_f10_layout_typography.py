#!/usr/bin/env python3
"""Auditoría automatizada de la Fase 10 (F10):
Certifica layout al 100% de altura, tipografía homologada (sin texto enano), eliminación
del teleprompter `.speaker-box` y la inyección del motor `front/prototype_engine.py`
en los 18 prototipos de las Secciones 1, 2 y 3, el bundle `presentacion.html` y las
36 capturas multi-resolución.
"""
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from front.prototype_engine import discover_slide_video, normalize_prototype_html  # noqa: E402

PROTOTIPOS = [
    (5, "docs/notebooklm/seccion_1/prototipos/5_Anatomia_de_la_senal_temporal_v3.html",
     ["drawLayerLabels", "minGapY", "Idea Clave"]),
    (6, "docs/notebooklm/seccion_1/prototipos/6_Era_1_La_parsimonia_lineal_v3.html",
     ["narr-blocks", "space-evenly", "executive-takeaway", "Idea Clave"]),
    (7, "docs/notebooklm/seccion_1/prototipos/7_Era_2_El_puente_tabular.html",
     ["narr-blocks", "space-evenly", "executive-takeaway", "Idea Clave"]),
    (8, "docs/notebooklm/seccion_1/prototipos/8_Era_3_Deep_Learning_y_Parches.html",
     ["narr-blocks", "space-evenly", "executive-takeaway", "Idea Clave"]),
    (9, "docs/notebooklm/seccion_1/prototipos/9_Era_4_Modelos_Fundacionales_Zero_Shot.html",
     ["narr-blocks", "space-evenly", "executive-takeaway", "Idea Clave"]),
    (10, "docs/notebooklm/seccion_1/prototipos/10_El_Cono_de_Incertidumbre_y_Prediccion_Conforme.html",
     ["narr-blocks", "space-evenly", "executive-takeaway", "Idea Clave"]),
    (11, "docs/notebooklm/seccion_1/prototipos/11_Arquitectura_de_Decision_y_Cierre_Ejecutivo.html",
     ["via-card", "via-items", "space-evenly", "Regla de Oro"]),
    (12, "docs/notebooklm/seccion_2/prototipos/12_Caso_1_Auditoria_Iquitos.html",
     ["narr-blocks", "space-evenly", "executive-takeaway", "Idea Clave"]),
    (13, "docs/notebooklm/seccion_2/prototipos/13_Datos_SENAMHI_Punchana.html",
     ["narr-blocks", "space-evenly", "executive-takeaway", "Idea Clave"]),
    (14, "docs/notebooklm/seccion_2/prototipos/14_Trampa_Arboles_Meseta_vs_Diferencias.html",
     ["narr-blocks", "space-evenly", "executive-takeaway", "Idea Clave"]),
    (15, "docs/notebooklm/seccion_2/prototipos/15_Benchmark_14_Modelos_Tierra_vs_Supercomputo.html",
     ["narr-blocks", "space-evenly", "executive-takeaway", "Idea Clave"]),
    (16, "docs/notebooklm/seccion_2/prototipos/16_Pronostico_7_Dias_Cono_P10_P90.html",
     ["audit-panel", "kpi-grid", "takeaway-card", "Idea Clave"]),
    (17, "docs/notebooklm/seccion_2/prototipos/17_Pipeline_Codigo_Diferencias_ExtraTrees.html",
     ["right-panel", "axioms-card", "bridge-card"]),
    (19, "docs/notebooklm/seccion_3/prototipos/19_c_mo_el_agro_invent_el_forecasting.html",
     ["narr-blocks", "space-evenly", "executive-takeaway", "Idea Clave"]),
    (20, "docs/notebooklm/seccion_3/prototipos/20_del_almanaque_al_sat_lite.html",
     ["narr-blocks", "space-evenly", "takeaway-badge", "takeaway-text", "Idea Clave"]),
    (21, "docs/notebooklm/seccion_3/prototipos/21_f_sica_biol_gica_y_el_l_mite_algor_tmico.html",
     ["narr-blocks", "space-evenly", "takeaway-badge", "takeaway-text", "Idea Clave"]),
    (22, "docs/notebooklm/seccion_3/prototipos/22_reloj_fenol_gico_del_caf.html",
     ["narr-blocks", "space-evenly", "takeaway-badge", "takeaway-text", "Idea Clave"]),
    (23, "docs/notebooklm/seccion_3/prototipos/23_precisi_n_actual_y_las_tres_trampas.html",
     ["narr-blocks", "space-evenly", "takeaway-badge", "takeaway-text", "Idea Clave"]),
]

FORBIDDEN_SNIPPETS = [
    "GUÍA DE EXPOSICIÓN",
    "GUIA DE EXPOSICION",
    'class="speaker-box"',
    'class="speaker-head"',
    'class="speaker-quote"',
    "Axioma Gerencial",
]

FONT_MINIMUMS = {
    "narr-title": 18.0,
    "narr-lead": 13.5,
    "info-block-label": 11.5,
    "info-block-text": 13.0,
    "via-title": 11.5,
    "q-text": 13.5,
    "takeaway-text": 12.5,
}

FONT_MINIMUMS_PER_SLIDE = {
    11: {"via-title": 18.0},
}

VIDEO_SLIDE_CANDIDATES = [(1, 5), (1, 7), (1, 9), (1, 10), (3, 19), (3, 21)]

SCREENSHOTS = [
    BASE_DIR / f"screenshots/f10_s{slide}_{width}.png"
    for slide in [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23]
    for width in [1366, 1920]
]

MAX_QUOTE_WORDS = 15


def font_px_values(block: str) -> list:
    values = []
    for decl in re.findall(r"(?:font|font-size)\s*:\s*([^;}]+)", block):
        values.extend(float(v) for v in re.findall(r"([\d.]+)px", decl))
    return values


def max_font_px(content: str, class_name: str):
    values = []
    pattern = re.compile(re.escape("." + class_name) + r"\b[^{}]*\{([^}]*)\}")
    for block in pattern.findall(content):
        values.extend(font_px_values(block))
    return max(values) if values else None


def quote_words(content: str):
    match = re.search(r'<span id="speakerQuote">(.*?)</span>', content, re.DOTALL)
    if not match:
        return None
    text = re.sub(r"<[^>]+>", " ", match.group(1))
    tokens = [t for t in re.split(r"\s+", text.strip()) if re.search(r"\w", t)]
    return len(tokens)


def audit_prototype(slide: int, rel_path: str, required: list) -> list:
    errors = []
    path = BASE_DIR / rel_path
    if not path.exists():
        return [f"[Diapo {slide}] Archivo no existe: {rel_path}"]

    content = path.read_text(encoding="utf-8")

    if "height: 100%" not in content:
        errors.append(f"[Diapo {slide}] Falta 'height: 100%' (llenado vertical).")

    for snippet in required:
        if snippet not in content:
            errors.append(f"[Diapo {slide}] Falta marcador requerido: '{snippet}'.")

    for snippet in FORBIDDEN_SNIPPETS:
        if snippet in content:
            errors.append(f"[Diapo {slide}] Contiene snippet prohibido: '{snippet}'.")

    words = quote_words(content)
    if words is not None and words > MAX_QUOTE_WORDS:
        errors.append(f"[Diapo {slide}] Quote '#speakerQuote' excede {MAX_QUOTE_WORDS} palabras ({words}).")

    minimums = dict(FONT_MINIMUMS)
    minimums.update(FONT_MINIMUMS_PER_SLIDE.get(slide, {}))
    for class_name, minimum in minimums.items():
        maximum = max_font_px(content, class_name)
        if maximum is not None and maximum < minimum:
            errors.append(
                f"[Diapo {slide}] Tipografía encogida en '.{class_name}': máx {maximum}px < {minimum}px."
            )

    normalized = normalize_prototype_html(content, slide, 1 if slide <= 17 else 3)
    for marker in ["deck-engine-override-css", "deck-engine-runtime-js"]:
        if marker not in normalized:
            errors.append(f"[Diapo {slide}] El motor no inyectó '{marker}' en el HTML procesado.")

    return errors


def audit_engine() -> list:
    errors = []
    path = BASE_DIR / "front/prototype_engine.py"
    if not path.exists():
        return ["[Motor] No existe front/prototype_engine.py."]
    content = path.read_text(encoding="utf-8")
    for snippet in ["ENGINE_OVERRIDE_CSS", "ENGINE_RUNTIME_JS", "def load_prototype_b64",
                    "space-evenly", "cinematicVideoGate"]:
        if snippet not in content:
            errors.append(f"[Motor] prototype_engine.py no contiene: '{snippet}'.")
    return errors


def audit_build() -> list:
    errors = []
    path = BASE_DIR / "back/build_deck.py"
    if not path.exists():
        return ["[Build] No existe back/build_deck.py."]
    content = path.read_text(encoding="utf-8")

    calls = len(re.findall(r"load_prototype_b64\(", content))
    if calls < 18:
        errors.append(f"[Build] load_prototype_b64 llamado {calls} veces (<18).")
    if "render_slide_video_gate" not in content:
        errors.append("[Build] Falta render_slide_video_gate (gates de video).")

    for _, rel_path, _ in PROTOTIPOS:
        if rel_path not in content:
            errors.append(f"[Build] El prototipo '{rel_path}' no está embebido en build_deck.py.")
    return errors


def audit_bundle() -> list:
    errors = []
    path = BASE_DIR / "presentacion.html"
    if not path.exists():
        return ["[Bundle] No existe presentacion.html (ejecutar back/build_deck.py)."]
    content = path.read_text(encoding="utf-8")

    if len(content) < 5_000_000:
        errors.append(f"[Bundle] presentacion.html sospechosamente pequeño: {len(content)} bytes.")

    leftover = len(re.findall(r"__[A-Z0-9_]+__", content))
    if leftover:
        errors.append(f"[Bundle] Quedan {leftover} placeholders sin reemplazar.")

    videos = [
        (sec, slide)
        for sec, slide in VIDEO_SLIDE_CANDIDATES
        if discover_slide_video(BASE_DIR, sec, slide) is not None
    ]
    gates = content.count("cinematicVideoGate")
    if videos and gates < len(videos):
        errors.append(
            f"[Bundle] Gates de video insuficientes: {gates} (<{len(videos)} videos presentes)."
        )

    for snippet in ["GUÍA DE EXPOSICIÓN", "class=\"speaker-box\""]:
        if snippet in content:
            errors.append(f"[Bundle] Contiene snippet prohibido: '{snippet}'.")

    return errors


def audit_screenshots() -> list:
    errors = []
    missing = [p for p in SCREENSHOTS if not p.exists()]
    tiny = [p for p in SCREENSHOTS if p.exists() and p.stat().st_size < 40_000]
    if missing:
        errors.append(f"[Capturas] Faltan {len(missing)} capturas: " +
                      ", ".join(p.name for p in missing[:6]) + ("..." if len(missing) > 6 else ""))
    if tiny:
        errors.append(f"[Capturas] {len(tiny)} capturas sospechosamente pequeñas: " +
                      ", ".join(p.name for p in tiny[:6]) + ("..." if len(tiny) > 6 else ""))
    return errors


def main():
    total_errors = []
    print("=== AUDITORÍA FASE 10 (F10): MOTOR DE ESTILOS Y HOMOLOGACIÓN VISUAL S1-S2-S3 ===")

    for slide, rel_path, required in PROTOTIPOS:
        errors = audit_prototype(slide, rel_path, required)
        if errors:
            for e in errors:
                print(f"❌ {e}")
            total_errors.extend(errors)
        else:
            print(f"✅ Diapo {slide}: Conforme ({Path(rel_path).name})")

    for label, errors in [
        ("Motor prototype_engine.py", audit_engine()),
        ("Build build_deck.py", audit_build()),
        ("Bundle presentacion.html", audit_bundle()),
        ("Capturas 36 PNG", audit_screenshots()),
    ]:
        if errors:
            for e in errors:
                print(f"❌ {e}")
            total_errors.extend(errors)
        else:
            print(f"✅ {label}: Conforme")

    print("\n-------------------------------------------------------------")
    if total_errors:
        print(f"FAILED: Se encontraron {len(total_errors)} violaciones.")
        sys.exit(1)
    else:
        print("SUCCESS: Los 18 prototipos, el motor, el bundle y las 36 capturas cumplen la Fase 10.")
        sys.exit(0)


if __name__ == "__main__":
    main()
