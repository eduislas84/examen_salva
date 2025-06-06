from flask import Blueprint, render_template, request, redirect, url_for
import pandas as pd
import os

from models import data_model  # Importamos el modelo

main = Blueprint('main', __name__)
df = pd.DataFrame()  # Variable global temporal para almacenar el dataset

# Inicializar la base de datos SQLite
data_model.init_db()

@main.route('/')
def index():
    return render_template('index.html')

# 1.1 - Cargar archivo CSV
@main.route('/cargar_csv', methods=['POST'])
def cargar_csv():
    global df
    archivo = request.files['archivo']
    if archivo.filename.endswith('.csv'):
        ruta = os.path.join('uploads', archivo.filename)
        archivo.save(ruta)
        df = pd.read_csv(ruta)

        # Guardar información del archivo en la base de datos
        data_model.insertar_archivo(archivo.filename, ruta)
    return redirect(url_for('main.index'))

# 2.6 - Descripción del dataset
@main.route('/descripcion')
def descripcion():
    global df
    if df.empty:
        return render_template('resultados.html', resultado="<p>No hay datos cargados.</p>")
    descripcion = df.describe().to_html()
    return render_template('resultados.html', resultado=descripcion)

# 3.1 - Seleccionar una columna
@main.route('/seleccionar_una_columna', methods=['GET', 'POST'])
def seleccionar_una_columna():
    global df
    columnas = df.columns.tolist()
    if request.method == 'POST':
        seleccionada = request.form.get('columna')
        resultado = df[seleccionada].to_frame().to_html()
        return render_template('resultados.html', resultado=resultado)
    return render_template('seleccionar_una.html', columnas=columnas)

# 3.2 - Seleccionar varias columnas
@main.route('/seleccionar_varias_columnas', methods=['GET', 'POST'])
def seleccionar_varias_columnas():
    global df
    columnas = df.columns.tolist()
    if request.method == 'POST':
        seleccionadas = request.form.getlist('columnas')
        resultado = df[seleccionadas].to_html()
        return render_template('resultados.html', resultado=resultado)
    return render_template('seleccionar_varias.html', columnas=columnas)

# 4.1 - Filtrar filas con condición
@main.route('/filtrar_filas', methods=['GET', 'POST'])
def filtrar_filas():
    global df
    columnas = df.select_dtypes(include=['number']).columns.tolist()  # Solo columnas numéricas
    operadores = ['>', '<', '==']

    if request.method == 'POST':
        columna = request.form.get('columna')
        operador = request.form.get('operador')
        valor = request.form.get('valor')

        try:
            valor = float(valor)
            if operador == '>':
                resultado = df[df[columna] > valor]
            elif operador == '<':
                resultado = df[df[columna] < valor]
            elif operador == '==':
                resultado = df[df[columna] == valor]
            else:
                resultado = pd.DataFrame()

            return render_template('resultados.html', resultado=resultado.to_html())
        except Exception as e:
            return render_template('resultados.html', resultado=f"<p>Error: {e}</p>")

    return render_template('filtrar_filas.html', columnas=columnas, operadores=operadores)
