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
    b64_header = get_base64_img("images/logos/official_logos_strip.png")
    b64_dw = get_base64_img("images/logos/data_wizard_badge.png")
    b64_bg_portada = get_base64_img("images/bg_cover_official.png")
    b64_bg_slide = get_base64_img("images/bg_content_official.png")
    b64_bg_closing = get_base64_img("images/bg_closing_official.png")
    b64_profile = get_base64_img("images/profile_alex.jpg")
    b64_qr = get_base64_img("images/qr_alex_website.png")

    return {
        "b64_header": b64_header,
        "b64_dw": b64_dw,
        "b64_bg_portada": b64_bg_portada,
        "b64_bg_slide": b64_bg_slide,
        "b64_bg_closing": b64_bg_closing,
        "b64_profile": b64_profile,
        "b64_qr": b64_qr,
        "qr_svg": ""
    }
