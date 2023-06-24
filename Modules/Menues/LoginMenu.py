from Modules.Login import login, registro

from Modules.Utils.Utils import limpiar_terminal

def LoginMenu(debug):
    resp = debug
    while True and not resp:
        print("1. Registro")
        print("2. Inicio de sesión")
        print("3. Salir\n")
        opcion = input("Seleccione una opción: ")
        limpiar_terminal(0.4)
        
        if opcion == "1":
            registro()
        elif opcion == "2":
            resp = login()
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")

    return resp
