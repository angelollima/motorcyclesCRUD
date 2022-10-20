from leitura_escrita import *  #importa as funções lerDados e salvarDados.
import os

def alterar(): #função para alterar moto.
    motos = lerDados()

    os.system("clear" if os.name == "posix" else "cls")

    #input pra receber o numero do chassi da moto
    chassiDaMoto = input("Digite o número do chassi da moto a qual quer alterar os itens: ")
    found = False #variavel com o valor Falso
    for moto in motos: #percorre a lista de motos.
        if chassiDaMoto == moto["chassi"]:  #verifica se o chassi passado existe em alguma moto.
            found = True #se o input for igual ao chassi da moto, Falso agora é Verdadeiro
            indexDaMoto = motos.index(moto) #acha o index (lugar) onde a moto está na lista.

            #Altera valores das chaves.
            moto["chassi"] = input("Digite o número do chassi da moto: ")
            moto["marca"] = input("Digite a marca da moto: ")
            moto["cilindrada"] = input("Digite a cilindrada da moto: ")
            moto["cor"] = input("Digite a cor da moto: ")
            moto["pneu"] = input("Digite a marca do pneu da moto: ")

            motos = lerDados() #chama a função lerDados.
            motos[indexDaMoto] = moto #altera a moto nova no lugar da velha.
            salvarDados(motos) #chama a função salvarDados com motos como argumento pro parametro.

            os.system("clear" if os.name == "posix" else "cls") #limpa o terminal (tela)
            print(10 * '-=-')
            print('Moto Alterada!!')
            print(10 * '-=-')
            input("Pressione ENTER para continuar...") #pausa o programa
            os.system("clear" if os.name == "posix" else "cls") #limpa o terminal (tela)

    if not found: #se o chassi da moto não for achado.
        print("Essa moto não esta cadastrada em nosso serviço")

        input("Pressione ENTER para continuar...") #pausa o programa
        os.system("clear" if os.name == "posix" else "cls") #limpa o terminal (tela)