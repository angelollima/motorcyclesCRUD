from leitura_escrita import * #importa as funções lerDados e salvarDados.
import os

def mostrarTudo(): #função para mostrar tudo.
    motos = lerDados() #chama a função lerDados

    os.system("clear" if os.name == "posix" else "cls")

    print(10 * '-=-')

    for moto in motos: #percorre a lista de motos.
        #mostra todos os atributos das motos, uma moto por vez até acabar.
        print(f'Chassi: {moto["chassi"]}')
        print(f'Marca: {moto["marca"]}')
        print(f'Cilindrada: {moto["cilindrada"]}')
        print(f'Cor: {moto["cor"]}')
        print(f'Pneu: {moto["pneu"]}')

        #print(moto)

        print(10 * '-=-')
    input("Pressione ENTER para continuar...")
    os.system("clear" if os.name == "posix" else "cls")
