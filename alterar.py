from leitura_escrita import *
import os

def alterar():
    motos = lerDados()

    os.system("clear" if os.name == "posix" else "cls")

    chassiDaMoto = input("Digite o número do chassi da moto a qual quer alterar os itens: ")
    found = False
    for moto in motos:
        if chassiDaMoto == moto["chassi"]:
            found = True
            indexDaMoto = motos.index(moto)
            moto["chassi"] = input("Digite o número do chassi da moto: ")
            moto["marca"] = input("Digite a marca da moto: ")
            moto["cilindrada"] = input("Digite a cilindrada da moto: ")
            moto["cor"] = input("Digite a cor da moto: ")
            moto["pneu"] = input("Digite a marca do pneu da moto: ")

            motos = lerDados()
            motos[indexDaMoto] = moto
            salvarDados(motos)

            os.system("clear" if os.name == "posix" else "cls")
            print(10 * '-=-')
            print('Moto Alterada!!')
            print(10 * '-=-')
            input("Pressione ENTER para continuar...")
            os.system("clear" if os.name == "posix" else "cls")

    if not found:
        print("Essa moto não esta cadastrada em nosso serviço")

        input("Pressione ENTER para continuar...")
        os.system("clear" if os.name == "posix" else "cls")