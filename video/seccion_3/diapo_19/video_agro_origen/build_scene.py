#!/usr/bin/env python3
"""Genera scene.html: entrada de 30 s para la Diapo 19 (Sección 3), 'El agro inventó el forecasting'. Datos reales de Jaén (24 campañas)."""

import base64
import json
import pathlib
import sys

import pandas as pd

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "_pipeline"))
from subtitles import load_beats, write_vtt  # noqa: E402

SRC = pathlib.Path(__file__).resolve().parent
ROOT = SRC.parents[3]

FPS = 30
DURATION_MS = 30000

df = pd.read_csv(ROOT / "data/caso_2/cafe_jaen_campanias.csv")


def col(name):
    return [None if pd.isna(v) else round(float(v), 4) for v in df[name]]


data = {
    "n": int(len(df)),
    "years": [int(v) for v in df["campania"]],
    "ndvi": col("ndvi_anual"),
    "rend": col("rendimiento_qq_ha"),
    "lluvia": col("lluvia_flor_mm"),
    "ndviMin": round(float(df["ndvi_anual"].min()), 3),
    "ndviMax": round(float(df["ndvi_anual"].max()), 3),
    "rendMax": round(float(df["rendimiento_qq_ha"].max()), 2),
    "yearStart": int(df["campania"].min()),
    "yearEnd": int(df["campania"].max()),
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

video_cfg = json.loads((SRC / "video.json").read_text(encoding="utf-8"))
beats = load_beats(SRC / "beats.json")
template = (SRC / "scene_template.html").read_text(encoding="utf-8")
html = (
    template.replace("__FONTS_CSS__", fonts_css)
    .replace("__DATA_JSON__", json.dumps(data, separators=(",", ":")))
    .replace("__DURATION_MS__", str(DURATION_MS))
    .replace("__BEATS_JSON__", json.dumps(beats, ensure_ascii=False, separators=(",", ":")))
)
(SRC / "scene.html").write_text(html, encoding="utf-8")
write_vtt(beats, video_cfg["start_ms"], video_cfg["time_scale"], SRC / "narration.vtt")
print(f"scene.html escrito: {len(html):,} bytes · N={data['n']} campañas {data['yearStart']}–{data['yearEnd']} · rendMax={data['rendMax']} qq/ha")
