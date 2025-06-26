from defs import *

sistema_de_usuarios = SistemaDeUsuarios(arquivo_externo_usuarios= "usuarios.json")

while True:
    opcao = sistema_de_usuarios.menu_principal()

    if opcao == "1":
        sistema_de_usuarios.adicionar_usuarios()

