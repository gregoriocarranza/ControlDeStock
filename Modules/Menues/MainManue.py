from IngresoDeProductos import ingresoDeProductos
from ControlDeStock import controlDeStock
from Informes import informes



def MainManue():
    while True:
        print("1. Ingreso de productos")
        print("2. Actualizar de stock")
        print("3. Informes")
        print("4. Salir\n")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ingresoDeProductos()
        elif opcion == "2":
            controlDeStock()
        elif opcion == "3":
            informes()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")