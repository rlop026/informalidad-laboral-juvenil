"""Script de inferencia. Uso:
    python src/predict.py --modelo output/modelo_informalidad.joblib --entrada nuevos.csv --salida pred.csv
El CSV de entrada debe traer las mismas columnas crudas del dataset limpio de la Fase 1
(tam_empresa, ocupacion, educ_nivel, educ_anios, edad, mujer, rural, entorno_informal,
clima_educativo, rama, horas, antiguedad, departamento, según el conjunto de variables del modelo)."""
import argparse, sys
from pathlib import Path
import joblib
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from features import preparar  # noqa: E402


def predecir(ruta_modelo, df):
    b = joblib.load(ruta_modelo)
    d = preparar(df)
    faltan = [c for c in b["variables"] if c not in d.columns]
    if faltan:
        raise ValueError(f"Faltan columnas en la entrada: {faltan}")
    p = b["modelo"].predict_proba(d[b["variables"]])[:, 1]
    return pd.DataFrame({"prob_informal": p, "pred_informal": (p >= b["umbral"]).astype(int)}, index=df.index)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--modelo", required=True)
    ap.add_argument("--entrada", required=True)
    ap.add_argument("--salida", default="predicciones.csv")
    a = ap.parse_args()
    out = predecir(a.modelo, pd.read_csv(a.entrada, encoding="utf-8-sig"))
    out.to_csv(a.salida, index=False)
    print(f"{len(out)} predicciones -> {a.salida}")
