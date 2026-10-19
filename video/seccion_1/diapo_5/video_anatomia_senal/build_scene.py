#!/usr/bin/env python3
"""Genera scene.html: escena cinemática (34 s) para la Diapo 5, Acto 1 'Anatomía de la señal'. El render usa el tramo [4 s, 27 s] estirado a 30 s."""

import base64
import json
import pathlib

import pandas as pd

SRC = pathlib.Path(__file__).resolve().parent
ROOT = SRC.parents[3]

FPS = 30
DURATION_MS = 34000

df = pd.read_csv(ROOT / "data/caso_1/senamhi_diario.csv", parse_dates=["fecha"]).set_index("fecha")
s = df["tmax"].astype(float)
y = s

T = s.rolling(365, center=True, min_periods=180).mean()
S = s.groupby(s.index.month).transform("mean") - s.mean()
M30 = s.rolling(30, center=True, min_periods=15).mean()
C = M30 - T
E = s - T - S - C


def rnd(series, nd):
    return [None if pd.isna(v) else round(float(v), nd) for v in series]


idx_max = int(y.values.argmax())
idx_cmax = int(C.values.argmax())

year_ticks = []
for year in range(2019, 2026):
    ts = pd.Timestamp(f"{year}-01-01")
    if ts in s.index:
        year_ticks.append({"i": int(s.index.get_loc(ts)), "label": str(year)})

data = {
    "n": int(len(s)),
    "start": s.index[0].strftime("%Y-%m-%d"),
    "end": s.index[-1].strftime("%Y-%m-%d"),
    "mean": round(float(s.mean()), 2),
    "min": round(float(s.min()), 1),
    "max": round(float(s.max()), 1),
    "maxDate": s.index[idx_max].strftime("%d·%m·%Y"),
    "sAbs": round(float(S.abs().max()), 2),
    "eStd": round(float(E.std()), 2),
    "y": rnd(y, 1),
    "t": rnd(T, 2),
    "s": rnd(S, 2),
    "m30": rnd(M30, 2),
    "c": rnd(C, 2),
    "e": rnd(E, 2),
    "idxMax": idx_max,
    "idxCMax": idx_cmax,
    "yearTicks": year_ticks,
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
print(f"scene.html escrito: {len(html):,} bytes · n={data['n']} · ymáx={data['max']} ({data['maxDate']})")
