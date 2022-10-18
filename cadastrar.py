from leitura_escrita import * #importa as funções lerDados e salvarDados.
import os

def cadastrar() -> dict: #função para cadastrar moto.
    os.system("clear" if os.name == "posix" else "cls")
    moto = {} #cria um dicionario vazio.

    #chaves que estão recebendo os valores por inputs
    moto["chassi"] = input("Digite o número do chassi da moto: ")
    moto["marca"] = input("Digite a marca da moto: ")
    moto["cilindrada"] = input("Digite a cilindrada da moto: ")
    moto["cor"] = input("Digite a cor da moto: ")
    moto["pneu"] = input("Digite a marca do pneu da moto: ")

    motos = lerDados() #chama a função lerDados
    motos.append(moto) #adiciona ao final da lista.
    salvarDados(motos) #chama a função salvarDados com motos como argumento. 

    os.system("clear" if os.name == "posix" else "cls")
    print(10 * '-=-')
    print('Moto Cadastrada!!')
    print(10 * '-=-')
    input('Pressione ENTER para continuar...')
    os.system("clear" if os.name == "posix" else "cls")