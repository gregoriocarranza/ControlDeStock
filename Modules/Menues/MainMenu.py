from Modules.IngresoProductos import ingresoDeProductos
from Modules.Ventas import ventas
# from ControlDeStock import controlDeStock
from Modules.Informes import generarInformes

from Modules.Utils.Utils import limpiar_terminal

def MainMenu():
    resp = True
    while True and resp:
        print("1. Ingreso de productos")
        print("2. Actualizar de stock")
        print("3. Ventas")
        print("4. Informes")
        print("5. Salir\n")
        opcion = input("Seleccione una opción: ")
        limpiar_terminal(1)

        if opcion == "1":
            ingresoDeProductos()
        elif opcion == "2":
            # controlDeStock()
            print("Control de stock")
        elif opcion == "3":
            ventas()
        elif opcion == "4":
            generarInformes()
        elif opcion == "5":
            resp = False
        else:
            print("Opción inválida.")
    return resp
