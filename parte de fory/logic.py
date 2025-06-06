import pandas as pd

DATAFRAME = None

def cargar_csv(ruta):
    global DATAFRAME
    DATAFRAME = pd.read_csv(ruta)
    return f"Archivo cargado con éxito. Filas: {DATAFRAME.shape[0]}"

def mostrar_head(n=5):
    return DATAFRAME.head(n).to_html() if DATAFRAME is not None else "No hay datos cargados"

def mostrar_tail(n=5):
    return DATAFRAME.tail(n).to_html() if DATAFRAME is not None else "No hay datos cargados"

import io

def info_basica():
    if DATAFRAME is not None:
        buffer = io.StringIO()
        DATAFRAME.info(buf=buffer)
        return buffer.getvalue().replace('\n', '<br>')
    return "No hay datos cargados"


def lista_columnas():
    return ", ".join(DATAFRAME.columns) if DATAFRAME is not None else "No hay datos cargados"

def forma_dataset():
    return str(DATAFRAME.shape) if DATAFRAME is not None else "No hay datos cargados"
