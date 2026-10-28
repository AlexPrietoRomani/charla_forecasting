"""
Archivo: deck_plain_numbers.py
Fecha de modificación: 28/10/2026
Autor: Alex Prieto Romani

Descripción:
    Tabla de cifras del deck traducidas a lenguaje llano para público sin estadística.
    Cada entrada enlaza la cifra visible ("show") con su fuente en data/ ("src"), de modo que
    el redondeo mostrado se pueda comprobar contra el dato exacto, y añade una frase
    cotidiana ("plain") de máximo 10 palabras.

Acciones Principales:
    - Expone el diccionario PLAIN con fuente, cifra visible y frase llana.
    - Expone resolve() para leer el valor exacto desde CSV o JSON de data/.
    - Expone check_all() para verificar que cada "show" es el redondeo de su fuente.
    - Expone unverified_keys() con las entradas sin fuente en data/ (prototipo o paper).

Estructura Interna:
    - `PLAIN`: Diccionario clave -> {"src", "show", "plain"}.
    - `resolve`: Devuelve el valor numérico de una fuente "ruta#campo" o None.
    - `check_all`: Devuelve la lista de errores de consistencia (vacía si todo cuadra).
    - `unverified_keys`: Devuelve las claves cuya fuente es "prototipo:...".

Gramática de `src`:
    - "ruta.csv#<fila>.<columna>": fila cuyo primer campo empieza por <fila>.
    - "ruta.csv#cobertura(<real>,<inferior>,<superior>)": porcentaje de filas con el real
      dentro del intervalo.
    - "ruta.json#<clave>.<subclave>": valor anidado.
    - "prototipo:<archivo>": cifra que solo vive en el prototipo (no verificable en data/).

Entradas / Dependencias:
    - data/caso_1/*.csv y data/caso_2/*.csv|json. Solo biblioteca estándar.

Salidas / Efectos:
    - Ninguna. Solo lectura de archivos.

Ejemplo de Integración:
    from front.deck_plain_numbers import PLAIN, check_all
    assert not check_all()
"""

import csv
import json
import re
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
MAX_PLAIN_WORDS = 10
PROTOTYPE_PREFIX = "prototipo:"
NUMBER_RE = re.compile(r"[-+]?\d+(?:\.\d+)?")
_BENCH_1 = "data/caso_1/benchmark_punchana.csv"
_FORECAST = "data/caso_1/senamhi_forecast_7d.csv"
_HYPOTHESES = "data/caso_2/cafe_jaen_hipotesis.json"
_BENCH_2 = "data/caso_2/benchmark_cafe.csv"
_CAMPAIGNS = "data/caso_2/cafe_jaen_campanias.csv"
_P27 = PROTOTYPE_PREFIX + "27_Validacion_WalkForward_Benchmark_Jaen.html"

PLAIN: dict[str, dict[str, str]] = {
    "rmse_extratrees": {
        "src": f"{_BENCH_1}#ExtraTrees.rmse_1d",
        "show": "±1.9 °C",
        "plain": "como el termómetro de tu casa",
    },
    "rmse_timesfm": {
        "src": f"{_BENCH_1}#TimesFM.rmse_1d",
        "show": "±1.9 °C",
        "plain": "el mismo error que el modelo gratuito",
    },
    "rmse_ecmwf": {
        "src": f"{_BENCH_1}#ECMWF.rmse_1d",
        "show": "±2.5 °C",
        "plain": "medio grado peor que el modelo local",
    },
    "rmse_noaa": {
        "src": f"{_BENCH_1}#NOAA.rmse_1d",
        "show": "±2.6 °C",
        "plain": "el supercómputo falla más que un árbol",
    },
    "dm_p_timesfm": {
        "src": f"{_BENCH_1}#TimesFM.p_valor_vs_mejor",
        "show": "p = 0.7",
        "plain": "empate técnico",
    },
    "dm_p_ecmwf": {
        "src": f"{_BENCH_1}#ECMWF.p_valor_vs_mejor",
        "show": "p = 0.03",
        "plain": "diferencia real",
    },
    "dm_p_noaa": {
        "src": f"{_BENCH_1}#NOAA.p_valor_vs_mejor",
        "show": "p = 0.009",
        "plain": "diferencia real, casi seguro no es azar",
    },
    "cpu_extratrees": {
        "src": f"{_BENCH_1}#ExtraTrees.tiempo_s",
        "show": "0.25 s",
        "plain": "un cuarto de segundo",
    },
    "tiempo_timesfm": {
        "src": f"{_BENCH_1}#TimesFM.tiempo_s",
        "show": "7.9 s",
        "plain": "casi ocho segundos y con GPU",
    },
    "cobertura_cono": {
        "src": f"{_FORECAST}#cobertura(tmax_observada,ci_lower_p10,ci_upper_p90)",
        "show": "71.4 %",
        "plain": "5 de cada 7 días cayeron dentro del cono",
    },
    "r_ndvi": {
        "src": f"{_HYPOTHESES}#H1_saturacion.pearson_r",
        "show": "r ≈ 0.15",
        "plain": "casi ninguna relación",
    },
    "p_ndvi": {
        "src": f"{_HYPOTHESES}#H1_saturacion.p_valor",
        "show": "p = 0.6",
        "plain": "puro azar",
    },
    "cv_ndvi": {
        "src": f"{_HYPOTHESES}#H1_saturacion.cv_ndvi_pct",
        "show": "2.3 %",
        "plain": "el verde casi no cambia de un año a otro",
    },
    "r_lluvia_floracion": {
        "src": f"{_HYPOTHESES}#H2_fenologia.r_lluvia_flor",
        "show": "r ≈ 0.75",
        "plain": "relación fuerte",
    },
    "r_deficit_hidrico": {
        "src": f"{_HYPOTHESES}#H2_fenologia.r_deficit_hidrico",
        "show": "r ≈ 0.76",
        "plain": "relación fuerte",
    },
    "r_tmax_floracion": {
        "src": f"{_HYPOTHESES}#H2_fenologia.r_tmax_flor",
        "show": "r ≈ -0.56",
        "plain": "relación moderada: más calor, menos cosecha",
    },
    "mae_tendencia": {
        "src": f"{_HYPOTHESES}#H3_fusion.mae_tendencia_qq_ha",
        "show": "4.8 qq/ha",
        "plain": "unos 220 kg de café por hectárea",
    },
    "mae_ndvi": {
        "src": f"{_HYPOTHESES}#H3_fusion.mae_solo_satelite_qq_ha",
        "show": "5.3 qq/ha",
        "plain": "unos 245 kg de café por hectárea",
    },
    "mae_fusion": {
        "src": f"{_HYPOTHESES}#H3_fusion.mae_fusion_qq_ha",
        "show": "4.5 qq/ha",
        "plain": "unos 210 kg de café por hectárea",
    },
    "mae_m12_rf": {
        "src": f"{_BENCH_2}#M12.mae_walkforward",
        "show": "3.7 qq/ha",
        "plain": "unos 170 kg de café por hectárea",
    },
    "mae_m05_ndvi": {
        "src": f"{_BENCH_2}#M05.mae_walkforward",
        "show": "5.4 qq/ha",
        "plain": "unos 250 kg de café por hectárea",
    },
    "error_2020_ndvi": {
        "src": f"{_BENCH_2}#M05.error_abs_2020",
        "show": "18.3 qq/ha",
        "plain": "el satélite falló por media cosecha",
    },
    "roya_caida": {
        "src": f"{_HYPOTHESES}#H4_roya_invisibilidad.caida_rendimiento_pct",
        "show": "-56 %",
        "plain": "la cosecha cayó a menos de la mitad",
    },
    "roya_ndvi": {
        "src": f"{_HYPOTHESES}#H4_roya_invisibilidad.variacion_ndvi_pct",
        "show": "+1.4 %",
        "plain": "el satélite ni lo notó",
    },
    "record_2020": {
        "src": f"{_CAMPAIGNS}#2020.rendimiento_qq_ha",
        "show": "35.4 qq/ha",
        "plain": "la mejor cosecha de la serie",
    },
    "cosecha_2014": {
        "src": f"{_CAMPAIGNS}#2014.rendimiento_qq_ha",
        "show": "10.0 qq/ha",
        "plain": "el peor año, golpeado por la roya",
    },
    "margen_conformal": {
        "src": _P27,
        "show": "±8.3 qq/ha",
        "plain": "unos 380 kg de margen de error",
    },
}


def _normalize(text: str) -> str:
    """Reemplaza el signo menos tipográfico por guion ASCII para poder parsear números."""
    return text.replace("−", "-")


def _read_csv_value(path: Path, selector: str, column: str) -> float | None:
    """Devuelve la columna de la primera fila cuyo primer campo empieza por selector."""
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        first_field = reader.fieldnames[0]
        for row in reader:
            if row[first_field].startswith(selector):
                return float(row[column].rstrip("%"))
    return None


def _read_coverage(path: Path, spec: str) -> float | None:
    """Calcula el porcentaje de filas con el valor real dentro de [inferior, superior]."""
    real_col, low_col, high_col = (name.strip() for name in spec.split(","))
    inside = total = 0
    with path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            total += 1
            inside += (
                float(row[low_col]) <= float(row[real_col]) <= float(row[high_col])
            )
    return 100.0 * inside / total if total else None


def _read_json_value(path: Path, dotted_key: str) -> float:
    """Recorre un JSON anidado por claves separadas con punto."""
    node = json.loads(path.read_text(encoding="utf-8"))
    for key in dotted_key.split("."):
        node = node[key]
    return float(node)


def resolve(src: str) -> float | None:
    """Devuelve el valor exacto de una fuente "ruta#campo", o None si no es verificable."""
    if src.startswith(PROTOTYPE_PREFIX) or "#" not in src:
        return None
    rel_path, field = src.split("#", 1)
    path = ROOT_DIR / rel_path
    if path.suffix == ".json":
        return _read_json_value(path, field)
    if field.startswith("cobertura(") and field.endswith(")"):
        return _read_coverage(path, field[len("cobertura(") : -1])
    selector, column = field.rsplit(".", 1)
    return _read_csv_value(path, selector, column)


def _shown_number(show: str) -> tuple[float, int] | None:
    """Extrae el primer número de "show" y su cantidad de decimales."""
    match = NUMBER_RE.search(_normalize(show))
    if match is None:
        return None
    token = match.group(0)
    decimals = len(token.split(".")[1]) if "." in token else 0
    return float(token), decimals


def check_all() -> list[str]:
    """Verifica que cada "show" sea el redondeo de su fuente; devuelve los errores."""
    errors = []
    for key, entry in PLAIN.items():
        shown = _shown_number(entry["show"])
        if shown is None:
            errors.append(f"{key}: 'show' sin número")
            continue
        value = resolve(entry["src"])
        if value is None:
            if not entry["src"].startswith(PROTOTYPE_PREFIX):
                errors.append(f"{key}: no se pudo resolver {entry['src']}")
            continue
        number, decimals = shown
        # Tolerancia de medio paso del último decimal mostrado (evita falsos por flotantes).
        if abs(value - number) > 0.5 * 10**-decimals + 1e-9:
            errors.append(f"{key}: {value} no redondea a {entry['show']}")
    return errors


def unverified_keys() -> list[str]:
    """Devuelve las claves cuya cifra no vive en data/ (fuente prototipo o paper)."""
    return [
        key for key, entry in PLAIN.items() if entry["src"].startswith(PROTOTYPE_PREFIX)
    ]
