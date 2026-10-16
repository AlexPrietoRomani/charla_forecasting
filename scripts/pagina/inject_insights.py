import re

insights_p1 = {
    1: ('💡 REGLA DE INGENIERÍA', 'En horizontes h > 7 días, la entropía atmosférica domina la señal predictiva. Toda decisión logística debe fundamentarse en bandas de cuantil (P10–P90), jamás en un escalar.'),
    2: ('💡 LEY DE PARSIMONIA', 'Aumentar parámetros sin suficiente volumen de entrenamiento genera sobreajuste espurio: un modelo simple con pocas variables domina en series cortas o ruidosas.'),
    3: ('💡 DESCOMPOSICIÓN LOESS', 'El algoritmo STL aísla la señal anual de 365 días mediante regresión ponderada local, permitiendo que el residuo identifique eventos anómalos reales como friajes antárticos.'),
    4: ('💡 TECHO DE CAPACIDAD', 'Modelos lineales o redes densas asumen crecimiento sin cotas. En problemas agroclimáticos, acotar la salida con asíntotas biológicas evita proyecciones físicamente absurdas.'),
    5: ('💡 DIAGNÓSTICO FORENSE', 'El árbol dividió el espacio en hojas cuyo máximo histórico era 31.5 °C. Ante una anomalía récord de 37.4 °C, promedió el pasado; diferenciar la serie (Δy) resolvió el colapso.'),
    6: ('💡 EFICIENCIA COMPUTACIONAL', 'El mecanismo de parches de PatchTST reduce la longitud de la secuencia de 336 a 42 tokens, disminuyendo la complejidad de la matriz de atención de 112,896 a 1,764 operaciones.'),
    7: ('💡 GENERALIZACIÓN ZERO-SHOT', 'Modelos como TimesFM 2.5 aprenden primitivas estadísticas universales en 100B de puntos. El prompt local de 512 días condiciona el pronóstico sin actualizar ningún peso.'),
    8: ('💡 LÍMITE ESPECTRAL ÓPTICO', 'Al superar un Índice de Área Foliar (LAI) de 3.0, el dosel intercepta toda la radiación roja fotosintéticamente activa, haciendo que el NDVI se aplane asintóticamente en 0.75-0.80.'),
    9: ('💡 FUNCIÓN DE PÉRDIDA AGRÍCOLA', 'El impacto del clima está modulado por la fenología: 30 mm de lluvia en floración aseguran el cuajado; los mismos 30 mm en plena cosecha pudren las cerezas en la planta.'),
    10: ('💡 DIVERGENCIA NUMÉRICA', 'Las discrepancias de hasta 9.3 °C entre NOAA GFS y ECMWF IFS demuestran que parametrizar la convección tropical en mallas de 9 a 25 km sigue siendo un problema físico abierto.')
}

with open('scripts/deck_slides_p1.py', 'r', encoding='utf-8') as f:
    text = f.read()

for i, (label, desc) in insights_p1.items():
    card = f'''      <div class="card-insight">
        <span class="insight-label">{label}</span>
        <p class="insight-text">{desc}</p>
      </div>'''
    pattern = rf'(data-index=\"{i}\".*?</ul>\s*)(\s*<div class=\"card-frase-clave\">)'
    text = re.sub(pattern, rf'\1{card}\n\2', text, flags=re.DOTALL)

with open('scripts/deck_slides_p1.py', 'w', encoding='utf-8') as f:
    f.write(text)

insights_p2 = {
    11: ('💡 SALTO COMPUTACIONAL', 'GraphCast sustituye la integración numérica explícita de ecuaciones diferenciales por propagación de mensajes sobre un grafo icosaédrico, reduciendo el gasto energético en 99.8%.'),
    12: ('💡 PROTOCOLO DE LIMPIEZA', 'Se aplicó interpolación estricta sin fuga de información futura sobre el 9.7% de huecos de la estación Punchana (-3.693°S, -73.255°W), preservando la dinámica térmica diaria.'),
    13: ('💡 PRUEBA DIEBOLD-MARIANO', 'El test estadístico confirma que ExtraTrees (RMSE 1.880 °C) empata con TimesFM (p = 0.275) y supera a LSTM profunda (p = 0.031) consumiendo 70 veces menos cómputo.'),
    14: ('💡 GESTIÓN OPERATIVA', 'La banda P10–P90 capturó el 71.4% de las observaciones reales (5 de 7 días) en la ventana de prueba a 7 días. La línea central sirve de referencia; la banda define el margen de seguridad.'),
    15: ('💡 CONSISTENCIA ARITMÉTICA', 'Se auditaron 24 compendios anuales de MIDAGRI/SIEA verificando la regla Producción = Superficie Cosechada × Rendimiento (Δ < 0.1%). Se excluyeron datos sintéticos.'),
    16: ('💡 PATOLOGÍA VEGETAL VS SATÉLITE', 'En la crisis de la roya (2012-2014), el rendimiento cayó -56.0% mientras el NDVI subió +1.4%. El hongo afectó los granos antes de defoliar el dosel; el sensor óptico fue ciego.'),
    17: ('💡 VALIDACIÓN EXPANSIVA HONESTA', 'El protocolo Walk-Forward entrena año a año sin ver el futuro: la combinación de variables fenológicas con tendencia redujo el MAE a 4.51 qq/ha frente a 5.32 de satélite solo.'),
    18: ('💡 CONCLUSIÓN CIENTÍFICA', 'Ninguna arquitectura moderna compensa la falta de rigor metodológico. La parsimonia matemática y la comprensión de los mecanismos físicos dominan sobre la complejidad bruta.'),
    19: ('💡 MATRIZ DE DECISIÓN', 'Elige la herramienta según la escala del sistema: parsimonia local para series individuales; modelos en diferencias para tendencias; modelos de frontera para catálogos masivos.'),
    20: ('💡 CIENCIA ABIERTA & REPRODUCIBLE', 'Cuadernos interactivos en Google Colab con código documentado, compendios oficiales auditados y datasets limpios disponibles bajo licencia MIT para la comunidad académica.')
}

with open('scripts/deck_slides_p2.py', 'r', encoding='utf-8') as f:
    text = f.read()

for i, (label, desc) in insights_p2.items():
    card = f'''      <div class="card-insight">
        <span class="insight-label">{label}</span>
        <p class="insight-text">{desc}</p>
      </div>'''
    pattern = rf'(data-index=\"{i}\".*?</ul>\s*)(\s*<div class=\"card-frase-clave\">)'
    text = re.sub(pattern, rf'\1{card}\n\2', text, flags=re.DOTALL)

with open('scripts/deck_slides_p2.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Insights injected into all 20 slides successfully!')
