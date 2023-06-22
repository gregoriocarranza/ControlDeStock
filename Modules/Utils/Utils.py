import os
import time
import csv

def limpiar_terminal(t):
    time.sleep(t)
    os.system("cls")



def initCsv(archivo_csv):
    try:
        with open(archivo_csv, 'r') as archivo:
            print("El archivo CSV existe.")
    except FileNotFoundError:
        with open(archivo_csv, 'w', newline='') as archivo:
            archivo.write('')
        print("Se ha creado un nuevo archivo CSV vacío.")

