#!/usr/bin/env python3
"""Genera scene.html: entrada de 30 s para la Diapo 21 (Sección 3), 'Física biológica · El límite algorítmico'. Datos reales de Jaén (24 campañas) + hipótesis confirmadas."""

import base64
import json
import pathlib

import pandas as pd

SRC = pathlib.Path(__file__).resolve().parent
ROOT = SRC.parents[3]

FPS = 30
DURATION_MS = 30000

df = pd.read_csv(ROOT / "data/caso_2/cafe_jaen_campanias.csv")
hip = json.loads((ROOT / "data/caso_2/cafe_jaen_hipotesis.json").read_text(encoding="utf-8"))

years = [int(v) for v in df["campania"]]
ndvi = [None if pd.isna(v) else round(float(v), 4) for v in df["ndvi_anual"]]
rend = [None if pd.isna(v) else round(float(v), 2) for v in df["rendimiento_qq_ha"]]
i2014 = years.index(2014)
r2014 = float(df.loc[df["campania"] == 2014, "rendimiento_qq_ha"].iloc[0])

data = {
    "years": years,
    "ndvi": ndvi,
    "rend": rend,
    "i2014": i2014,
    "ndvi2014": ndvi[i2014],
    "rend2014": round(r2014, 1),
    "n": len(years),
    "hip": {
        "rNdvi": hip["H1_saturacion"]["pearson_r"],
        "pNdvi": hip["H1_saturacion"]["p_valor"],
        "cvNdvi": hip["H1_saturacion"]["cv_ndvi_pct"],
        "rLluvia": hip["H2_fenologia"]["r_lluvia_flor"],
        "rDeficit": hip["H2_fenologia"]["r_deficit_hidrico"],
        "rTmax": hip["H2_fenologia"]["r_tmax_flor"],
        "caidaPct": hip["H4_roya_invisibilidad"]["caida_rendimiento_pct"],
        "varNdviPct": hip["H4_roya_invisibilidad"]["variacion_ndvi_pct"],
    },
}

fonts_css = ""
font_files = [
    ("Space Grotesk", "SpaceGrotesk-500.woff2", "300 800"),
    ("IBM Plex Sans", "IBMPlexSans-400.woff2", "100 700"),
    ("IBM Plex Mono", "IBMPlexMono-400.woff2", "400"),
    ("IBM Plex Mono", "IBMPlexMono-600.woff2", "600"),
]
for family, fname, weight in font_files:
    b64 = base64.b64encode((SRC / "fonts" / fname).read_bytes()).decode("ascii")
    fonts_css += (
        "@font-face{font-family:'%s';font-style:normal;font-weight:%s;"
        "src:url(data:font/woff2;base64,%s) format('woff2');}\n" % (family, weight, b64)
    )

template = (SRC / "scene_template.html").read_text(encoding="utf-8")
html = (
    template.replace("__FONTS_CSS__", fonts_css)
    .replace("__DATA_JSON__", json.dumps(data, separators=(",", ":")))
    .replace("__DURATION_MS__", str(DURATION_MS))
)
(SRC / "scene.html").write_text(html, encoding="utf-8")
print(f"scene.html escrito: {len(html):,} bytes · N={data['n']} · 2014: NDVI {data['ndvi2014']} ({data['hip']['varNdviPct']}%) vs rend {data['rend2014']} qq/ha ({data['hip']['caidaPct']}%)")
