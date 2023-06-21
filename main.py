from Modules.Menues.LoginMenu import LoginMenu
from Modules.Menues.MainManue import MainManue
from Modules.Utils.Utils import limpiar_terminal,initCsv,archivoDeUsuarios,archivoDeProductos

initCsv(archivoDeUsuarios)
initCsv(archivoDeProductos)


limpiar_terminal(0.1)
inicio=LoginMenu()

while inicio:
    MainManue()
    print("Main")