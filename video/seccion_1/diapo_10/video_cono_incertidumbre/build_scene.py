#!/usr/bin/env python3
"""Genera scene.html: entrada de 30 s para la Diapo 10 (Sección 1), 'La ilusión de la certeza y el cono de incertidumbre'. Datos reales de Punchana."""

import base64
import json
import pathlib

import pandas as pd

SRC = pathlib.Path(__file__).resolve().parent
ROOT = SRC.parents[3]

FPS = 30
DURATION_MS = 30000

fc = pd.read_csv(ROOT / "data/caso_1/senamhi_forecast_7d.csv")
di = pd.read_csv(ROOT / "data/caso_1/senamhi_diario.csv", parse_dates=["fecha"]).set_index("fecha")

s = di["tmax"].astype(float)
T = s.rolling(365, center=True, min_periods=180).mean()
S = s.groupby(s.index.month).transform("mean") - s.mean()
C = s.rolling(30, center=True, min_periods=15).mean() - T
E = s - T - S - C

MES = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"]
days = ["%02d·%s" % (int(d[8:10]), MES[int(d[5:7]) - 1]) for d in fc["fecha"].astype(str)]

qhat = float(((fc["ci_upper_p90"] - fc["ci_lower_p10"]) / 2).mean())

data = {
    "days": days,
    "obs": [round(float(v), 1) for v in fc["tmax_observada"]],
    "et": [round(float(v), 2) for v in fc["pred_extratrees"]],
    "lo": [round(float(v), 2) for v in fc["ci_lower_p10"]],
    "hi": [round(float(v), 2) for v in fc["ci_upper_p90"]],
    "qhat": round(qhat, 2),
    "n": len(s),
    "sigma": round(float(E.std()), 2),
    "record": round(float(s.max()), 1),
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
print(
    f"scene.html escrito: {len(html):,} bytes · n={data['n']} · σ={data['sigma']} · récord={data['record']} · "
    f"banda {min(data['lo'])}–{max(data['hi'])} · friaje {data['obs'][3]} °C · q̂={data['qhat']}"
)
