from Modules.Validaciones import validar_codigo,validar_nombre_producto, validar_precio_stock


def ingresoDeProductos():
    codigos,nombres,precios=Rescate_de_variables()
    # print(codigos,nombres,precios)
    codigo = validar_codigo(codigos,"Ingrese el código del producto o EXIT para salir: ","El código ingresado no es válido o ya existe. Ingrese nuevamente: ")
    
    while codigo!=-1:
        
        nombre = validar_nombre_producto("Ingrese el nombre del producto: ", "El nombre ingresado no es valido. Intente nuevamente: ")
        precio = validar_precio_stock("Ingrese el precio unitario del producto: ", "El precio ingresado no es válido. Intente nuevamente: ")
        stock = validar_precio_stock("Ingrese la cantidad inicial de stock del producto: ", "La cantidad ingresada no es válida. Intente nuevamente:")

        with open("./Archivos/Productos.csv", 'a') as archivo_productos:
            archivo_productos.write(f"{codigo};{nombre};{precio};{stock}\n")
            print('Ingreso de producto exitoso!')
            
        codigo = validar_codigo(codigos,"Ingrese el código del producto o EXIT para salir: ","El código ingresado no es válido o ya existe. Ingrese nuevamente: ")
    return True

def Rescate_de_variables():
    codigos = []
    nombres = []
    precios=[]

    # with open("./Archivos/Productos.csv", 'r') as archivo_productos:
    #     contenido_reg = archivo_productos.readlines()
    #     for linea in contenido_reg:
    #         campos = linea.strip().split(';')
    #         codigos.append(campos[0])
    #         nombres.append(campos[1])
    #         precios.append(campos[2])
    
    
    with open("./Archivos/Productos.csv", 'r') as archivo_productos:
        archivo_productos.seek(0)
        contenido_reg = archivo_productos.readline().strip()
        while contenido_reg:
            codigo,nombre,precio,stock = contenido_reg.split(';')

            codigos.append(codigo)
            nombres.append(nombre)
            precios.append(precio)
            contenido_reg = archivo_productos.readline().strip()
            
    return codigos,nombres,precios
