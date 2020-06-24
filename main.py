# Declaración de import (1)
from items_and_prices import items, prices

import datetime
print(datetime.datetime.now())  # Local version of date and time


# Declaración de funciones (2)
def save_transaction(description, quantity, price):
    file = open("sales.txt", "a")
    file.write(str(datetime.datetime.now())
               + ", {d}, {q}, {p}".format(d=description, q=quantity, p=(price * quantity))
               + "\n")
    file.close()


def cerrar_día():
    file1 = open("sales.txt", "r")
    file2 = open(("sales_"+str(datetime.datetime.now().date()))+".txt", "w")
    print("Ventas del día", str(datetime.datetime.now().date())+":")
    for index, line in enumerate(file1):
        if (str(datetime.datetime.now().date())) in line:
            print(line)
            file2.write(line)
    file1.close()
    file2.close()


# Inicio del programa principal(3)
def main():
    running = True
    while running:
        print("")
        n = 1
        for item in items:
            print(str(n) + ".", item, "- $" + str(prices[n-1]))
            n = n + 1
        print(str(n) + ". Quit")
        print(str(n + 1) + ". Cerrar dia")
        print(str(n + 2) + ". Lista de precios")

        # Exception handling
        item = 0
        while item not in range(1, n+3):
            try:
                item = int(input("Elija opcion: >"))
            except ValueError:
                "ValueError"

        if item == n:
            running = False

        elif item == n+1:
            cerrar_día()
            running = False

        elif item == n+2:
            s = 1
            print("Lista de precios:")
            for i in items:
                print(str(s) + ".", i, "- $" + str(prices[s-1]))
                s += 1

        elif item < n:
            # Exception handling
            quantity = 0
            while quantity <= 0:
                try:
                    quantity = int(input(items[item - 1] + " cantidad? >"))
                except ValueError:
                    "ValueError"
            save_transaction(items[item - 1], quantity, prices[item - 1])


main()
