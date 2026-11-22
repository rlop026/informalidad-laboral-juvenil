"""Ingeniería de variables compartida por el cuaderno de la Fase 3 y el script de inferencia."""
import re
import numpy as np
import pandas as pd

OCUP = {1: "Directivos y profesionales", 2: "Directivos y profesionales", 3: "Técnicos",
        4: "Oficinistas", 5: "Servicios y ventas", 6: "Otras (cód. 6 y 10)",
        7: "Operarios y artesanos", 8: "Operadores de máquinas", 9: "No calificados",
        10: "Otras (cód. 6 y 10)"}
TRAMOS = {1: "Solo", 2: "2 a 5", 3: "6 a 10", 4: "11 a 20", 5: "21 a 30", 6: "31 a 50",
          7: "51 a 100", 8: "101 a 500", 9: "Más de 500"}
ETQ_TAM = {**TRAMOS, -1: "Sin tamaño válido (-1)", 11: "Código 11 (sin etiqueta)"}

NUM = ["edad", "educ_anios", "mujer", "rural", "horas", "antiguedad", "clima_educativo"]
CAT_BASE = ["educ_nivel", "ocup_grp", "rama", "departamento"]


def parse_periodo(s):
    """'2024-T1' / 'T1-2024' / '20241' -> (2024, 1)."""
    s = str(s)
    m = re.search(r"(20\d{2})", s)
    anio = int(m.group(1))
    resto = s[:m.start()] + s[m.end():]
    q = re.search(r"[1-4]", resto)
    return anio, (int(q.group(0)) if q else 1)


def _map_codigo(serie, dic, otro):
    return serie.map(lambda v: dic.get(int(v), otro) if pd.notna(v) else "Sin dato")


def preparar(df):
    """Deriva las columnas que usa el modelo. No toca la variable objetivo."""
    d = df.copy()
    if "periodo" in d.columns:
        ap = d["periodo"].map(parse_periodo)
        d["anio"] = [a for a, _ in ap]
        d["trim"] = [q for _, q in ap]
        d["t_idx"] = (d["anio"] - d["anio"].min()) * 4 + d["trim"]
    d["tam_cat"] = _map_codigo(d["tam_empresa"], ETQ_TAM, "Otro")
    d["ocup_grp"] = _map_codigo(d["ocupacion"], OCUP, "Otras (cód. 6 y 10)")
    for c in ["educ_nivel", "entorno_informal", "rama", "departamento"]:
        if c in d.columns:
            d[c] = d[c].astype(str)
    for c in ["mujer", "rural"]:
        if c in d.columns:
            d[c] = d[c].astype(float)
    return d
