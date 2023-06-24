import csv

# ----------------------------------------------------------Validaciones de registro y ingreso----------------------------------------------------------


def validar_caracteres_especiales(texto, textoDeError):
    user = input(texto).capitalize()
    while caracteres_especiales(user):
        user = input(textoDeError)
    return user


def validar_email(texto, textoDeError, valida):
    proveedores_autorizados = ("gmail.com", "hotmail.com", "outlook.com")
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


def validar_contrasena(texto, textoDeError1, textoDeError2):
    contrasena = input(texto)
    while validar_cantidad_caracteres(contrasena, 5):
        contrasena = input(textoDeError1)

    while not contiene_caracteres_alfanumericos(contrasena):
        contrasena = input(textoDeError2)
    return contrasena


def validar_registro(email, textoDeError):
    resp = True
    with open("./Archivos/Usuarios.csv", "r") as archivo_de_usuarios:
        contenido_reg = archivo_de_usuarios.readline().strip()
        while contenido_reg:
            campos = contenido_reg.split(";")
            email_registrado = campos[1]
            if email == email_registrado:
                print(textoDeError)
                resp = False
            contenido_reg = archivo_de_usuarios.readline().strip()
    return resp


# ----------------------------------------------------------Validaciones ingreso de productos----------------------------------------------------------


def validar_precio_stock(texto, textoError):
    valor = input(texto)
    while not validar_numero_positivo(valor):
        valor = input(textoError)
    return valor


def validar_codigo(codigo,codigos_existentes):
    b=False
    if (codigo in codigos_existentes and contiene_caracteres_alfanumericos(codigo)):
        b= True
    return b


def validar_nombre_producto(texto, textoError):
    nombre = input(texto)
    while caracteres_especiales(nombre) or nombre.isdigit():
        nombre = input(textoError)
    return nombre

def busq_indice(numero, lista):
    return lista.index(numero)
# ----------------------------------------------------------Validaciones venta de productos----------------------------------------------------------


def validar_stock_disponible(stock, texto, textoError):
    valor = validar_precio_stock(texto, textoError)
 
    while int(valor) > int(stock):
        print("Error, stock insuficiente para realizar la venta")
        valor = validar_precio_stock(texto, textoError)
    return valor


# ----------------------------------------------------------Validaciones Comunes----------------------------------------------------------
def caracteres_especiales(string):
    caracteres_especiales = "!@#$%^&*()-+"
    if any(char in caracteres_especiales for char in string):
        return True
    return False


# Función para validar si una cadena contiene solo caracteres alfanuméricos
def contiene_caracteres_alfanumericos(cadena):
    if not (cadena.isalpha() or cadena.isdigit()) and cadena.isalnum():
        return True
    return False


# Función para validar si un número es un entero o decimal válido y positivo
def validar_numero_positivo(numero):
    try:
        num = int(numero)
        if num >= 0:
            return True
        else:
            return False
    except ValueError:
        return False


# Funcion para validar si un numero esta en rango
def validar_rango(texto, textoDeError, limi, lims):
    nro = int(input(texto))
    while nro < limi or nro > lims:
        nro = int(input(textoDeError))
    return nro


# Funcion para validar si un numero es menor al limite
def validar_cantidad_caracteres(string, limite):
    if len(string) < limite:
        return True
    return False
