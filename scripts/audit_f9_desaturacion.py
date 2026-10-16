#!/usr/bin/env python3
"""Auditoría automatizada de la Fase 9 (F9):
Valida desaturación textual, eliminación de teleprompter público y limpieza de lienzos
en los 12 prototipos interactivos de las Secciones 1 y 3.
"""
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

PROTOTYPES_S1 = [
    BASE_DIR / "docs/notebooklm/seccion_1/prototipos/5_Anatomia_de_la_senal_temporal_v3.html",
    BASE_DIR / "docs/notebooklm/seccion_1/prototipos/6_Era_1_La_parsimonia_lineal_v3.html",
    BASE_DIR / "docs/notebooklm/seccion_1/prototipos/7_Era_2_El_puente_tabular.html",
    BASE_DIR / "docs/notebooklm/seccion_1/prototipos/8_Era_3_Deep_Learning_y_Parches.html",
    BASE_DIR / "docs/notebooklm/seccion_1/prototipos/9_Era_4_Modelos_Fundacionales_Zero_Shot.html",
    BASE_DIR / "docs/notebooklm/seccion_1/prototipos/10_El_Cono_de_Incertidumbre_y_Prediccion_Conforme.html",
    BASE_DIR / "docs/notebooklm/seccion_1/prototipos/11_Arquitectura_de_Decision_y_Cierre_Ejecutivo.html",
]

PROTOTYPES_S3 = [
    BASE_DIR / "docs/notebooklm/seccion_3/prototipos/19_c_mo_el_agro_invent_el_forecasting.html",
    BASE_DIR / "docs/notebooklm/seccion_3/prototipos/20_del_almanaque_al_sat_lite.html",
    BASE_DIR / "docs/notebooklm/seccion_3/prototipos/21_f_sica_biol_gica_y_el_l_mite_algor_tmico.html",
    BASE_DIR / "docs/notebooklm/seccion_3/prototipos/22_reloj_fenol_gico_del_caf.html",
    BASE_DIR / "docs/notebooklm/seccion_3/prototipos/23_precisi_n_actual_y_las_tres_trampas.html",
]

ALL_PROTOTYPES = PROTOTYPES_S1 + PROTOTYPES_S3


def audit_prototype(path: Path) -> list:
    errors = []
    if not path.exists():
        return [f"Archivo no existe: {path}"]

    content = path.read_text(encoding="utf-8")

    # 1. Prohibido "GUÍA DE EXPOSICIÓN" o "CITA DE CONFERENCIA" en la vista pública
    if "GUÍA DE EXPOSICIÓN" in content or "CITA DE CONFERENCIA" in content:
        errors.append(f"[{path.name}] Contiene teleprompter 'GUÍA DE EXPOSICIÓN' o 'CITA DE CONFERENCIA' visible.")

    # 2. Prohibidos banners redundantes tipo "Arriba: ... / Abajo: ..."
    if "canvas-split-hint" in content or "Arriba: Ventana deslizándose" in content:
        errors.append(f"[{path.name}] Contiene banners redundantes 'canvas-split-hint' o 'Arriba: ...'.")

    # 3. Validar longitud de quote / takeaway (máx 18 palabras)
    # Extraer quotes de STAGES si existen
    quotes = re.findall(r'quote:\s*"([^"]+)"', content)
    for q in quotes:
        wc = len(q.split())
        if wc > 18:
            errors.append(f"[{path.name}] Quote excede 18 palabras ({wc} palabras): '{q[:40]}...'")

    # 4. Validar Diapo 11 si aplica: debe contener .lane-meters
    if "11_Arquitectura_de_Decision" in path.name:
        if "lane-meters" not in content:
            errors.append(f"[{path.name}] Falta bloque visual comparativo 'lane-meters'.")

    # 5. Validar Diapo 20 si aplica: debe contener .step-kpi-strip o .step-kpi-cell
    if "20_del_almanaque" in path.name:
        if "step-kpi" not in content:
            errors.append(f"[{path.name}] Falta grid 'step-kpi-strip' de detalle sin recorte.")

    # 6. Validar Diapo 23 si aplica: fire-test no debe usar position absolute sobre texto
    if "23_precisi_n_actual" in path.name:
        if "grid-template-columns" not in content and "fire-test-btn" in content:
            errors.append(f"[{path.name}] Botón de Prueba de Fuego debe usar grid para no pisar texto.")

    return errors


def main():
    total_errors = []
    print("=== AUDITORÍA FASE 9 (F9): DESATURACIÓN COGNITIVA Y PEDAGOGÍA VISUAL ===")
    for p in ALL_PROTOTYPES:
        errs = audit_prototype(p)
        if errs:
            for e in errs:
                print(f"❌ {e}")
            total_errors.extend(errs)
        else:
            print(f"✅ {p.name}: Conforme")

    print("\n-------------------------------------------------------------")
    if total_errors:
        print(f"FAILED: Se encontraron {len(total_errors)} violaciones.")
        sys.exit(1)
    else:
        print(f"SUCCESS: Los 12 prototipos cumplen con los estándares de la Fase 9.")
        sys.exit(0)


if __name__ == "__main__":
    main()
