"""
Assets y snippets de branding oficial para Iquitos Data Fest 2026.
Contiene logos institucionales embebidos en Base64, backgrounds oficiales y código QR vectorial oficial.
"""
import base64
from pathlib import Path

def get_base64_img(rel_path):
    p = Path(rel_path)
    if p.exists():
        with open(p, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    return ""

def get_branding():
    b64_header = get_base64_img("images/logos/header_logos.png")
    b64_dw = get_base64_img("images/logos/banner_dw.png")
    b64_bg_portada = get_base64_img("images/bg_portada_iquitos.jpg")
    b64_bg_slide = get_base64_img("images/bg_slide_iquitos.jpg")
    
    qr_svg_path = Path("images/qr_charla_forecasting.svg")
    qr_svg = ""
    if qr_svg_path.exists():
        with open(qr_svg_path, "r", encoding="utf-8") as f:
            qr_svg = f.read()
            qr_svg = qr_svg.replace('width="41mm" height="41mm"', 'viewBox="0 0 41 41" style="width:100%; height:100%; display:block;"')

    return {
        "b64_header": b64_header,
        "b64_dw": b64_dw,
        "b64_bg_portada": b64_bg_portada,
        "b64_bg_slide": b64_bg_slide,
        "qr_svg": qr_svg
    }
