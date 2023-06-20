from Modules.Login import login,registro

def LoginMenu(archivo):
    resp=False
    while True and not resp:
        print("1. Registro")
        print("2. Inicio de sesión")
        print("3. Salir\n")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registro(archivo)
        elif opcion == "2":
            resp=login(archivo)
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")
            
    return resp