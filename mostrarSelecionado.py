from leitura_escrita import * #importa as funções lerDados e salvarDados.
import os

def mostrarSelecionado(): #função para mostrar apenas uma moto por vez
    motos = lerDados() #chama a função lerDados

    os.system("clear" if os.name == "posix" else "cls")

    chassiDaMoto = input("Digite o chassi da moto a qual quer ver: ")
    #input para selecionar a moto que quer ser mostrada pelo chasi

    print(10 * '-=-')

    for moto in motos: #percorre a lista de motos.
        if chassiDaMoto == moto["chassi"]: #verifica se o chassi passado existe em alguma moto.
            #mostra todos os atributos da moto.
            print(f'Chassi: {moto["chassi"]}')
            print(f'Marca: {moto["marca"]}')
            print(f'Cilindrada: {moto["cilindrada"]}')
            print(f'Cor: {moto["cor"]}')
            print(f'Pneu: {moto["pneu"]}')

            print(10 * '-=-')
    input("Pressione ENTER para continuar...") #pausa o programa até que o usuario clique em enter
    os.system("clear" if os.name == "posix" else "cls") #apaga o terminal