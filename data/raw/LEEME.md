# Datos crudos — EPHC del INE (base REG02)

Esta carpeta contiene los **diez archivos SPSS (`.SAV`) de la base de personas (REG02)** de la
Encuesta Permanente de Hogares Continua (EPHC) trimestral, publicados por el Instituto Nacional de
Estadística (INE) del Paraguay: del 1.er trimestre de 2024 al 2.º trimestre de 2026, factor de
expansión revisión 2025. Son la única entrada del cuaderno `notebooks/01_Fase1_Comprension_y_EDA.ipynb`.

| Archivo | Trimestre | Registros |
|---|---|---|
| `fb5f7-REG02_EPHC_1er_Trim_2024.SAV` | 2024-T1 | 13.928 |
| `b2b14-REG02_EPHC_2º Trim 2024.SAV` | 2024-T2 | 14.081 |
| `44269-REG02_EPHC_3er Trim 2024.SAV` | 2024-T3 | 13.353 |
| `c8ccc-REG02_EPHC_4º Trim 2024.SAV` | 2024-T4 | 16.382 |
| `54802-REG02_EPHC_1er Trim 2025.SAV` | 2025-T1 | 13.246 |
| `f7b48-REG02_EPHC_2º Trim 2025.SAV` | 2025-T2 | 13.597 |
| `6bf65-REG02_EPHC_3er Trim 2025.SAV` | 2025-T3 | 13.536 |
| `75003-REG02_EPHC_4º Trim 2025.SAV` | 2025-T4 | 15.555 |
| `84f1f-REG02_EPHC_1er Trim 2026.SAV` | 2026-T1 | 13.059 |
| `d6b15-REG02_EPHC_2º Trim 2026.SAV` | 2026-T2 | 13.391 |
| **Total** | 10 trimestres | **140.128** |

## Origen y licencia

- Portal de microdatos del INE: <https://www.ine.gov.py/microdatos/> (descarga del 7 de septiembre de 2026).
- Son microdatos **públicos y anonimizados** (no contienen nombres, documentos ni direcciones),
  difundidos bajo la Ley 5282/2014 de libre acceso ciudadano a la información pública.

## Si la carpeta está vacía

1. Ingresar al portal de microdatos del INE → *Encuesta Permanente de Hogares Continua* → trimestral.
2. Descargar, para cada trimestre de 2024-T1 a 2026-T2, la base **REG02 (personas)** en formato SPSS (`.SAV`).
3. Copiar los diez archivos en esta carpeta sin renombrarlos (el cuaderno busca el patrón `*REG02*.SAV`).

Los cuadernos de las Fases 2 y 3 no necesitan estos archivos: parten de
`data/processed/dataset_limpio.csv`, que el cuaderno 01 regenera de forma idéntica.
