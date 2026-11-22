"""Configuración común a los tres cuadernos: rutas del proyecto, semilla y guardado de figuras.

Todos los cuadernos importan este módulo después de su celda 0, de modo que las rutas son
siempre relativas a la raíz del repositorio y no dependen de dónde se abra el cuaderno
(Jupyter local, VS Code o Google Colab tras clonar el repositorio).
"""
from pathlib import Path
import random

import numpy as np

SEMILLA = 42  # semilla única del proyecto (Fases 1, 2 y 3)


def raiz_proyecto(inicio=None):
    """Devuelve la carpeta raíz del repositorio (la que contiene src/entorno.py)."""
    inicio = Path(inicio or Path.cwd()).resolve()
    for carpeta in [inicio, *inicio.parents]:
        if (carpeta / "src" / "entorno.py").exists():
            return carpeta
    raise FileNotFoundError(
        "No se encontró la raíz del repositorio. Abrí el cuaderno desde la carpeta "
        "notebooks/ del proyecto o ejecutá primero la celda 0 (en Colab clona el repositorio)."
    )


def rutas(fase):
    """Crea (si hace falta) y devuelve las rutas que usa la fase indicada ('fase1', 'fase2', 'fase3')."""
    raiz = raiz_proyecto()
    r = {
        "raiz": raiz,
        "raw": raiz / "data" / "raw",              # microdatos originales del INE (.SAV)
        "processed": raiz / "data" / "processed",  # dataset limpio que produce la Fase 1
        "out": raiz / "output" / fase,             # tablas de resultados de la fase
        "fig": raiz / "output" / fase / "figuras", # figuras de la fase
    }
    for clave in ("processed", "out", "fig"):
        r[clave].mkdir(parents=True, exist_ok=True)
    if fase == "fase3":
        r["modelos"] = r["out"] / "modelos"
        r["modelos"].mkdir(parents=True, exist_ok=True)
    return r


def fijar_semilla(semilla=SEMILLA):
    """Fija las semillas de random y numpy para que las ejecuciones sean idénticas."""
    random.seed(semilla)
    np.random.seed(semilla)
    return np.random.default_rng(semilla)


def guardar_figura(carpeta, nombre, fig=None, dpi=160):
    """Guarda la figura actual (o la indicada) como PNG en la carpeta de figuras de la fase."""
    import matplotlib.pyplot as plt

    fig = fig or plt.gcf()
    destino = Path(carpeta) / f"{nombre}.png"
    fig.savefig(destino, dpi=dpi, bbox_inches="tight")
    return destino
