from Menu import menu
from utils import limpiar_terminal
# def initAllScv():
#     try:
#       with open(r'usuarios.csv', 'w+') as userScv:
#           print("archivo Creado Con Exito")
#     except IOError as msj:
#         print(f'ERROR ---------> {msj}')
#     return True

# initAllScv()
limpiar_terminal(0.1)
inicio=menu()

while inicio:
    print("Main")