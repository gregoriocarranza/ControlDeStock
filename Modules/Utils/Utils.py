import os
import time
import csv


def limpiar_terminal(t):
    time.sleep(t)
    os.system("cls")

def pausa():
    input("Presione Enter para continuar...")
    limpiar_terminal(0.1)

def initCsv(archivo_csv):
    try:
        with open(archivo_csv, "r") as archivo:
            print("El archivo CSV existe.")
    except FileNotFoundError:
        with open(archivo_csv, "w", newline="") as archivo:
            archivo.write("")
        print("Se ha creado un nuevo archivo CSV vacío.")


def Rescate_de_variables(codigos, nombres, precios, stocks):
    with open("./Archivos/Productos.csv", "r") as archivo_productos:
        archivo_productos.seek(0)
        contenido_reg = archivo_productos.readline().strip()
        while contenido_reg:
            codigo, nombre, precio, stock = contenido_reg.split(";")

            codigos.append(codigo)
            nombres.append(nombre)
            precios.append(int(precio))
            stocks.append(int(stock))
            contenido_reg = archivo_productos.readline().strip()

    return codigos, nombres, precios, stocks
