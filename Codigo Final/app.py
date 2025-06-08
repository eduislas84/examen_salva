from flask import Flask, render_template, request, redirect, url_for
import os
import logic

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cargar_csv', methods=['POST'])
def cargar_csv():
    archivo = request.files['archivo']
    if archivo:
        ruta = os.path.join(app.config['UPLOAD_FOLDER'], archivo.filename)
        archivo.save(ruta)
        resultado = logic.cargar_csv(ruta)
        return render_template('index.html', resultado=resultado, seccion='carga')
    return redirect(url_for('index'))

@app.route('/head', methods=['POST'])
def head():
    n = int(request.form['n'])
    resultado = logic.mostrar_head(n)
    return render_template('index.html', resultado=resultado, seccion='top')

@app.route('/tail', methods=['POST'])
def tail():
    n = int(request.form['n'])
    resultado = logic.mostrar_tail(n)
    return render_template('index.html', resultado=resultado, seccion='bottom')

@app.route('/info')
def info():
    return render_template('index.html', resultado=logic.info_basica(), seccion='info')

@app.route('/columnas')
def columnas():
    return render_template('index.html', resultado=logic.lista_columnas(), seccion='columnas')

@app.route('/forma')
def forma():
    return render_template('index.html', resultado=logic.forma_dataset(), seccion='forma')

@app.route('/descripcion')
def descripcion():
    return render_template('index.html', resultado=logic.descripcion_dataset(), seccion='descripcion')

@app.route('/columna', methods=['POST'])
def columna():
    col = request.form['columna']
    return render_template('index.html', resultado=logic.seleccionar_columna(col), seccion='unaCol')

@app.route('/columnas_n', methods=['POST'])
def columnas_n():
    cols = request.form['columnas']
    return render_template('index.html', resultado=logic.seleccionar_columnas(cols), seccion='variasCol')

@app.route('/filtrar', methods=['POST'])
def filtrar():
    condicion = request.form['condicion']
    return render_template('index.html', resultado=logic.filtrar_filas(condicion), seccion='filtro')

if __name__ == '__main__':
    app.run(debug=True)
