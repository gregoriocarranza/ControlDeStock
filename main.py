from Modules.Menues.LoginMenu import LoginMenu
from Modules.Menues.MainMenu import MainMenu
from Modules.Utils.Utils import limpiar_terminal,initCsv

initCsv("./Archivos/Usuarios.csv")
initCsv("./Archivos/Productos.csv")
initCsv("./Archivos/Ventas.csv")


limpiar_terminal(0.1)
# inicio=True
inicio=LoginMenu()


while inicio:
    limpiar_terminal(2)
    inicio=MainMenu()
    print("Main")