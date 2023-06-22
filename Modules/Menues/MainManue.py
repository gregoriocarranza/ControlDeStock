from Modules.IngresoProductos import ingresoDeProductos
# from ControlDeStock import controlDeStock
# from Informes import informes
# from Ventas import ventas




def MainManue():
    resp=True
    while True and resp:
        print("1. Ingreso de productos")
        print("2. Actualizar de stock")
        print("3. Informes")
        print("4. Salir\n")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ingresoDeProductos()
        elif opcion == "2":
            # controlDeStock()
            print("Control de stock")
        elif opcion == "3":
            # ventas()
            print("Ventas")
        elif opcion == "4":
            # informes()
            print("Informes")            
        elif opcion == "5":
            resp=False
        else:
            print("Opción inválida.")
    return resp