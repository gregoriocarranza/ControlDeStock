import csv
proveedores_autorizados = ('gmail.com', 'hotmail.com', 'outlook.com')
caracteres_especiales = "!@#$%^&*()-+"

def ValidarCaracteresEspeciales(texto,textoDeError):
    user=input(texto)
    while any(char in caracteres_especiales for char in user):
        user=input(textoDeError)
    return user


def validar_email(texto,textoDeError,valida):
    email=input(texto)
    username, domain = email.split("@")  
    while domain not in proveedores_autorizados or not "@" in email:
        email=input(textoDeError)
        username, domain = email.split("@")
    # if valida:
        # validar_registro(email,"El correo electrónico ya está registrado.")
    return email

def validar_contrasena(texto,textoDeError1,textoDeError2):
    contrasena=input(texto)
    while len(contrasena) != 8:
        contrasena=input(textoDeError1)
        
    while (contrasena.isalpha() or contrasena.isdigit()) or not contrasena.isalnum():
        contrasena=input(textoDeError2)
    return contrasena


# def validar_registro(email,textoDeError):
#     with open('usuarios.csv', 'r+') as archivo_csv:
#         reader = csv.reader(archivo_csv)
#         for row in reader:
#             print(row)
#             if email.lower() == row[0].lower():
#                 return False
#     return True
