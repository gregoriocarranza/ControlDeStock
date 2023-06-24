import csv

from Modules.Validaciones import (
    validar_caracteres_especiales,
    validar_email,
    validar_contrasena,
    validar_rango,
)
from Modules.Utils.Utils import limpiar_terminal


def registro():
    with open("./Archivos/Usuarios.csv", "a") as archivo_de_usuarios:
        usuario = validar_caracteres_especiales("Ingrese su nombre de usuario: ","El nombre de usuario no puede contener caracteres especiales, Ingrese otro para continuar : ")
        email = validar_email("Ingrese su correo electrónico: ","El correo electrónico no tiene la estructura correspondiente o no es de un proveedor autorizado: ",True)
        contraseña = validar_contrasena("Ingrese su contraseña: ","La contraseña debe tener una longitud de 5 caracteres : ","La contraseña debe ser alfanumérica: ")
        edad = validar_rango("Ingrese su edad: ", "La edad debe ser mayor de 18 y menor a 96: ", 18, 96)

        archivo_de_usuarios.write(f"{usuario};{email};{contraseña};{edad}\n")

        print("Registro exitoso.\n")
        return True


def login():
    existe = False
    passw = False
    email = validar_email("Ingrese su correo electrónico: ","El correo electrónico no tiene la estructura correspondiente o no es de un proveedor autorizado: ",False)
    contrasena = validar_contrasena("Ingrese su contraseña: ","La contraseña debe tener una longitud de 5 caracteres : ","La contraseña debe ser alfanumérica: ")

    with open("./Archivos/Usuarios.csv", "r") as archivo_de_usuarios:
        archivo_de_usuarios.seek(0)
        contenido_reg = archivo_de_usuarios.readline().strip()
        while contenido_reg:
            Username, Email, Password, edad = contenido_reg.split(";")
            if email == Email:
                existe = True
                if contrasena == Password:
                    passw = True
            contenido_reg = archivo_de_usuarios.readline().strip()

        print("")
        if not existe:
            print("El Correo electronico que esta queriendo ingresar no esta en nuestra base de datos, registrese")
        elif not passw:
            print("Contraseña incorrecta, intentelo nuevamnete.")
        else:
            print("Ingreso exitoso!")
            return True

    limpiar_terminal(1)
