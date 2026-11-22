# Determinantes y predicción de la informalidad laboral juvenil en Paraguay

**Data Science (Electiva) · Curso TQ · Trabajo Práctico Integrador · Grupo 5**
Universidad Nacional de Asunción — Facultad de Ingeniería

Integrantes: Isaac Ulises Gabriel González · Rubén David López · Martín Victorino Rodríguez
Docente: Prof. Dra. Margarita Ruiz Olazar

| Cuaderno | Fase | Abrir en Google Colab |
|---|---|---|
| `01_Fase1_Comprension_y_EDA.ipynb` | 1 · Comprensión, limpieza y análisis exploratorio | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rlop026/informalidad-laboral-juvenil/blob/main/notebooks/01_Fase1_Comprension_y_EDA.ipynb) |
| `02_Fase2_Analisis_Inferencial.ipynb` | 2 · Análisis inferencial | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rlop026/informalidad-laboral-juvenil/blob/main/notebooks/02_Fase2_Analisis_Inferencial.ipynb) |
| `03_Fase3_Modelado_Predictivo.ipynb` | 3 · Modelado predictivo | [![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/rlop026/informalidad-laboral-juvenil/blob/main/notebooks/03_Fase3_Modelado_Predictivo.ipynb) |

El informe final (5 páginas) está en [`informe/Informe_Final_Grupo5.pdf`](informe/Informe_Final_Grupo5.pdf).

---

## 1. Problema

En Paraguay, la mayoría de las personas ocupadas de 18 a 29 años trabaja en condición de
informalidad: no aporta a un sistema jubilatorio, no accede al seguro médico contributivo y carece
de estabilidad contractual. Las políticas de formalización suelen apoyarse en un diagnóstico
unifactorial —la falta de calificación— que orienta buena parte del gasto público hacia la
capacitación. El proyecto examina si ese supuesto es suficiente, comparando el peso de los atributos
**individuales**, del **puesto de trabajo**, del **territorio** y del **entorno del hogar**.

**Pregunta de investigación.** ¿Qué factores se asocian con la informalidad laboral de las personas
ocupadas no agropecuarias de 18 a 29 años en Paraguay entre 2024-T1 y 2026-T2, y cuánto aportan a
su predicción?

## 2. Objetivos

**General.** Identificar y comparar los factores asociados a la informalidad laboral juvenil y
evaluar su aporte ajustado (inferencia) y predictivo (modelado).

**Específicos.**

1. Construir un conjunto de datos reproducible a partir de los microdatos trimestrales de la EPHC (Fase 1).
2. Describir distribuciones y asociaciones bivariadas de los factores con la informalidad (Fase 1).
3. Contrastar formalmente hipótesis sobre tamaño del establecimiento, educación, entorno del hogar,
   ingresos y sexo, verificando supuestos y reportando tamaños del efecto (Fase 2).
4. Entrenar y evaluar clasificadores con validación temporal y sin fuga de información,
   comparándolos con líneas base (Fase 3).

## 3. Datos y fuente

| | |
|---|---|
| **Fuente** | Instituto Nacional de Estadística (INE) del Paraguay — Encuesta Permanente de Hogares Continua (EPHC), base de personas **REG02** |
| **Período** | 10 trimestres: 2024-T1 a 2026-T2 (factor de expansión revisión 2025) |
| **Acceso** | Portal de microdatos del INE: <https://www.ine.gov.py/microdatos/> · microdatos públicos y anonimizados (Ley 5282/2014) |
| **Datos crudos** | `data/raw/` — 10 archivos `.SAV`, 140.128 registros y 154 variables (instrucciones en [`data/raw/LEEME.md`](data/raw/LEEME.md)) |
| **Población de análisis** | Personas ocupadas no agropecuarias de 18 a 29 años con condición de informalidad definida |
| **Dataset final** | `data/processed/dataset_limpio.csv` — 12.691 personas, 10.055 hogares, 30 variables |
| **Variable objetivo** | `informal` (1 = informal, 0 = formal), a partir de la variable oficial `INFORMALIDAD` del INE |
| **Diccionario** | `data/processed/diccionario_final.csv` · bitácora de limpieza: `data/processed/bitacora_limpieza.csv` |

Los microdatos no contienen datos personales identificables; los identificadores del dataset son
códigos de muestreo (UPM, vivienda, hogar, línea) que el INE publica junto con la encuesta.

## 4. Estructura del repositorio

```
informalidad-laboral-juvenil/
├── README.md
├── requirements.txt              # versiones exactas del entorno
├── ejecutar_todo.py              # ejecuta los 3 cuadernos en orden y exporta HTML
├── data/
│   ├── raw/                      # 10 archivos .SAV del INE (entrada de la Fase 1) + LEEME.md
│   └── processed/                # dataset_limpio.csv, diccionario_final.csv, bitacora_limpieza.csv
├── notebooks/
│   ├── 01_Fase1_Comprension_y_EDA.ipynb
│   ├── 02_Fase2_Analisis_Inferencial.ipynb
│   └── 03_Fase3_Modelado_Predictivo.ipynb
├── src/
│   ├── entorno.py                # rutas del proyecto, semilla 42 y guardado de figuras (común a las 3 fases)
│   ├── fase2_utils.py            # V de Cramér, bootstrap por hogar, GVIF, Hosmer-Lemeshow, Mann-Whitney…
│   ├── features.py               # ingeniería de variables compartida por la Fase 3 y la inferencia
│   └── predict.py                # aplicación del modelo a datos nuevos por línea de comandos
├── output/
│   ├── fase1/                    # figuras (11) y HTML del cuaderno 01
│   ├── fase2/                    # tablas de contrastes y sensibilidad, figuras (6) y HTML
│   └── fase3/                    # tablas de resultados y validación, figuras, modelos .joblib y HTML
└── informe/
    └── Informe_Final_Grupo5.pdf
```

## 5. Tecnologías

Python 3.12 · Jupyter · pandas 2.2 · NumPy 2.2 · SciPy 1.15 · statsmodels 0.14 · scikit-learn 1.8 ·
matplotlib 3.10 · seaborn 0.13 · pyreadstat 1.3 (lectura de SPSS) · joblib (serialización del modelo).
Las versiones exactas están en [`requirements.txt`](requirements.txt). Metodología: CRISP-DM.

## 6. Instrucciones de ejecución

### Orden de ejecución

| Paso | Cuaderno | Entrada | Salida principal | Tiempo aprox. |
|---|---|---|---|---|
| 1 | `01_Fase1_Comprension_y_EDA` | `data/raw/*.SAV` | `data/processed/dataset_limpio.csv`, `output/fase1/` | < 1 min |
| 2 | `02_Fase2_Analisis_Inferencial` | `data/processed/dataset_limpio.csv` | `output/fase2/` | 3 min |
| 3 | `03_Fase3_Modelado_Predictivo` | `data/processed/dataset_limpio.csv` | `output/fase3/` (incluye modelos) | 2 min |

El dataset limpio está versionado en el repositorio, de modo que los cuadernos 02 y 03 pueden
ejecutarse sin correr antes el 01. Cada cuaderno se ejecuta de arriba hacia abajo sin intervención
manual y empieza con una **celda 0** que prepara el entorno.

### Opción A · Google Colab (sin instalar nada)

1. Abrir un cuaderno con el botón **Abrir en Colab** de la tabla inicial.
2. Menú *Entorno de ejecución → Ejecutar todas*.
   La celda 0 clona este repositorio en `/content/informalidad-laboral-juvenil` y trabaja con las
   mismas rutas que en local; en la Fase 1 instala además `pyreadstat`.
3. Para usar exactamente las versiones de `requirements.txt`, poner `VERSIONES_EXACTAS = True` en la
   celda 0, ejecutarla, reiniciar la sesión y volver a ejecutar todo. Con las versiones que trae Colab
   por defecto pueden aparecer diferencias mínimas en los decimales de la Fase 3.

### Opción B · Local

```bash
git clone https://github.com/rlop026/informalidad-laboral-juvenil.git
cd informalidad-laboral-juvenil
python -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python ejecutar_todo.py              # ejecuta 01 → 02 → 03 y exporta cada HTML a output/faseN/
# o solo algunas fases:  python ejecutar_todo.py 2 3
```

También pueden abrirse los cuadernos con `jupyter lab` (desde la raíz o desde `notebooks/`) y
ejecutarse con *Run All*. Exportar un cuaderno a HTML manualmente:
`jupyter nbconvert --to html notebooks/02_Fase2_Analisis_Inferencial.ipynb --output-dir output/fase2`.

### Aplicar el modelo a datos nuevos

```bash
python src/predict.py --modelo output/fase3/modelos/modelo_informalidad.joblib \
                      --entrada nuevos.csv --salida predicciones.csv
```

El CSV de entrada debe tener las columnas del dataset limpio (`tam_empresa`, `ocupacion`,
`educ_nivel`, `educ_anios`, `edad`, `mujer`, `rural`, `entorno_informal`, `clima_educativo`, `rama`,
`horas`, `antiguedad`, `departamento`). La salida trae la probabilidad y la clase predicha con el
umbral fijado en validación.

### Reproducibilidad

- **Semilla única 42** (`src/entorno.py`), usada en NumPy, bootstrap, particiones y modelos.
- **Rutas relativas** a la raíz del repositorio: el mismo código funciona en local y en Colab.
- **Una sola fuente de funciones** (`src/`), compartida por cuadernos y script de inferencia.
- **Auditorías por código**: las Fases 2 y 3 verifican filas, hogares y tasa de informalidad del
  dataset antes de analizar y se detienen si no coinciden.
- **Verificado:** al ejecutar `01` desde los `.SAV` originales se obtiene un `dataset_limpio.csv`
  idéntico byte a byte al entregado en la Fase 1, y los tres cuadernos corren de principio a fin sin
  errores con el entorno de `requirements.txt` (Python 3.12.3), reproduciendo exactamente las 40 pruebas de la Fase 2 y las métricas de la Fase 3 entregadas.
- **Sin fuga de información:** el preprocesamiento vive dentro de un `Pipeline` ajustado solo con
  entrenamiento; partición cronológica y por hogar; el conjunto de prueba se usa una sola vez.

## 7. Síntesis de resultados

### Fase 1 · Exploración

- Embudo de limpieza: 140.128 registros → 55.857 con condición laboral definida → 15.023 de 18 a 29
  años → 12.698 sin repeticiones del panel → **12.691** con años de estudio informados.
- Tasa de informalidad **ponderada de 68,1 %** (71,2 % sin ponderar), estable entre trimestres
  (66,4 % a 71,3 %, sin tendencia).
- Mayor asociación bivariada: **tamaño del establecimiento** (V de Cramér = 0,520), seguido por
  ocupación (0,339), educación (0,273), departamento (0,236) y entorno informal del hogar (0,234).
  La informalidad va de 88,1 % en establecimientos de 2 a 5 personas a 18,5 % en los de más de 500.

### Fase 2 · Inferencia (α = 0,05, corrección de Holm)

| Hipótesis | Prueba | Resultado | Tamaño del efecto |
|---|---|---|---|
| H1 · tamaño del establecimiento | Chi-cuadrado | Se rechaza H0 (p < 0,001) | V = 0,501 [0,484; 0,519] |
| H2 · educación ajustada | Logística, Wald conjunto | Se rechaza H0 (p = 2,4×10⁻⁴⁷) | OR primaria inc. vs superior = 9,39; −6 a −7 pp cada 3 años de estudio |
| H3 · entorno informal del hogar | Logística anidada | Se rechaza H0 (p = 3,8×10⁻²⁶) | OR todos vs ninguno = 2,24, pero ΔAUC = 0,005 |
| H4 · ingresos menores en informales | U de Mann-Whitney | Se rechaza H0 (p < 0,001) | −33 % mensual, −28 % por hora (medianas) |
| H5 · sexo: OR ajustado ≠ bruto | Bootstrap de hogares | No se rechaza H0 (p = 0,168) | OR ajustado 1,23 vs bruto 1,17 |

### Fase 3 · Modelado predictivo (prueba en 2026, n = 2.159)

| Modelo | AUC | Exactitud balanceada | Precisión | Exhaustividad | F1 |
|---|---|---|---|---|---|
| Línea base: clase mayoritaria | 0,500 | 0,500 | 0,704 | 1,000 | 0,827 |
| Línea base: regla de tamaño | 0,687 | 0,687 | 0,868 | 0,587 | 0,700 |
| **HistGradientBoosting · conjunto A (principal)** | **0,896** | **0,814** | **0,935** | **0,752** | **0,834** |
| HistGradientBoosting · B (sin tamaño) | 0,858 | 0,772 | 0,926 | 0,671 | 0,778 |
| HistGradientBoosting · C (sin tamaño ni hogar) | 0,855 | 0,777 | 0,898 | 0,760 | 0,823 |

- El tamaño del establecimiento domina la predicción (caída de AUC ≈ 0,14 al permutarlo); quitar
  además el hogar solo cuesta 0,003 de AUC, en línea con H3.
- El error principal son los falsos negativos (informales con rasgos de empleo formal: empresas de
  6 a 50 personas, ocupaciones calificadas, educación superior). El modelo detecta al 85 % de los
  informales rurales y al 70 % de los urbanos.

### Conclusión

La informalidad juvenil no se explica por un único factor: **puesto de trabajo > educación >
entorno del hogar > sexo y área**, un orden que se mantiene tanto en la inferencia como en la
predicción fuera de la muestra. La capacitación es necesaria pero insuficiente; el modelo sirve para
estimaciones agregadas, no para decisiones sobre personas.

**Limitaciones:** asociaciones transversales (no causales); posible circularidad entre el tamaño del
establecimiento y la definición oficial de informalidad; sin estratos ni UPM para inferencia basada
en el diseño; calibración imperfecta en probabilidades intermedias; una sola ventana de prueba; se
excluye el sector agropecuario.

## 8. Uso de inteligencia artificial

Conforme al reglamento de la cátedra, se utilizó un asistente de IA (Claude, de Anthropic) como apoyo
en la redacción de código, figuras y textos. Las decisiones metodológicas y la interpretación de los
resultados son del grupo, que revisó y comprende todo el contenido del repositorio.
