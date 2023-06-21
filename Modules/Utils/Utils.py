import os
import time
import csv
proveedores_autorizados = ('gmail.com', 'hotmail.com', 'outlook.com')
archivoDeUsuarios="./archivos/Usuarios.csv"
archivoDeProductos="./archivos/Productos.csv"

def limpiar_terminal(t):
    time.sleep(t)
    os.system("cls")



def initCsv(archivo_csv):
    try:
        with open(archivo_csv, 'r') as archivo:
            # Puedes realizar alguna operación aquí si el archivo existe
            print("El archivo CSV existe.")
    except FileNotFoundError:
        # Si el archivo no existe, se crea uno nuevo vacío
        with open(archivo_csv, 'w', newline='') as archivo:
            # Escribe una línea vacía para asegurar que el archivo esté creado
            archivo.write('')
        print("Se ha creado un nuevo archivo CSV vacío.")

