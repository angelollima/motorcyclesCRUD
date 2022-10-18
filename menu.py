import os
#apagar o menu toda vez!

def menu():
    print(11 * '\033[1;35m-=-\033[m')
    print('\033[1;35m:=:\033[0m \033[1;32m1 - Cadastrar Moto\033[0m        \033[1;35m:=:\033[0m')
    print('\033[1;35m:=:\033[0m \033[1;32m2 - Deletar Moto\033[1;32m          \033[1;35m:=:\033[0m')
    print('\033[1;35m:=:\033[0m \033[1;32m3 - Alterar Moto\033[1;32m          \033[1;35m:=:\033[0m')
    print('\033[1;35m:=:\033[0m \033[1;32m4 - Ver Todas Motos\033[1;32m       \033[1;35m:=:\033[0m')
    print('\033[1;35m:=:\033[0m \033[1;32m5 - Ver Moto por Chassis\033[1;32m  \033[1;35m:=:\033[0m')
    print('\033[1;35m:=:\033[0m \033[1;32m6 - Sair\033[1;32m                  \033[1;35m:=:\033[0m')
    print(11 * '\033[1;35m-=-\033[m')
    return int(input('\033[1mEscolha uma opção: \033[0m'))