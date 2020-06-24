# Declaración de import.
import sqlite3
import datetime
print(datetime.datetime.now())  # Local version of date and time

# Crear base de datos y tabla si es que no existen, funciones connect y cursor.
connected_database = sqlite3.connect('sales_database.db')
cursor_obj = connected_database.cursor()

cursor_obj.execute('CREATE TABLE IF NOT EXISTS sales_table \
                   (id INTEGER PRIMARY KEY AUTOINCREMENT, \
                   date TEXT, \
                   time TEXT, \
                   description TEXT, \
                   quantity INTEGER, \
                   price INTEGER)')

# Abrir el .txt, extraer y formatear el contenido, cargarlo a la base de datos.
file = open(("sales_"+str(datetime.datetime.now().date()))+".txt", "r")
for index, line in enumerate(file):
    x = line.replace(',', '')
    x = x.split()
    print(x)
    cursor_obj.execute(
        'INSERT INTO sales_table(date, time, description, quantity, price) VALUES(?, ?, ?, ?, ?)', x)
connected_database.commit()
file.close()
connected_database.close()
