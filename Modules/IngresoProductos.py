from Modules.Validaciones import validar_codigo,contiene_caracteres_alfanumericos,validar_numero_positivo


def ingresoDeProductos():
    
    codigos,nombres,precios=Rescate_de_variables()
    print(codigos,nombres,precios)
    
    codigo = validar_codigo(codigos,"Ingrese el código del producto: ","El código ingresado no es válido o ya existe. Ingrese nuevamente: ")

    nombre = input("Ingrese el nombre del producto: ")
    while not contiene_caracteres_alfanumericos(nombre,"El nombre ingresado contiene caracteres especiales. Intente nuevamente: "):
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
    
    with open("./Archivos/Productos.csv", 'a') as archivo_productos:
        archivo_productos.write(f"{codigo};{nombre};{precio};{stock}\n")

    return True


def Rescate_de_variables():
    codigos = []
    nombres = []
    precios=[]
    with open("./Archivos/Productos.csv", 'r') as archivo_productos:
        contenido_reg = archivo_productos.readlines()
        for linea in contenido_reg:
            campos = linea.strip().split(';')
            codigos.append(campos[0])
            nombres.append(campos[1])
            precios.append(campos[2])
            
    return codigos,nombres,precios
