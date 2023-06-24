from Modules.Validaciones import (
    validar_codigo,
    validar_numero_positivo,
    busq_indice,
)
from Modules.Utils.Utils import Rescate_de_variables

import csv


def controlDeStock():
    codigos = []
    nombres = []
    precios = []
    stocks = []
    codigos, nombres, precios, stocks = Rescate_de_variables(codigos, nombres, precios, stocks)

    codigo = input("Ingrese el código del producto o EXIT para salir: ").upper()
    while not validar_codigo(codigo,codigos) and codigo!="EXIT":
        codigo = input("El código ingresado no es válido. Ingrese nuevamente: ").upper()
    
    while codigo!="EXIT":
        productoIndice = busq_indice(codigo, codigos)
        stock_a_agregar = input("Ingresar un stock a agregar: ")
        
        while not validar_numero_positivo(stock_a_agregar):
            stock_a_agregar = input("Error: debe ser positivo y entero: ")
        print("Ingreso de stock exitoso!")
        stocks[productoIndice]+=int(stock_a_agregar)
        
        with open("./Archivos/productos.csv", "w", newline="") as archivo_productos:
            for index, produc in enumerate(codigos):
                archivo_productos.write(f"{codigos[index]};{nombres[index]};{precios[index]};{int(stocks[index])}\n")
        
        codigo = input("Ingrese el código del producto o EXIT para salir: ").upper()
        
        while not validar_codigo(codigo,codigos) and codigo!="EXIT":
            codigo = input("El código ingresado no es válido. Ingrese nuevamente: ").upper()




