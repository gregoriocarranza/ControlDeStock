from Modules.Menues.LoginMenu import LoginMenu
from Modules.Menues.MainMenu import MainMenu
from Modules.Utils.Utils import limpiar_terminal, initCsv,pausa

initCsv("./Archivos/Usuarios.csv")
initCsv("./Archivos/Productos.csv")
initCsv("./Archivos/Ventas.csv")


limpiar_terminal(0.1)
debug=True   #False: No debugging // True: Debugging
inicio = LoginMenu(debug)


while inicio:
    limpiar_terminal(1)
    inicio = MainMenu()
    
    

print("\n\nFin del programa\n")
pausa()
