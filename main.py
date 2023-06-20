from Modules.Menues.LoginMenu import LoginMenu
# from Modules.Menues.MainManue import MainManue
from Modules.Utils.Utils import limpiar_terminal,initCsv
archivoDeUsuarios="./archivos/usuarios.csv"
archivoDeProductos="./archivos/productos.csv"

initCsv(archivoDeUsuarios)
initCsv(archivoDeProductos)


limpiar_terminal(0.1)
inicio=LoginMenu(archivoDeUsuarios)

while inicio:
    print("Main")