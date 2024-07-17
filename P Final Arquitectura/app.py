import sqlite3
import os
from flask import Flask, request, redirect, url_for, render_template, flash
from controllers.controller_shurima import ControllerShurima
from API_Fechas.fechas_api import fechas_api

app = Flask(__name__)
app.secret_key = 'your_secret_key'
controller = ControllerShurima()

DATABASE = 'reservations.sql'

def get_db_connection():
    if not os.path.exists(DATABASE):
        print(f"Database file {DATABASE} does not exist!")
    else:
        print(f"Database file {DATABASE} found.")
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Esto permitirá obtener filas como diccionarios
    return conn

# Ruta para la página principal
@app.route('/')
def index():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM reservations')
    reservations = c.fetchall()
    conn.close()
    reservations = [dict(row) for row in reservations]  # Convertir a lista de diccionarios
    print(f"Reservations fetched: {reservations}")
    return render_template('index.html', reservations=reservations)

# Ruta para manejar la reserva
@app.route('/reserve', methods=['POST'])
def reserve():
    name = request.form['name']
    date = request.form['date']
    time = request.form['time']
    type = request.form['type']

    conn = get_db_connection()
    c = conn.cursor()

    # Verificar si ya existe una reserva para la misma fecha y hora
    c.execute('SELECT * FROM reservations WHERE date = ? AND time = ? AND type = ?', (date, time, type))
    existing_reservation = c.fetchone()

    if existing_reservation:
        flash('La reserva ya existe para la fecha y hora especificadas.')
    else:
        c.execute('INSERT INTO reservations (name, date, time, type) VALUES (?, ?, ?, ?)',
                  (name, date, time, type))
        conn.commit()
        flash('Reserva realizada con éxito.')

    conn.close()
    return redirect(url_for('index'))

# Nueva ruta para verificar disponibilidad
@app.route('/check_availability', methods=['GET'])
def check_availability():
    date = request.args.get('date')
    time = request.args.get('time')
    type = request.args.get('type')

    print(f"Checking availability for date: {date}, time: {time}, type: {type}")

    conn = get_db_connection()
    c = conn.cursor()

    # Verificar qué se está almacenando y comparando
    query = 'SELECT * FROM reservations WHERE date = ? AND time = ? AND type = ?'
    print(f"Executing query: {query} with values ({date}, {time}, {type})")
    c.execute(query, (date, time, type))
    reservation = c.fetchone()

    # Depuración adicional
    print(f"Reservation found: {reservation}")

    conn.close()

    if reservation:
        return {"available": False}
    else:
        return {"available": True}

# Registrar la Blueprint
app.register_blueprint(fechas_api)

if __name__ == '__main__':
    app.run(debug=True)
