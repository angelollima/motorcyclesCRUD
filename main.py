from cadastrar import *
from mostrarTudo import *
from mostrarSelecionado import *
from menu import *
from deletar import *
from alterar import *

import os

def main():
    os.system("clear" if os.name == "posix" else "cls")
    while True:
        opcao = menu()
        if opcao == 1:
            print(cadastrar())
        elif opcao == 2:
            print(deletar())
        elif opcao == 3:
            print(alterar())
        elif opcao == 4:
            print(mostrarTudo())
        elif opcao == 5:
            print(mostrarSelecionado())
        elif opcao == 6:
            os.system("clear" if os.name == "posix" else "cls")
            break

if __name__ == '__main__':
    main()