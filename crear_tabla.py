import sqlite3

DATABASE = 'reservations.sql'

def remove_duplicates():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    # Obtener todas las filas de la tabla lugares
    c.execute('SELECT id, nombre, descripcion FROM lugares')
    rows = c.fetchall()

    # Crear un diccionario para almacenar los nombres únicos
    unique_lugares = {}
    
    # Iterar sobre las filas y mantener solo la primera aparición de cada nombre
    for row in rows:
        id, nombre, descripcion = row
        if nombre not in unique_lugares:
            unique_lugares[nombre] = (id, descripcion)
        else:
            # Eliminar duplicados
            c.execute('DELETE FROM lugares WHERE id = ?', (id,))

    conn.commit()
    conn.close()

def add_area_cometas():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    
    # Agregar 'Area de cometas'
    c.execute('INSERT INTO lugares (nombre, descripcion) VALUES (?, ?)', ('Sala de ESports', 'Pa jugar el Valo, pa'))
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
  
    add_area_cometas()
    print("Duplicados eliminados y 'Area de cometas' añadido.")
