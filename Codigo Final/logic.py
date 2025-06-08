import pandas as pd
import io

DATAFRAME = None

def cargar_csv(ruta):
    global DATAFRAME
    DATAFRAME = pd.read_csv(ruta)
    return f"✅ Archivo cargado con éxito. Filas: {DATAFRAME.shape[0]}, Columnas: {DATAFRAME.shape[1]}"

def mostrar_head(n=5):
    return DATAFRAME.head(n).to_html() if DATAFRAME is not None else "❌ No hay datos cargados."

def mostrar_tail(n=5):
    return DATAFRAME.tail(n).to_html() if DATAFRAME is not None else "❌ No hay datos cargados."

def info_basica():
    if DATAFRAME is not None:
        buffer = io.StringIO()
        DATAFRAME.info(buf=buffer)
        return buffer.getvalue().replace('\n', '<br>')
    return "❌ No hay datos cargados."

def lista_columnas():
    return ", ".join(DATAFRAME.columns) if DATAFRAME is not None else "❌ No hay datos cargados."

def forma_dataset():
    return str(DATAFRAME.shape) if DATAFRAME is not None else "❌ No hay datos cargados."

def descripcion_dataset():
    return DATAFRAME.describe().to_html() if DATAFRAME is not None else "❌ No hay datos cargados."

def seleccionar_columna(columna):
    if DATAFRAME is not None and columna in DATAFRAME.columns:
        return DATAFRAME[[columna]].to_html()
    return f"❌ Columna '{columna}' no encontrada."

def seleccionar_columnas(columnas):
    if DATAFRAME is not None:
        columnas_lista = [col.strip() for col in columnas.split(',')]
        columnas_validas = [col for col in columnas_lista if col in DATAFRAME.columns]
        if columnas_validas:
            return DATAFRAME[columnas_validas].to_html()
        return "❌ Ninguna columna válida encontrada."
    return "❌ No hay datos cargados."

def filtrar_filas(condicion):
    if DATAFRAME is not None:
        try:
            filtrado = DATAFRAME.query(condicion)
            return filtrado.to_html()
        except Exception as e:
            return f"❌ Error en la condición: {str(e)}"
    return "❌ No hay datos cargados."
