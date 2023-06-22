import csv

#----------------------------------------------------------Validaciones de registro y ingreso----------------------------------------------------------

def ValidarCaracteresEspeciales(texto,textoDeError):
    caracteres_especiales = "!@#$%^&*()-+"
    user=input(texto).capitalize()
    while any(char in caracteres_especiales for char in user):
        user=input(textoDeError)
    return user


def validar_email(texto, textoDeError, valida):
    proveedores_autorizados = ('gmail.com', 'hotmail.com', 'outlook.com')
    while True:
        email = input(texto).lower()
        try:
            username, domain = email.split("@")
        except ValueError:
            print(textoDeError)
            continue
        if domain not in proveedores_autorizados or not "@" in email:
            print(textoDeError)
            continue
        if valida:
            if not validar_registro(email, "El correo electrónico ya está registrado."):
                continue
        return email

def validar_contrasena(texto,textoDeError1,textoDeError2):
    contrasena=input(texto)
    while len(contrasena) < 5:
        contrasena=input(textoDeError1)
        
    while (contrasena.isalpha() or contrasena.isdigit()) or not contrasena.isalnum():
        contrasena=input(textoDeError2)
    return contrasena

def validar_rango(texto,textoDeError,limi,lims):
    nro=int(input(texto))
    while(nro<limi or nro>lims):
        nro=int(input(textoDeError))
    return nro
    

def validar_registro(email,  textoDeError):
    resp=True
    with open("./Archivos/Usuarios.csv", 'r') as archivo_de_usuarios:
        contenido_reg = archivo_de_usuarios.readlines()
        for linea in contenido_reg:
            campos = linea.strip().split(';')
            email_registrado = campos[1]
            if email == email_registrado:
                print(textoDeError)
                resp= False
    return resp

#----------------------------------------------------------Validaciones ingreso de productos----------------------------------------------------------

# Función para validar si una cadena contiene solo caracteres alfanuméricos
def contiene_caracteres_alfanumericos(cadena,textoerror):
    b=True
    if (cadena.isalpha() or cadena.isdigit()) or not cadena.isalnum():
        print (textoerror," (Caracteres alfanumericos no encontrados)")
        b=False
    return b

# Función para validar si un número es un entero o decimal válido y positivo
def validar_numero_positivo(numero):
    try:
        num = float(numero)
        if num >= 0:
            return True
        else:
            return False
    except ValueError:
        return False


def validar_codigo(codigos_existentes,texto,textoError):
    codigo = input("Ingrese el código del producto: ")
    print(codigo in codigos_existentes)
    print(contiene_caracteres_alfanumericos(codigo,textoError))
    while codigo in codigos_existentes or not contiene_caracteres_alfanumericos(codigo,textoError):
        codigo = input(textoError)
    return codigo
