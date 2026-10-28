#!/usr/bin/env python3
"""Auditoría automatizada de la Fase 12 (F12): claridad para público sin estadística.

Verifica el deck HTML (21 prototipos) y las escenas de video de la Fase 12 con seis
reglas: inventario de términos técnicos sin tooltip, cobertura del glosario,
longitud de titulares, cifras con decimales fuera de `data-expert`, jerarquía de
cabeceras y tamaños de fuente y artefactos de las escenas de video.
"""

import argparse
import base64
import fnmatch
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
from collections import Counter
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path
from types import ModuleType

BASE_DIR = Path(__file__).resolve().parent.parent

# Lista copiada de scripts/audit_f10_layout_typography.py (los 21 prototipos del deck).
PROTOTIPOS = [
    "docs/notebooklm/seccion_1/prototipos/5_Anatomia_de_la_senal_temporal_v3.html",
    "docs/notebooklm/seccion_1/prototipos/6_Era_1_La_parsimonia_lineal_v3.html",
    "docs/notebooklm/seccion_1/prototipos/7_Era_2_El_puente_tabular.html",
    "docs/notebooklm/seccion_1/prototipos/8_Era_3_Deep_Learning_y_Parches.html",
    "docs/notebooklm/seccion_1/prototipos/9_Era_4_Modelos_Fundacionales_Zero_Shot.html",
    "docs/notebooklm/seccion_1/prototipos/10_El_Cono_de_Incertidumbre_y_Prediccion_Conforme.html",
    "docs/notebooklm/seccion_1/prototipos/11_Arquitectura_de_Decision_y_Cierre_Ejecutivo.html",
    "docs/notebooklm/seccion_2/prototipos/12_Caso_1_Auditoria_Iquitos.html",
    "docs/notebooklm/seccion_2/prototipos/13_Datos_SENAMHI_Punchana.html",
    "docs/notebooklm/seccion_2/prototipos/14_Trampa_Arboles_Meseta_vs_Diferencias.html",
    "docs/notebooklm/seccion_2/prototipos/15_Benchmark_14_Modelos_Tierra_vs_Supercomputo.html",
    "docs/notebooklm/seccion_2/prototipos/16_Pronostico_7_Dias_Cono_P10_P90.html",
    "docs/notebooklm/seccion_2/prototipos/17_Pipeline_Codigo_Diferencias_ExtraTrees.html",
    "docs/notebooklm/seccion_3/prototipos/19_c_mo_el_agro_invent_el_forecasting.html",
    "docs/notebooklm/seccion_3/prototipos/20_del_almanaque_al_sat_lite.html",
    "docs/notebooklm/seccion_3/prototipos/21_f_sica_biol_gica_y_el_l_mite_algor_tmico.html",
    "docs/notebooklm/seccion_3/prototipos/22_reloj_fenol_gico_del_caf.html",
    "docs/notebooklm/seccion_3/prototipos/23_precisi_n_actual_y_las_tres_trampas.html",
    "docs/notebooklm/seccion_4/prototipos/25_Datos_24_Campanias_Jaen.html",
    "docs/notebooklm/seccion_4/prototipos/26_Trampa_Satelite_NDVI_vs_Clima.html",
    "docs/notebooklm/seccion_4/prototipos/27_Validacion_WalkForward_Benchmark_Jaen.html",
]

GLOSSARY_RELPATH = "front/deck_glossary.py"

# Términos usados si deck_glossary.py no existe o no aporta terms().
TERMINOS_FIJOS = (
    "lyapunov",
    "diebold-mariano",
    "mase",
    "msiw",
    "conformal",
    "cuantil",
    "holdout",
    "4d-var",
    "p-valor",
    "rmse",
    "mae",
    "arima",
    "lstm",
    "patchtst",
    "zero-shot",
    "lag",
    "walk-forward",
    "ndvi",
    "lai",
    "vpd",
    "kpa",
    "extratrees",
    "lightgbm",
    "transformer",
    "token",
    "parche",
    "varianza",
    "entropía",
    "autorregresivo",
    "heterocedástico",
)

LIMITE_SIN_TOOLTIP = 25
LIMITE_TAKEAWAY_PALABRAS = 15
LIMITE_HERO_PALABRAS = 12
LIMITE_DEF_PALABRAS = 15
LIMITE_RUTA_CORTA = 3
MIN_FONT_PX = 22.0
TOP_FRECUENCIA = 20

# Cifras con 2+ decimales; el lookbehind evita partir versiones y palabras con dígitos.
RE_CIFRA = re.compile(r"(?<![\w.,])-?\d+[.,]\d{2,}(?!\d)")
RE_TAXONOMIA = re.compile(r"\b(VÍA|Via|Era|Pilar|Etapa)\s+\d+( de \d+)?\b")
RE_BOTON_NAVEGACION = re.compile(r"<button[^>]*>[^<]*(Pase a|Ir al|Ir a |Ver )")
RE_RUTA_CORTA = re.compile(r'data-route\s*=\s*"corta"')
RE_DATA_ROUTE = re.compile(r"data-route\s*=")
RE_FONT_SIZE = re.compile(r"font-size\s*:\s*([^;}]+)")
RE_PX = re.compile(r"^(\d+(?:\.\d+)?)px\b")
RE_IFRAME_BASE64 = re.compile(r"data:text/html;base64,([A-Za-z0-9+/=]+)")
RE_TITULO_HTML = re.compile(r"<title>([^<]*)</title>", re.IGNORECASE)
RE_GL_TERM_CLASE = re.compile(r"class=\"[^\"]*\bgl-term\b")
# Etiquetas de cabecera que no son parte del titular (con o sin emoji 💡).
RE_ETIQUETA_TAKEAWAY = re.compile(r"(💡\s*)?\b(Idea Clave|Regla de Oro)\b:?")

VOID_TAGS = frozenset(
    {
        "area",
        "base",
        "br",
        "col",
        "embed",
        "hr",
        "img",
        "input",
        "link",
        "meta",
        "source",
        "track",
        "wbr",
    }
)
TAGS_OCULTOS = frozenset({"script", "style"})
TAGS_EXENTOS = frozenset({"code", "pre"})
CLASES_CABECERA = frozenset({"eyebrow", "stage-tag", "proc-year"})


@dataclass
class Element:
    """Representa un elemento HTML con su texto visible acumulado."""

    tag: str
    attrs: dict[str, str]
    text_parts: list[str] = field(default_factory=list)

    @property
    def classes(self) -> set[str]:
        """Devuelve las clases CSS del elemento como conjunto."""
        return set(self.attrs.get("class", "").split())

    @property
    def text(self) -> str:
        """Devuelve el texto visible del elemento con espacios normalizados."""
        return " ".join(" ".join(self.text_parts).split())


@dataclass(frozen=True)
class Segmento:
    """Fragmento de texto con los ancestros que determinan su tratamiento."""

    texto: str
    oculto: bool  # Dentro de <script> o <style>.
    tooltip: bool  # Dentro de un span.gl-term ya explicado.
    exento: bool  # Dentro de data-expert, <code> o <pre>.


@dataclass
class HtmlDoc:
    """Documento HTML analizado con segmentos de texto y elementos."""

    raw: str
    segmentos: list[Segmento]
    elementos: list[Element]


class _Extractor(HTMLParser):
    """Recorre el HTML y registra los segmentos de texto con sus ancestros."""

    def __init__(self) -> None:
        """Inicializa la pila de elementos abiertos y los acumuladores."""
        super().__init__(convert_charrefs=True)
        self._pila: list[Element] = []
        self.elementos: list[Element] = []
        self.segmentos: list[Segmento] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        """Registra un elemento y lo apila si no es vacío."""
        elemento = Element(tag=tag, attrs={k: v or "" for k, v in attrs})
        self.elementos.append(elemento)
        if tag not in VOID_TAGS:
            self._pila.append(elemento)

    def handle_endtag(self, tag: str) -> None:
        """Desapila hasta el elemento abierto que coincide con la etiqueta."""
        for indice in range(len(self._pila) - 1, -1, -1):
            if self._pila[indice].tag == tag:
                del self._pila[indice:]
                return

    def handle_data(self, data: str) -> None:
        """Clasifica el texto según sus ancestros y lo añade a los elementos abiertos."""
        oculto = any(e.tag in TAGS_OCULTOS for e in self._pila)
        tooltip = any(e.tag == "span" and "gl-term" in e.classes for e in self._pila)
        exento = any(
            "data-expert" in e.attrs or e.tag in TAGS_EXENTOS for e in self._pila
        )
        self.segmentos.append(Segmento(data, oculto, tooltip, exento))
        if not oculto:
            for elemento in self._pila:
                elemento.text_parts.append(data)


def parse_html(raw: str) -> HtmlDoc:
    """Analiza el HTML y devuelve su documento con texto visible clasificado."""
    extractor = _Extractor()
    extractor.feed(raw)
    extractor.close()
    return HtmlDoc(
        raw=raw, segmentos=extractor.segmentos, elementos=extractor.elementos
    )


def _prototipos(root: Path, archivos: list[Path] | None) -> list[Path]:
    """Devuelve las rutas de prototipos a auditar, por defecto los 21 del deck."""
    if archivos is not None:
        return archivos
    return [root / relativa for relativa in PROTOTIPOS]


def _leer_doc(ruta: Path) -> HtmlDoc:
    """Lee y analiza un archivo HTML en UTF-8."""
    return parse_html(ruta.read_text(encoding="utf-8"))


def _patron_termino(termino: str) -> re.Pattern[str]:
    """Compila el patrón que busca un término como palabra completa."""
    return re.compile(r"(?<!\w)" + re.escape(termino) + r"(?!\w)", re.IGNORECASE)


def _contexto_glosario(root: Path) -> tuple[list[str], dict[str, str]]:
    """Devuelve los términos a buscar y el mapa alias -> término canónico.

    La lista combina TERMINOS_FIJOS con terms() de deck_glossary.py si existe. El
    mapa usa GLOSSARY[k]["alias"], así una forma alterna cuenta como su término.
    """
    terminos = set(TERMINOS_FIJOS)
    mapa: dict[str, str] = {}
    modulo, _ = _cargar_glosario(root)
    if modulo is not None:
        if callable(getattr(modulo, "terms", None)):
            terminos.update(str(t).lower() for t in modulo.terms())
        glosario = getattr(modulo, "GLOSSARY", None)
        if isinstance(glosario, dict):
            for clave, entrada in glosario.items():
                canonico = str(clave).lower()
                mapa[canonico] = canonico
                alias = entrada.get("alias", []) if isinstance(entrada, dict) else []
                for forma in alias:
                    mapa[str(forma).lower()] = canonico
    return sorted(terminos), mapa


@dataclass
class Inventario:
    """Conteo de términos técnicos de un prototipo.

    El tooltip se inyecta en compilación (front/prototype_engine.inject_glossary),
    así que el fuente no trae `.gl-term`. Un término está cubierto si tiene entrada
    o alias en GLOSSARY; la regla de FAIL cuenta solo los no cubiertos.
    """

    nombre: str
    bruto: Counter[str]  # Ocurrencias por término canónico, cubiertos o no.
    no_cubiertos: Counter[str]  # Ocurrencias de términos sin entrada ni alias.
    con_tooltip: int  # Spans .gl-term ya presentes en el fuente.

    @property
    def total_bruto(self) -> int:
        """Devuelve la suma de ocurrencias de todos los términos técnicos."""
        return sum(self.bruto.values())

    @property
    def total_no_cubiertos(self) -> int:
        """Devuelve la suma de ocurrencias de términos sin entrada ni alias."""
        return sum(self.no_cubiertos.values())


def _inventario_doc(
    nombre: str, doc: HtmlDoc, terminos: list[str], mapa: dict[str, str]
) -> Inventario:
    """Cuenta los términos técnicos visibles fuera de span.gl-term."""
    texto = " ".join(s.texto for s in doc.segmentos if not s.oculto and not s.tooltip)
    bruto: Counter[str] = Counter()
    no_cubiertos: Counter[str] = Counter()
    for termino in terminos:
        apariciones = len(_patron_termino(termino).findall(texto))
        if not apariciones:
            continue
        if termino in mapa:
            # Un alias suma al término canónico, así no aparece como "sin entrada".
            bruto[mapa[termino]] += apariciones
        else:
            bruto[termino] += apariciones
            no_cubiertos[termino] += apariciones
    con_tooltip = sum(
        1 for e in doc.elementos if e.tag == "span" and "gl-term" in e.classes
    )
    return Inventario(
        nombre=nombre,
        bruto=bruto,
        no_cubiertos=no_cubiertos,
        con_tooltip=con_tooltip,
    )


def _inventarios(root: Path, archivos: list[Path] | None) -> list[Inventario]:
    """Calcula el inventario de los prototipos que existen."""
    terminos, mapa = _contexto_glosario(root)
    resultado = []
    for ruta in _prototipos(root, archivos):
        if ruta.is_file():
            resultado.append(
                _inventario_doc(ruta.name, _leer_doc(ruta), terminos, mapa)
            )
    return resultado


def tabla_inventario(root: Path, archivos: list[Path] | None = None) -> list[str]:
    """Devuelve las líneas de la tabla de inventario de términos por prototipo."""
    cabecera = (
        f"{'Prototipo':<60} {'no cubiertos':>12} {'bruto (INFO)':>12}"
        f" {'con tooltip':>11}  top no cubiertos"
    )
    lineas = [cabecera]
    for inv in _inventarios(root, archivos):
        top = ", ".join(t for t, _ in inv.no_cubiertos.most_common(3))
        lineas.append(
            f"{inv.nombre[:60]:<60} {inv.total_no_cubiertos:>12}"
            f" {inv.total_bruto:>12} {inv.con_tooltip:>11}  {top}"
        )
    return lineas


def check_inventario(
    root: Path, archivos: list[Path] | None = None
) -> list[tuple[bool, str]]:
    """Falla si un prototipo tiene más de 25 términos sin entrada ni alias en GLOSSARY.

    El conteo bruto de términos se informa en el detalle, pero no decide el FAIL.
    """
    resultados = []
    terminos, mapa = _contexto_glosario(root)
    for ruta in _prototipos(root, archivos):
        if not ruta.is_file():
            resultados.append((False, f"{ruta.name}: no existe"))
            continue
        inv = _inventario_doc(ruta.name, _leer_doc(ruta), terminos, mapa)
        resultados.append(
            (
                inv.total_no_cubiertos <= LIMITE_SIN_TOOLTIP,
                (
                    f"{inv.nombre}: {inv.total_no_cubiertos} no cubiertos "
                    f"(límite {LIMITE_SIN_TOOLTIP}); INFO bruto {inv.total_bruto}, "
                    f"{inv.con_tooltip} con tooltip en fuente"
                ),
            )
        )
    return resultados


def _cargar_glosario(root: Path) -> tuple[ModuleType | None, str]:
    """Importa front/deck_glossary.py y devuelve el módulo o el motivo del fallo."""
    ruta = root / GLOSSARY_RELPATH
    if not ruta.is_file():
        return None, f"falta {GLOSSARY_RELPATH}"
    especificacion = importlib.util.spec_from_file_location("deck_glossary", ruta)
    if especificacion is None or especificacion.loader is None:
        return None, f"no se pudo cargar {GLOSSARY_RELPATH}"
    modulo = importlib.util.module_from_spec(especificacion)
    try:
        especificacion.loader.exec_module(modulo)
    except Exception as error:  # noqa: BLE001 - el glosario puede lanzar cualquier error al importarse.
        return None, f"error al importar {GLOSSARY_RELPATH}: {error}"
    return modulo, ""


def check_glosario(
    root: Path, archivos: list[Path] | None = None
) -> list[tuple[bool, str]]:
    """Valida deck_glossary.py y que los términos frecuentes tengan entrada."""
    modulo, motivo = _cargar_glosario(root)
    if modulo is None:
        return [(False, f"{motivo} (la tarea de glosario aún no está hecha)")]
    glosario = getattr(modulo, "GLOSSARY", None)
    if not isinstance(glosario, dict):
        return [(False, f"{GLOSSARY_RELPATH}: GLOSSARY no es un dict")]

    resultados = []
    for clave, entrada in glosario.items():
        if clave != str(clave).lower():
            resultados.append((False, f"clave '{clave}' no está en minúscula"))
        if not isinstance(entrada, dict):
            resultados.append((False, f"'{clave}': la entrada no es un dict"))
            continue
        definicion = str(entrada.get("def", "")).strip()
        analogia = str(entrada.get("analogia", "")).strip()
        palabras = len(definicion.split())
        if palabras > LIMITE_DEF_PALABRAS:
            resultados.append(
                (
                    False,
                    f"'{clave}': def con {palabras} palabras (límite {LIMITE_DEF_PALABRAS})",
                )
            )
        if not analogia:
            resultados.append((False, f"'{clave}': analogia vacía"))

    conteo: Counter[str] = Counter()
    for inv in _inventarios(root, archivos):
        conteo.update(inv.bruto)
    sin_entrada = [
        termino
        for termino, _ in conteo.most_common(TOP_FRECUENCIA)
        if termino not in {str(k).lower() for k in glosario}
    ]
    if sin_entrada:
        resultados.append((False, f"términos frecuentes sin entrada: {sin_entrada}"))
    else:
        resultados.append(
            (
                True,
                f"{len(glosario)} entradas; top {TOP_FRECUENCIA} términos cubiertos",
            )
        )
    return resultados


def check_titulares(
    root: Path, archivos: list[Path] | None = None
) -> list[tuple[bool, str]]:
    """Valida la longitud de takeaways y titulares .hero-title de cada prototipo."""
    resultados = []
    for ruta in _prototipos(root, archivos):
        if not ruta.is_file():
            resultados.append((False, f"{ruta.name}: no existe"))
            continue
        doc = _leer_doc(ruta)
        takeaways = [
            e
            for e in doc.elementos
            if "executive-takeaway" in e.classes or e.attrs.get("id") == "speakerBox"
        ]
        heroes = [e for e in doc.elementos if "hero-title" in e.classes]
        for take in takeaways:
            palabras = len(_sin_etiqueta_takeaway(take.text).split())
            resultados.append(
                (
                    palabras <= LIMITE_TAKEAWAY_PALABRAS,
                    (
                        f"{ruta.name}: takeaway con {palabras} palabras "
                        f"(límite {LIMITE_TAKEAWAY_PALABRAS})"
                    ),
                )
            )
        if not takeaways:
            resultados.append((True, f"{ruta.name}: sin .executive-takeaway"))
        if not heroes:
            resultados.append(
                (True, f"{ruta.name}: sin .hero-title, pendiente T12.2.1")
            )
        for hero in heroes:
            palabras = len(hero.text.split())
            resultados.append(
                (
                    palabras <= LIMITE_HERO_PALABRAS,
                    (
                        f"{ruta.name}: hero-title con {palabras} palabras "
                        f"(límite {LIMITE_HERO_PALABRAS})"
                    ),
                )
            )
    return resultados


def _sin_etiqueta_takeaway(texto: str) -> str:
    """Quita las etiquetas de cabecera del takeaway antes de contar palabras."""
    return RE_ETIQUETA_TAKEAWAY.sub(" ", texto)


def _es_excepcion_cifra(texto: str, inicio: int, fin: int, cifra: str) -> bool:
    """Indica si una cifra es separador de miles, año, coordenada o versión."""
    # Separador de miles con coma: 30,490 o 2,557 (coma + exactamente 3 dígitos).
    if re.fullmatch(r"-?\d+,\d{3}", cifra):
        return True
    despues = texto[fin : fin + 8]
    if re.match(r"\s*[°º]", despues):  # Coordenada como -3.69°.
        return True
    if re.match(r"\.\d", despues):  # Versión encadenada como 1.10.2.
        return True
    entero = re.sub(r"^-", "", cifra).replace(",", ".").split(".")[0]
    return len(entero) == 4 and 1900 <= int(entero) <= 2100  # Año.


def check_cifras(
    root: Path, archivos: list[Path] | None = None
) -> list[tuple[bool, str]]:
    """Falla si hay cifras con 2+ decimales visibles fuera de data-expert o código."""
    resultados = []
    for ruta in _prototipos(root, archivos):
        if not ruta.is_file():
            resultados.append((False, f"{ruta.name}: no existe"))
            continue
        hallazgos = []
        for segmento in _leer_doc(ruta).segmentos:
            if segmento.oculto or segmento.exento:
                continue
            for coincidencia in RE_CIFRA.finditer(segmento.texto):
                cifra = coincidencia.group(0)
                if not _es_excepcion_cifra(
                    segmento.texto, coincidencia.start(), coincidencia.end(), cifra
                ):
                    hallazgos.append(cifra)
        resultados.append(
            (
                not hallazgos,
                (
                    f"{ruta.name}: {len(hallazgos)} cifras con 2+ decimales fuera de "
                    f"data-expert {hallazgos[:10]}"
                ),
            )
        )
    return resultados


def check_jerarquia(
    root: Path, archivos: list[Path] | None = None
) -> list[tuple[bool, str]]:
    """Falla con taxonomías viejas en cabeceras, botones de navegación o rutas largas."""
    resultados = []
    for ruta in _prototipos(root, archivos):
        if not ruta.is_file():
            resultados.append((False, f"{ruta.name}: no existe"))
            continue
        doc = _leer_doc(ruta)
        cabeceras = [
            e
            for e in doc.elementos
            if e.tag in {"h1", "h2"} or e.classes & CLASES_CABECERA
        ]
        taxonomias = [
            m.group(0) for e in cabeceras for m in RE_TAXONOMIA.finditer(e.text)
        ]
        botones = RE_BOTON_NAVEGACION.findall(doc.raw)
        resultados.append(
            (
                not taxonomias,
                f"{ruta.name}: taxonomías viejas en cabeceras {taxonomias[:5]}",
            )
        )
        resultados.append(
            (
                not botones,
                f"{ruta.name}: {len(botones)} botones de navegación interna",
            )
        )

        # Las marcas data-route pueden estar en cualquier elemento (stage, proc-node, ...).
        cortas = len(RE_RUTA_CORTA.findall(doc.raw))
        resultados.append(
            (
                cortas <= LIMITE_RUTA_CORTA,
                (
                    f"{ruta.name}: {cortas} marcas data-route=corta "
                    f"(límite {LIMITE_RUTA_CORTA})"
                ),
            )
        )
        nodos = [e for e in doc.elementos if "proc-node" in e.classes]
        if nodos:
            hay_marca = RE_DATA_ROUTE.search(doc.raw) is not None
            resultados.append(
                (
                    hay_marca,
                    f"{ruta.name}: {len(nodos)} proc-node, "
                    + (
                        "con data-route"
                        if hay_marca
                        else "sin ninguna marca data-route"
                    ),
                )
            )
    return resultados


def _archivos_git(root: Path) -> list[Path] | None:
    """Devuelve los archivos versionados bajo video/ o None si no hay repo git."""
    try:
        salida = subprocess.run(
            ["git", "ls-files", "video"],
            cwd=root,
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError:
        return None
    if salida.returncode != 0:
        return None
    return [root / linea for linea in salida.stdout.splitlines() if linea]


def _check_mp4_versionados(root: Path) -> list[tuple[bool, str]]:
    """Falla si hay videos versionados (*_v<n>*.mp4) bajo control de versiones."""
    archivos = _archivos_git(root)
    if archivos is None:  # Sin git se revisa el disco en lugar de la lista versionada.
        archivos = (
            list((root / "video").rglob("*.mp4")) if (root / "video").is_dir() else []
        )
    versionados = [
        p.relative_to(root).as_posix()
        for p in archivos
        if fnmatch.fnmatch(p.name, "*_v[0-9]*.mp4")
    ]
    return [
        (
            not versionados,
            f"{len(versionados)} videos versionados (*_v<n>*.mp4) {versionados[:5]}",
        )
    ]


def _check_capturas_duplicadas(root: Path) -> list[tuple[bool, str]]:
    """Falla si dos o más capture.mjs tienen el mismo contenido (mismo md5)."""
    capturas = sorted(
        p
        for p in root.rglob("capture.mjs")
        if not {".git", "node_modules"} & set(p.parts)
    )
    por_hash: dict[str, list[str]] = {}
    for captura in capturas:
        digest = hashlib.md5(captura.read_bytes()).hexdigest()
        por_hash.setdefault(digest, []).append(captura.relative_to(root).as_posix())
    duplicados = {h: rutas for h, rutas in por_hash.items() if len(rutas) > 1}
    if not duplicados:
        return [(True, f"{len(capturas)} capture.mjs sin duplicados por md5")]
    return [
        (False, f"capture.mjs duplicados (md5 {h[:8]}): {rutas}")
        for h, rutas in duplicados.items()
    ]


def check_video(root: Path) -> list[tuple[bool, str]]:
    """Valida fuentes, artefactos de narración y capturas de las escenas de video."""
    resultados: list[tuple[bool, str]] = []
    escenas = sorted(root.glob("video/*/*/*/scene_template.html"))
    if not escenas:
        resultados.append((False, "no hay video/*/*/*/scene_template.html"))

    for escena in escenas:
        nombre = escena.relative_to(root).as_posix()
        # Un solo resultado por escena evita repetir cada declaración en la salida.
        pequenos = sorted(
            {
                float(c.group(1))
                for valor in RE_FONT_SIZE.findall(escena.read_text(encoding="utf-8"))
                if (c := RE_PX.match(valor.strip())) and float(c.group(1)) < MIN_FONT_PX
            }
        )
        if pequenos:
            resultados.append(
                (
                    False,
                    f"{nombre}: font-size menores a {MIN_FONT_PX:.0f}px en px {pequenos}",
                )
            )
        else:
            resultados.append((True, f"{nombre}: font-size >= {MIN_FONT_PX:.0f}px"))

    carpetas = [escena.parent for escena in escenas]
    sin_artefactos = [
        c
        for c in carpetas
        if not (c / "beats.json").is_file() and not (c / "narration.vtt").is_file()
    ]
    if carpetas and len(sin_artefactos) == len(carpetas):
        resultados.append((True, "beats.json y narration.vtt pendientes, T12.3.2"))
    else:
        for carpeta in carpetas:
            faltantes = [
                nombre
                for nombre in ("beats.json", "narration.vtt")
                if not (carpeta / nombre).is_file()
            ]
            if faltantes:
                resultados.append(
                    (
                        False,
                        f"{carpeta.relative_to(root).as_posix()}: faltan {faltantes}",
                    )
                )

    resultados.extend(_check_capturas_duplicadas(root))
    resultados.extend(_check_mp4_versionados(root))
    return resultados


def check_bundle(root: Path, archivo: Path | None = None) -> list[tuple[bool, str]]:
    """Verifica que cada prototipo compilado en el bundle trae spans .gl-term.

    Decodifica los iframes `data:text/html;base64` de presentacion.html. Un prototipo
    sin `.gl-term` indica que la inyección de tooltips no ocurrió en compilación.
    """
    ruta = archivo if archivo is not None else root / "presentacion.html"
    if not ruta.is_file():
        return [(False, f"{ruta.name}: no existe")]
    cargas = RE_IFRAME_BASE64.findall(ruta.read_text(encoding="utf-8"))
    if not cargas:
        return [(False, f"{ruta.name}: no hay iframes data:text/html;base64")]
    resultados = []
    for indice, carga in enumerate(cargas, start=1):
        try:
            html = base64.b64decode(carga).decode("utf-8")
        except ValueError as error:  # binascii.Error hereda de ValueError.
            resultados.append((False, f"iframe {indice}: no decodifica ({error})"))
            continue
        titulo = RE_TITULO_HTML.search(html)
        nombre = titulo.group(1).strip() if titulo else f"iframe {indice}"
        numero = len(RE_GL_TERM_CLASE.findall(html))
        resultados.append(
            (
                numero > 0,
                f"{nombre}: {numero} .gl-term en el bundle compilado",
            )
        )
    return resultados


REGLAS = {
    "inventario": check_inventario,
    "glosario": check_glosario,
    "titulares": check_titulares,
    "cifras": check_cifras,
    "jerarquia": check_jerarquia,
    "video": check_video,
    "bundle": check_bundle,
}

REGLAS_SOLO_INFORMAR = frozenset({"inventario", "cifras"})
# Chequeos opt-in: no entran en --all; se piden con --bundle de forma explícita.
REGLAS_OPCIONALES = frozenset({"bundle"})


def main(argv: list[str] | None = None) -> int:
    """Ejecuta las reglas seleccionadas y devuelve 1 si alguna falla."""
    parser = argparse.ArgumentParser(
        description="Auditoría F12 de claridad del deck y videos."
    )
    for nombre in REGLAS:
        parser.add_argument(f"--{nombre}", action="store_true", help=f"regla {nombre}")
    parser.add_argument("--all", action="store_true", help="ejecuta todas las reglas")
    parser.add_argument(
        "--solo-informar",
        action="store_true",
        help="convierte los FAIL de inventario y cifras en INFO",
    )
    parser.add_argument("--json", action="store_true", help="salida estructurada")
    parser.add_argument("--root", type=Path, default=BASE_DIR, help="raíz del repo")
    args = parser.parse_args(argv)
    # Fuerza UTF-8 en la salida: las consolas de Windows usan cp1252 por defecto.
    sys.stdout.reconfigure(encoding="utf-8")

    seleccion = (
        [n for n in REGLAS if n not in REGLAS_OPCIONALES]
        if args.all
        else [n for n in REGLAS if getattr(args, n)]
    )
    if not seleccion:
        parser.print_help()
        return 1

    root = args.root.resolve()
    fallos = 0
    salida_json: dict[str, list[dict[str, object]]] = {}
    for nombre in seleccion:
        filas = REGLAS[nombre](root)
        if nombre == "inventario" and not args.json:
            print("\n".join(tabla_inventario(root)))
        filas_finales = []
        for ok, detalle in filas:
            informativo = (
                args.solo_informar and nombre in REGLAS_SOLO_INFORMAR and not ok
            )
            if informativo:
                estado = "INFO"
            else:
                estado = "OK" if ok else "FAIL"
                if not ok:
                    fallos += 1
            filas_finales.append({"estado": estado, "detalle": detalle})
            if not args.json:
                print(f"[{estado}] {nombre} — {detalle}")
        salida_json[nombre] = filas_finales

    if args.json:
        print(
            json.dumps(
                {"reglas": salida_json, "fallos": fallos}, ensure_ascii=False, indent=2
            )
        )
    else:
        print(f"Resultado: {fallos} fallo(s)")
    return 1 if fallos else 0


if __name__ == "__main__":
    raise SystemExit(main())
