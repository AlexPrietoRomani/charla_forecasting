"""
Script orquestador de generación de imágenes, gráficos y figuras de análisis para la página / deck interactivo.
Genera las figuras de alta resolución de Caso 1 y Caso 2 y audita la presencia de assets visuales del front.
Salidas en:
  - docs/images/caso_1/
  - docs/images/caso_2/
  - docs/images/front/
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Añadir scripts a sys.path
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# Importar generadores de imágenes de caso_1 y caso_2
sys.path.insert(0, str(BASE_DIR / "scripts/caso_1"))
sys.path.insert(0, str(BASE_DIR / "scripts/caso_2"))

from visualizar_caso_1 import main as generar_caso_1
from visualizar_caso_2 import main as generar_caso_2

def verificar_assets_front():
    front_dir = BASE_DIR / "docs/images/front"
    print(f"\n=== Auditando assets visuales del Front en {front_dir} ===")
    archivos_esperados = [
        "bg_cover_official.png",
        "bg_content_official.png",
        "bg_closing_official.png",
        "profile_alex.jpg",
        "qr_alex_website.png",
        "logos/official_logos_strip.png",
        "logos/data_wizard_badge.png"
    ]
    faltantes = []
    for f in archivos_esperados:
        p = front_dir / f
        if p.exists():
            size_kb = p.stat().st_size / 1024
            print(f"  [OK] {f} ({size_kb:.1f} KB)")
        else:
            print(f"  [MISSING] {f}")
            faltantes.append(f)
    if not faltantes:
        print("  Todos los assets visuales del Front están presentes y verificados.")
    else:
        print(f"  ALERTA: Faltan {len(faltantes)} assets del front.")

def main():
    print("=================================================================")
    print(" INICIANDO PIPELINE DE GENERACIÓN VISUAL PARA LA PÁGINA / DECK   ")
    print("=================================================================")
    
    # 1. Caso 1 (Punchana Clima)
    print("\n--- [1/3] Generando gráficos de análisis: Caso 1 (Clima SENAMHI) ---")
    generar_caso_1()
    
    # 2. Caso 2 (Café Jaén MIDAGRI)
    print("\n--- [2/3] Generando gráficos de análisis: Caso 2 (Café Jaén / MODIS) ---")
    generar_caso_2()
    
    # 3. Auditoría de Front
    print("\n--- [3/3] Verificando assets del Front (Diapositivas) ---")
    verificar_assets_front()
    
    print("\n=================================================================")
    print(" PIPELINE VISUAL COMPLETADO CON ÉXITO                            ")
    print("=================================================================")

if __name__ == "__main__":
    main()
