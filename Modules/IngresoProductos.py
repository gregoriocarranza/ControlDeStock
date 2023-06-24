from Modules.Validaciones import (
    validar_codigo,
    validar_nombre_producto,
    validar_precio_stock,
)
from Modules.Utils.Utils import Rescate_de_variables


def ingresoDeProductos():
    codigos = []
    nombres = []
    precios = []
    stocks = []
    
    codigos, nombres, precios, stocks = Rescate_de_variables(codigos, nombres, precios, stocks)
    resp,codigo = validar_codigo(input("Ingrese el código del producto o EXIT para salir: ").upper(),codigos)

    while resp and codigo!="EXIT":
        resp,codigo = validar_codigo(input("El código ingresado no es válido. Ingrese nuevamente: ").upper(),codigos)
        
    while codigo != "EXIT":

        
        with open("./Archivos/Productos.csv", "a") as archivo_productos:
            nombre = validar_nombre_producto("Ingrese el nombre del producto: ","El nombre ingresado no es valido. Intente nuevamente: ")
            
            precio = validar_precio_stock("Ingrese el precio unitario del producto: ","El precio ingresado no es válido. Intente nuevamente: ")
            stock = validar_precio_stock("Ingrese la cantidad inicial de stock del producto: ","La cantidad ingresada no es válida. Intente nuevamente:")

            print(f"{codigo};{nombre};{precio};{stock}\n")
            archivo_productos.write(f"{codigo};{nombre};{precio};{stock}\n")
            print("Ingreso de producto exitoso!")

            resp,codigo = validar_codigo(input("Ingrese el código del producto o EXIT para salir: ").upper(),codigos)

            while resp and codigo!="EXIT":
                resp,codigo = validar_codigo(input("El código ingresado no es válido. Ingrese nuevamente: ").upper(),codigos)
    return True
