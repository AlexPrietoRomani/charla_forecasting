"""
Archivo: deck_glossary.py
Fecha de modificación: 28/10/2026
Autor: Alex Prieto Romani

Descripción:
    Glosario de términos técnicos del deck de forecasting para público sin formación
    estadística. Cada entrada define el término en lenguaje llano, ofrece una analogía
    cotidiana y lista variantes de escritura que aparecen en los prototipos.

Acciones Principales:
    - Expone el diccionario GLOSSARY con definición, analogía y alias por término.
    - Expone terms() con todos los términos y alias, sin duplicados, para inyectores y validadores.

Estructura Interna:
    - `GLOSSARY`: Diccionario de término (en minúscula) a su definición, analogía y alias.
    - `terms`: Devuelve la lista plana de términos y alias sin duplicados.

Entradas / Dependencias:
    - Ninguna. Solo biblioteca estándar.

Salidas / Efectos:
    - Ninguna. El módulo no escribe archivos ni modifica estado global.

Ejemplo de Integración:
    from front.deck_glossary import GLOSSARY, terms
    lista_terminos = terms()
"""

GLOSSARY: dict[str, dict[str, str | list[str]]] = {
    "p10/p90": {
        "def": "Franja donde el valor real caerá con 80% de probabilidad.",
        "analogia": "como el pronóstico del tiempo que dice 'entre 20 y 28 grados'.",
        "alias": ["P10", "P90", "P10-P90"],
    },
    "cono de incertidumbre": {
        "def": "Franja que se ensancha cuanto más lejos miramos hacia el futuro.",
        "analogia": "como el cono de un faro: más lejos, más abierto.",
        "alias": ["cono"],
    },
    "ndvi": {
        "def": "Índice satelital que mide cuán verde está la vegetación desde el espacio.",
        "analogia": "como medir la salud del cultivo con una foto aérea en color.",
    },
    "lag": {
        "def": "Valor de un periodo anterior, usado como pista para predecir el siguiente.",
        "analogia": "como mirar ayer para adivinar cuánto lloverá hoy.",
        "alias": ["lags"],
    },
    "p-valor": {
        "def": "Probabilidad de que una diferencia sea solo fruto del azar.",
        "analogia": "empate técnico, como dos corredores que llegan juntos.",
        "alias": ["p-value", "p ="],
    },
    "zero-shot": {
        "def": "Modelo que predice series nuevas sin entrenarse con ellas previamente.",
        "analogia": "como un cocinero que prepara un plato nuevo sin haberlo practicado.",
        "alias": ["zero shot"],
    },
    "extratrees": {
        "def": "Método que combina cientos de reglas sencillas y promedia sus respuestas.",
        "analogia": "como consultar a cien vecinos y quedarse con la respuesta media.",
        "alias": ["extra trees", "extra-trees"],
    },
    "parche": {
        "def": "Bloque pequeño de la señal que el modelo mira como una sola unidad.",
        "analogia": "como cortar una foto en cuadritos para analizarla por partes.",
        "alias": ["patch", "parches", "patches"],
    },
    "conformal": {
        "def": "Técnica que ajusta el margen de error para cumplir una cobertura prometida.",
        "analogia": "como una cuerda de seguridad calibrada según la altura del salto.",
        "alias": ["predicción conforme", "conformal prediction"],
    },
    "lstm": {
        "def": "Red neuronal que recuerda patrones de secuencias largas en el tiempo.",
        "analogia": "como un cuaderno de bitácora que recuerda lo ocurrido días atrás.",
    },
    "forecasting": {
        "def": "Predicción de valores futuros a partir del historial de datos.",
        "analogia": "como estimar la cosecha mirando los registros de años previos.",
        "alias": ["forecast", "pronóstico"],
    },
    "benchmark": {
        "def": "Prueba comparativa que pone varios modelos frente a las mismas condiciones.",
        "analogia": "como una carrera de atletas con la misma pista y reglas.",
    },
    "patchtst": {
        "def": "Modelo de inteligencia artificial que predice mirando bloques de tiempo consecutivos.",
        "analogia": "como leer un libro por capítulos en lugar de palabra por palabra.",
    },
    "mae": {
        "def": "Promedio de cuánto se equivoca el pronóstico, sin importar el signo.",
        "analogia": "como contar cuántos minutos llega tarde el bus, en promedio.",
        "alias": ["error absoluto medio", "error medio absoluto"],
    },
    "rmse": {
        "def": "Error típico que castiga más los fallos grandes que los pequeños.",
        "analogia": "como el termómetro de tu casa: marca casi lo real.",
        "alias": ["raíz del error cuadrático medio"],
    },
    "walk-forward": {
        "def": "Evaluación que simula el pronóstico avanzando en el tiempo, sin ver el futuro.",
        "analogia": "como ir jugando una liga: cada fecha solo usas lo ocurrido antes.",
        "alias": ["walk forward"],
    },
    "fenologia": {
        "def": "Estudio de las etapas del ciclo de una planta según el clima.",
        "analogia": "como el calendario de una cosecha: brotes, flores y frutos.",
        "alias": ["fenológico", "fenológica"],
    },
    "vpd": {
        "def": "Déficit de presión de vapor: qué tan seco está el aire para las hojas.",
        "analogia": "como la sequedad que siente la piel en un día de viento caliente.",
        "alias": ["déficit de presión de vapor"],
    },
    "lyapunov": {
        "def": "Medida de cuánto se amplifican los errores pequeños con el tiempo.",
        "analogia": "como el efecto mariposa: un empujón mínimo cambia todo el resultado.",
        "alias": ["exponente de Lyapunov"],
    },
    "kpa": {
        "def": "Unidad de presión: mide con qué fuerza la planta jala el agua del suelo.",
        "analogia": "como una pajita que cuesta más succionar cuando el suelo está seco.",
    },
    "arima": {
        "def": "Modelo clásico que predice combinando valores pasados y errores pasados.",
        "analogia": "como predecir el clima de mañana mirando los últimos días.",
    },
    "deep learning": {
        "def": "Familia de métodos de inteligencia artificial con muchas capas de cálculo.",
        "analogia": "como una cadena de filtros que refina el agua paso a paso.",
        "alias": ["aprendizaje profundo"],
    },
    "sobreajuste": {
        "def": "Cuando el modelo memoriza el pasado y falla con datos nuevos.",
        "analogia": "como estudiar solo las respuestas del examen anterior.",
        "alias": ["overfitting", "sobreajustado"],
    },
    "holdout": {
        "def": "Conjunto de datos reservado para probar el modelo, sin usarlo al entrenar.",
        "analogia": "el examen final con preguntas nuevas.",
        "alias": ["hold-out", "hold out"],
    },
    "estacionalidad": {
        "def": "Patrón que se repite con regularidad, como cada año o cada día.",
        "analogia": "como las lluvias que llegan cada temporada del año.",
        "alias": ["estacional", "estacionales"],
    },
    "lai": {
        "def": "Índice de área foliar: cuánta superficie de hojas hay por metro de suelo.",
        "analogia": "como cuántas capas de hojas forman el techo de un bosque.",
        "alias": ["índice de área foliar"],
    },
    "gdd": {
        "def": "Grados-día: acumulado de calor útil que necesita una planta para avanzar.",
        "analogia": "como juntar monedas diarias hasta reunir lo necesario para comprar algo.",
        "alias": ["grados-día", "grados día"],
    },
    "xgboost": {
        "def": "Método que va sumando reglas sencillas y corrige cada error anterior.",
        "analogia": "como un equipo de revisores donde cada uno corrige al anterior.",
    },
    "diebold-mariano": {
        "def": "Prueba estadística que compara si dos pronósticos son realmente distintos.",
        "analogia": "como preguntar si dos cocineros cocinan de verdad distinto, o es casualidad.",
        "alias": ["diebold mariano"],
    },
    "o(l²)": {
        "def": "Costo de cálculo que crece con el cuadrado del tamaño de los datos.",
        "analogia": "como comparar cada persona de un salón con todas las demás.",
        "alias": ["O(L^2)", "O(L2)"],
    },
    "modelo fundacional": {
        "def": "Modelo grande entrenado con datos muy variados, listo para usar en muchas tareas.",
        "analogia": "como un chef con formación general que cocina cualquier receta.",
        "alias": ["foundation model", "fundacionales"],
    },
    "transformer": {
        "def": "Arquitectura de IA que mira todas las partes de una secuencia a la vez.",
        "analogia": "como leer una página entera de un vistazo, no palabra a palabra.",
        "alias": ["transformers"],
    },
    "reanálisis": {
        "def": "Base de datos climática que reconstruye el pasado mezclando modelos y observaciones.",
        "analogia": "como armar la historia del clima con fotos, diarios y testigos.",
        "alias": ["ERA5", "reanalysis"],
    },
    "senamhi": {
        "def": "Servicio meteorológico oficial de Perú que mide el clima del país.",
        "analogia": "como la estación del clima de tu ciudad, pero a escala nacional.",
    },
    "ecmwf": {
        "def": "Centro europeo de predicción del tiempo que produce modelos globales de clima.",
        "analogia": "como un meteorólogo mundial que mira el planeta entero a la vez.",
    },
    "serie temporal": {
        "def": "Secuencia de mediciones ordenadas en el tiempo, como la temperatura diaria.",
        "analogia": "como el registro diario de tu presión arterial anotado cada mañana.",
        "alias": ["series temporales", "serie de tiempo"],
    },
    "varianza": {
        "def": "Qué tanto cambian los valores alrededor de su promedio.",
        "analogia": "como la diferencia entre un tiro certero y uno disperso.",
    },
}


def terms() -> list[str]:
    """
    Devuelve todos los términos y alias del glosario sin duplicados.

    La deduplicación no distingue mayúsculas, porque el validador compara
    las menciones del texto en minúscula. Conserva el orden de aparición.

    Returns:
        list[str]: Lista de claves y alias, cada uno aparece una sola vez.
    """
    vistos: set[str] = set()
    resultado: list[str] = []
    for clave, entrada in GLOSSARY.items():
        candidatos = [clave, *entrada.get("alias", [])]
        for candidato in candidatos:
            # Clave normalizada para descartar variantes con distinta capitalización
            normalizado = str(candidato).casefold()
            if normalizado not in vistos:
                vistos.add(normalizado)
                resultado.append(str(candidato))
    return resultado
