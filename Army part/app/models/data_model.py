import sqlite3
import os

DB_PATH = os.path.join('database', 'datos.db')

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS archivos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                ruta TEXT NOT NULL
            )
        ''')
        conn.commit()

def insertar_archivo(nombre, ruta):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO archivos (nombre, ruta) VALUES (?, ?)', (nombre, ruta))
        conn.commit()

def obtener_archivos():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM archivos')
        return cursor.fetchall()
