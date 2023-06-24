from Modules.Validaciones import (
    validar_codigo,
    validar_stock_disponible,
    validar_caracteres_especiales,
    busq_indice,
)
from Modules.Utils.Utils import Rescate_de_variables,ordenar_por_vendido,pausa

import csv
from pprint import pprint

def ventas():
    with open("./Archivos/Ventas.csv", "a") as archivo_ventas:
        ventas = []
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
            vendido = validar_stock_disponible(stocks[productoIndice],"Ingrese cantidad vendida del producto: ","La cantidad ingresada no es válida. Intente nuevamente: ")
            usuario = validar_caracteres_especiales("Ingrese el nombre del vendedor: ","El nombre no puede contener caracteres especiales, Ingrese otro para continuar : ")
            
            ventas.append({"codigo": f"{codigos[productoIndice]}","producto": f"{nombres[productoIndice]}","cantidad": f"{vendido}","vendedor": f"{usuario}"})

            archivo_ventas.write(f"{codigos[productoIndice]};{nombres[productoIndice]};{vendido};{usuario}\n")
            
            print("Venta de producto exitoso!")
            stocks[productoIndice]-=int(vendido)
            
            with open("./Archivos/productos.csv", "w", newline="") as archivo_productos:
                for index, produc in enumerate(codigos):
                    archivo_productos.write(f"{codigos[index]};{nombres[index]};{precios[index]};{int(stocks[index])}\n")
                    
            codigo = input("Ingrese el código del producto o EXIT para salir: ").upper()
    
            while not validar_codigo(codigo,codigos) and codigo!="EXIT":
                    codigo = input("El código ingresado no es válido. Ingrese nuevamente: ").upper()
        
        # ventas_ordenadas=ordenar_por_vendido(ventas)
        # print(ventas_ordenadas,"\n")
        # pausa()




