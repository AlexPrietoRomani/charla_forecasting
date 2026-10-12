import pandas as pd
import numpy as np

# Official data extracted from INEI Compendio Estadístico Cajamarca 2017 and 2025
# Source 1: INEI - Compendio Estadístico Cajamarca 2017 (Lib1492), Cuadro 12.1.8 (p. 231) y Cuadro 12.2.8 (p. 245)
# Source 2: INEI - Compendio Estadístico Cajamarca 2025 (CompDptal2025), Cuadro 12.1.8 (p. 213) y Cuadro 12.2.8 (p. 227)
# Primary Agency: Dirección Regional de Agricultura y Riego - Cajamarca / MIDAGRI

records = [
    # 2010 - 2016 from Cajamarca 2017
    {"anio": 2010, "superficie_cosechada_ha": 25055, "produccion_t": 26084, "fuente": "INEI / DRAC Cajamarca", "documento": "Compendio Estadístico Cajamarca 2017", "pagina": "231, 245"},
    {"anio": 2011, "superficie_cosechada_ha": 25534, "produccion_t": 26679, "fuente": "INEI / DRAC Cajamarca", "documento": "Compendio Estadístico Cajamarca 2017", "pagina": "231, 245"},
    {"anio": 2012, "superficie_cosechada_ha": 25910, "produccion_t": 22805, "fuente": "INEI / DRAC Cajamarca", "documento": "Compendio Estadístico Cajamarca 2017", "pagina": "231, 245"},
    {"anio": 2013, "superficie_cosechada_ha": 25909, "produccion_t": 19530, "fuente": "INEI / DRAC Cajamarca", "documento": "Compendio Estadístico Cajamarca 2017", "pagina": "231, 245"},
    {"anio": 2014, "superficie_cosechada_ha": 25910, "produccion_t": 11916, "fuente": "INEI / DRAC Cajamarca", "documento": "Compendio Estadístico Cajamarca 2017", "pagina": "231, 245"},
    {"anio": 2015, "superficie_cosechada_ha": 16375, "produccion_t": 12772, "fuente": "INEI / DRAC Cajamarca", "documento": "Compendio Estadístico Cajamarca 2017", "pagina": "231, 245"},
    {"anio": 2016, "superficie_cosechada_ha": 17189, "produccion_t": 12886, "fuente": "INEI / DRAC Cajamarca", "documento": "Compendio Estadístico Cajamarca 2017", "pagina": "231, 245"},
    # 2018 - 2024 from Cajamarca 2025
    {"anio": 2018, "superficie_cosechada_ha": 21142, "produccion_t": 19088, "fuente": "INEI / MIDAGRI OIA", "documento": "Compendio Estadístico Cajamarca 2025", "pagina": "213, 227"},
    {"anio": 2019, "superficie_cosechada_ha": 21258, "produccion_t": 23170, "fuente": "INEI / MIDAGRI OIA", "documento": "Compendio Estadístico Cajamarca 2025", "pagina": "213, 227"},
    {"anio": 2020, "superficie_cosechada_ha": 15426, "produccion_t": 25104, "fuente": "INEI / MIDAGRI OIA", "documento": "Compendio Estadístico Cajamarca 2025", "pagina": "213, 227"},
    {"anio": 2021, "superficie_cosechada_ha": 22128, "produccion_t": 23826, "fuente": "INEI / MIDAGRI OIA", "documento": "Compendio Estadístico Cajamarca 2025", "pagina": "213, 227"},
    {"anio": 2022, "superficie_cosechada_ha": 22359, "produccion_t": 24618, "fuente": "INEI / MIDAGRI OIA", "documento": "Compendio Estadístico Cajamarca 2025", "pagina": "213, 227"},
    {"anio": 2023, "superficie_cosechada_ha": 22359, "produccion_t": 25526, "fuente": "INEI / MIDAGRI OIA", "documento": "Compendio Estadístico Cajamarca 2025", "pagina": "213, 227"},
    {"anio": 2024, "superficie_cosechada_ha": 22359, "produccion_t": 23539, "fuente": "INEI / MIDAGRI OIA", "documento": "Compendio Estadístico Cajamarca 2025", "pagina": "213, 227"},
]

df = pd.DataFrame(records)
# Compute rendimiento in kg/ha and qq/ha (1 quintal pergamino = 46 kg)
df["rendimiento_kg_ha"] = (df["produccion_t"] * 1000.0 / df["superficie_cosechada_ha"]).round(2)
df["rendimiento_qq_ha"] = (df["rendimiento_kg_ha"] / 46.0).round(2)

# Arithmetic check
calc_diff = np.abs(df["produccion_t"] * 1000.0 / df["superficie_cosechada_ha"] - df["rendimiento_kg_ha"]) / df["rendimiento_kg_ha"]
assert (calc_diff < 0.001).all(), "Error en control aritmético de coherencia"

output_path = "data/raw/cafe_real/midagri_jaen_rendimiento.csv"
df.to_csv(output_path, index=False)
print(f"Exported {len(df)} records to {output_path}")
print(df[["anio", "superficie_cosechada_ha", "produccion_t", "rendimiento_kg_ha", "rendimiento_qq_ha"]])
