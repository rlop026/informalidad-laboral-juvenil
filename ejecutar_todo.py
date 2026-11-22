"""Ejecuta los tres cuadernos del proyecto en orden y exporta cada uno a HTML.

Uso (desde la raíz del repositorio, con el entorno ya instalado):
    python ejecutar_todo.py            # Fases 1, 2 y 3
    python ejecutar_todo.py 2 3        # solo las fases indicadas

Cada cuaderno se ejecuta de principio a fin con su carpeta notebooks/ como directorio de trabajo.
El cuaderno ejecutado se guarda en su lugar (con salidas) y su HTML va a output/faseN/.
"""
import sys
import time
from pathlib import Path

import nbformat
from nbconvert import HTMLExporter
from nbconvert.preprocessors import ExecutePreprocessor

RAIZ = Path(__file__).resolve().parent
CUADERNOS = {
    1: "01_Fase1_Comprension_y_EDA.ipynb",
    2: "02_Fase2_Analisis_Inferencial.ipynb",
    3: "03_Fase3_Modelado_Predictivo.ipynb",
}


def ejecutar(fase):
    ruta = RAIZ / "notebooks" / CUADERNOS[fase]
    print(f"[Fase {fase}] Ejecutando {ruta.name} ...", flush=True)
    inicio = time.time()
    nb = nbformat.read(ruta, as_version=4)
    ExecutePreprocessor(timeout=3600, kernel_name="python3").preprocess(
        nb, {"metadata": {"path": str(ruta.parent)}})
    nbformat.write(nb, ruta)
    html, _ = HTMLExporter().from_notebook_node(nb)
    destino = RAIZ / "output" / f"fase{fase}" / ruta.with_suffix(".html").name
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(html, encoding="utf-8")
    print(f"[Fase {fase}] OK en {time.time() - inicio:.0f} s · HTML: {destino.relative_to(RAIZ)}", flush=True)


if __name__ == "__main__":
    fases = [int(a) for a in sys.argv[1:]] or [1, 2, 3]
    for f in fases:
        ejecutar(f)
    print("Listo. Resultados en output/ y dataset limpio en data/processed/.")
