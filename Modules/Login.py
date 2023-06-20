import csv

from Modules.Validaciones import ValidarCaracteresEspeciales,validar_email,validar_contrasena
from Modules.Utils.Utils import limpiar_terminal


def registro(archivo):
    usuario = ValidarCaracteresEspeciales("Ingrese su nombre de usuario: ","El nombre de usuario no puede contener caracteres especiales, Ingrese otro para continuar : ")
    email = validar_email("Ingrese su correo electrónico: ","El correo electrónico no tiene la estructura correspondiente o no es de un proveedor autorizado: ",True)
    contraseña = validar_contrasena("Ingrese su contraseña: ","La contraseña debe tener una longitud de 8 caracteres : ","La contraseña debe ser alfanumérica: ")
    
    with open(archivo, 'a') as archivo_de_usuarios:
        archivo_de_usuarios.write(f"{usuario};{email};{contraseña}\n")
        

    print("Registro exitoso.\n")
    limpiar_terminal(2)


def login(archivo):
    existe=False
    passw=False
    email = validar_email("Ingrese su correo electrónico: ","El correo electrónico no tiene la estructura correspondiente o no es de un proveedor autorizado: ",False)
    contrasena = validar_contrasena("Ingrese su contraseña: ","La contraseña debe tener una longitud de 8 caracteres : ","La contraseña debe ser alfanumérica: ")

    with open(archivo, 'r') as archivo_de_usuarios:
        archivo_de_usuarios.seek(0)
        contenido_reg = archivo_de_usuarios.readline().strip()
        while contenido_reg:
            Username,Email,Password = contenido_reg.split(';')
            if email==Email:
                existe=True
                if contrasena==Password:
                    passw=True
            contenido_reg = archivo_de_usuarios.readline().strip()
        
        print("")
        if not existe:
            print("El Correo electronico que esta queriendo ingresar no esta en nuestra base de datos, registrese")
        elif not passw:
            print("Contraseña incorrecta, intentelo nuevamnete.")
        else:
            print("Ingreso exitoso!")
            return True
            
    limpiar_terminal(2)
        