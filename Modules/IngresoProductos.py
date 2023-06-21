from Modules.Validaciones import validar_codigo,contiene_caracteres_alfanumericos,validar_numero_positivo
from Modules.Utils.Utils import archivoDeProductos



def ingresoDeProductos():
    
    codigos,nombres=Rescate_de_variables()
    print(codigos,nombres)
    codigo = input("Ingrese el código del producto: ")
    while not validar_codigo(codigo, codigos):
        print("El código ingresado no es válido o ya existe. Intente nuevamente.")
        codigo = input("Ingrese el código del producto: ")

    nombre = input("Ingrese el nombre del producto: ")
    while not contiene_caracteres_alfanumericos(nombre):
        print("El nombre ingresado contiene caracteres especiales. Intente nuevamente.")
        nombre = input("Ingrese el nombre del producto: ")

    precio = input("Ingrese el precio unitario del producto: ")
    while not validar_numero_positivo(precio):
        print("El precio ingresado no es válido. Intente nuevamente.")
        precio = input("Ingrese el precio unitario del producto: ")

    stock = input("Ingrese la cantidad inicial de stock del producto: ")
    while not validar_numero_positivo(stock):
        print("La cantidad ingresada no es válida. Intente nuevamente.")
        stock = input("Ingrese la cantidad inicial de stock del producto: ")

    codigos.append(codigo)
    nombres.append(nombre)
    
    with open(archivoDeProductos, 'a') as archivo_productos:
        archivo_productos.write(f"{codigo};{nombre};{precio};{stock}\n")

    return True


def Rescate_de_variables():
    codigos = []
    nombres = []
    # with open(archivoDeProductos, 'r') as archivo_productos:
    #     archivo_productos.seek(0)
    #     contenido_reg = archivo_productos.readline().strip()
    #     while contenido_reg:
    #         codigo,nombre,precio,stock = contenido_reg.split(';')
    #         print(codigo,nombre,precio,stock)
    #         codigos.append(codigo)
    #         nombres.append(nombre)
    #         contenido_reg = archivo_productos.readline().strip()
    
    with open(archivoDeProductos, 'r') as archivo_productos:
        contenido_reg = archivo_productos.readlines()
        for linea in contenido_reg:
            campos = linea.strip().split(';')
            codigos.append(campos[0])
            nombres.append(campos[1])
            
    return codigos,nombres
