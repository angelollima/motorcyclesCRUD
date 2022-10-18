from leitura_escrita import *  #importa as funções lerDados e salvarDados.
import os

def deletar(): #função para deletar moto (entidade)
    motos = lerDados()  #chama a função lerDados

    os.system("clear" if os.name == "posix" else "cls") #Limpa o terminal (tela)

    chassiDaMoto = input("Digite o chassi da moto a qual quer deletar: ") #input pra ver qual chassi da moto quer deletar

    for moto in motos: #percorre toda lista de motos
        if chassiDaMoto == moto["chassi"]:  #verifica se o chassi da moto existe
            motos.remove(moto) #se existir, remove a moto inteira
            salvarDados(motos)  #chama a função salvarDados

    os.system("clear" if os.name == "posix" else "cls") #apaga o terminal (limpa)
    print(10 * '-=-')
    print('Moto Deletada!!')
    print(10 * '-=-')
    input("Pressione ENTER para continuar...") #pausa o programa até que o usuario clique em enter
    os.system("clear" if os.name == "posix" else "cls") #apaga o terminal (limpa)