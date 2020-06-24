# Declaración de import (1)
from items_and_prices import items
import sqlite3
import datetime
print(datetime.datetime.now())  # Local version of date and time

# Conectar a base de datos
connected_database = sqlite3.connect('sales_database.db')
cursor_obj = connected_database.cursor()


# Declaración de funciones (2)
def ventas_total():
    # Ventas totales en dinero
    cursor_obj.execute('SELECT SUM(price) FROM sales_table')
    sum_sales = cursor_obj.fetchone()
    print("Ventas totales en dinero: $" + str(sum_sales[0]))

    # Unidades vendidas
    n = 1
    for item in items:
        cursor_obj.execute('SELECT SUM(quantity), SUM(price) \
        FROM sales_table WHERE description = "{i}"'.format(i=item))

        units_sold = cursor_obj.fetchone()
        print(str(n) + ".", item, "-", units_sold[0], "unidades vendidas ($" + str(units_sold[1]) + ")")
        n = n + 1

    connected_database.close()


def ventas_tiempo_exacto():
    print("Puede ingresar: año (ej: 2020) / año y mes (ej: 2020-01) / año, mes y día (ej: 2020-01-25)")
    fecha = str(input(">"))

    # Ventasen dinero por tiempo
    cursor_obj.execute('SELECT SUM(price) FROM sales_table WHERE date LIKE "{f}%"'.format(f=fecha))
    sum_sales = cursor_obj.fetchone()
    print("Ventas en dinero: $" + str(sum_sales[0]))

    # Unidades vendidas por tiempo
    n = 1
    for item in items:
        cursor_obj.execute('SELECT SUM(quantity), SUM(price) FROM sales_table \
                           WHERE description = "{i}" AND date LIKE "{f}%"'.format(i=item, f=fecha))

        units_sold = cursor_obj.fetchone()
        print(str(n) + ".", item, "-", units_sold[0], "unidades vendidas ($" + str(units_sold[1]) + ")")
        n = n + 1

    connected_database.close()


# Inicio del programa principal(3)
def main():
    print("Puede ingresar: '1' para ver las ventas totales / '2' para ver las ventas por tiempo")
    opcion = 0
    while opcion not in range(1, 3):
        try:
            opcion = int(input(">"))
        except ValueError:
            "ValueError"
    print("")
    if opcion == 1:
        ventas_total()
    elif opcion == 2:
        ventas_tiempo_exacto()


main()  # \

print("")
input("Presione ENTER para finalizar.")
