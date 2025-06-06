from flask import Flask, render_template, request, redirect
import os
from models import init_db, guardar_archivo
import logic

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

init_db()

@app.route('/')
def index():
    return render_template('index.html', resultado="")

@app.route('/cargar_csv', methods=['POST'])
def cargar_csv():
    archivo = request.files['archivo']
    if archivo:
        ruta = os.path.join(app.config['UPLOAD_FOLDER'], archivo.filename)
        archivo.save(ruta)
        guardar_archivo(archivo.filename)
        resultado = logic.cargar_csv(ruta)
        return render_template('index.html', resultado=resultado)
    return redirect('/')

@app.route('/head')
def head():
    return render_template('index.html', resultado=logic.mostrar_head(5))

@app.route('/tail')
def tail():
    return render_template('index.html', resultado=logic.mostrar_tail(5))

@app.route('/info')
def info():
    return render_template('index.html', resultado=logic.info_basica())

@app.route('/columnas')
def columnas():
    return render_template('index.html', resultado=logic.lista_columnas())

@app.route('/forma')
def forma():
    return render_template('index.html', resultado=logic.forma_dataset())

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.mkdir('uploads')
    app.run(debug=True)
