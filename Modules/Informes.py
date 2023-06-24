""" Falta:
        - Informe ventas
        - Verificar datos suficientes         
"""

from Modules.Utils.Utils import pausa

def generarInformes():
    print('INFORMES'.center(70, '-'))
    print()
    with open("./Archivos/Productos.csv", 'r') as archivo_productos:
        productos = []

        producto = archivo_productos.readline().strip()
        while producto:

            productos.append(producto.split(';')) 
            producto = archivo_productos.readline().strip()

        if productos:
            informeOrdenadoPrecio(productos)
            informeOrdenadoStock(productos)
            informeFormatoEspecial(productos)
            informeProductosSinStock(productos)
        else:
            print("No hay listado de productos, agrega uno para mostrar: ")
            
        
        
    pausa()

# ------------------------------------------------------------ Informes ------------------------------------------------------------
def informeOrdenadoPrecio(productos):
    print()
    print('Informe ordenado por precio'.center(70, '-'))
    ordenarProductos(2, productos)
    imprimirResultados(productos)

def informeOrdenadoStock(productos):
    print()
    print('Informe ordenado por stock'.center(70, '-'))
    ordenarProductos(3, productos)
    imprimirResultados(productos)

def informeFormatoEspecial(productos):
    print()
    print('Informe con formato particular'.center(70, '-'))
    for x in range(len(productos)):
        print(f'Nombre: {productos[x][1]} / Precio: {productos[x][2]} / Stock: {productos[x][3]}')

def informeProductosSinStock(productos):
    productos = filter(lambda prod: int(prod[3]) == 0 , productos)
    if list(productos):
        print()
        print('Informe productos sin stock'.center(70, '-'))
        imprimirResultados(list(productos))
        
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

def imprimirResultados(productos):
    print()
    print('CODIGO'.ljust(20), 'PRODUCTO'.ljust(20), 'PRECIO'.ljust(20), 'STOCK')
    print('-'.center(70, '-'))
    for x in range(len(productos)):
        print(productos[x][0].ljust(20), productos[x][1].ljust(20), f'${productos[x][2].ljust(20)}', productos[x][3])
    print()

    