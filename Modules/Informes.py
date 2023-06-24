""" Falta:
        - Informe ventas    
"""

from Modules.Utils.Utils import pausa

def generarInformes():
    print('INFORMES'.center(70, '-'))
    print()
    with open("./Archivos/Productos.csv", 'r') as archivo_productos, open("./Archivos/Ventas.csv", 'r') as archivo_ventas:
        productos = []
        ventas = []

        producto = archivo_productos.readline().strip()
        while producto:
            productos.append(producto.split(';')) 
            producto = archivo_productos.readline().strip()
            
        venta = archivo_ventas.readline().strip()
        while venta:
            ventas.append(venta.split(';')) 
            venta = archivo_ventas.readline().strip()

        if productos:
            parameters=['CODIGO', 'PRODUCTO', 'PRECIO', 'STOCK']
            informeOrdenadoPrecio(productos,parameters)
            informeOrdenadoStock(productos,parameters)
            informeFormatoEspecial(productos)
            informeProductosSinStock(productos,parameters)
        else:
            print("No hay listado de productos, agrega uno para mostrar: ")
            
        
        if ventas:
            parameters=['CODIGO', 'PRODUCTO', 'VENDIDO', 'VENDEDOR']
            informeOrdenadoVentas(ventas,parameters)
        else:
            print("No hay listado de productos, agrega uno para mostrar: ")
            
        
        
    pausa()

# ------------------------------------------------------------ Informes ------------------------------------------------------------
def informeOrdenadoPrecio(productos,parameters):
    print()
    print('Informe ordenado por precio'.center(70, '-'))
    ordenarProductos(2, productos)
    imprimirResultados(productos,parameters)

def informeOrdenadoStock(productos,parameters):
    print()
    print('Informe ordenado por stock'.center(70, '-'))
    ordenarProductos(3, productos)
    imprimirResultados(productos,parameters)

def informeFormatoEspecial(productos):
    print()
    print('Informe con formato particular'.center(70, '-'))
    for x in range(len(productos)):
        print(f'Nombre: {productos[x][1]} / Precio: {productos[x][2]} / Stock: {productos[x][3]}')

def informeProductosSinStock(productos,parameters):
    productos = filter(lambda prod: int(prod[3]) == 0 , productos)
    if list(productos):
        print()
        print('Informe productos sin stock'.center(70, '-'))
        imprimirResultados(list(productos),parameters)

def informeOrdenadoVentas(ventas,parameters):
    print()
    print('Informe ordenado por cantidad de ventas'.center(70, '-'))
    ordenarProductos(2, ventas)
    imprimirResultados(ventas,parameters)
        
# ------------------------------------------------------------ Funciones Comunes ------------------------------------------------------------

def ordenarProductos(ordenIndice, productos):
    cambio = True
    while cambio:
        cambio = False
        for x in range(len(productos)-1):
            if(int(productos[x][ordenIndice]) > int(productos[x+1][ordenIndice])):
                cambio = True
                productos[x], productos[x+1] = productos[x+1], productos[x]
    return productos

def imprimirResultados(productos,parameters):
    print()
    print(parameters[0].ljust(20), parameters[1].ljust(20), parameters[2].ljust(20), parameters[3])
    print('-'.center(70, '-'))
    for x in range(len(productos)):
        print(productos[x][0].ljust(20), productos[x][1].ljust(20), f'${productos[x][2].ljust(20)}', productos[x][3])
    print()

    