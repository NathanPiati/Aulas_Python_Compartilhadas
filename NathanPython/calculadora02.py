from os import system as limp
limp("cls")


def soma(num1, num2):
    res = num1 + num2
    return res


def subtracao(num1, num2):
    res = num1 - num2
    return res


def multiplicacao(num1, num2):
    res = num1 * num2
    return res


def divisao(num1, num2):
    res = num1 / num2
    return res


def menu():
    print("*" * 50)
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    print("*" * 50)
    opcao = int(input("Digite a opção desejada: "))
    print("*" * 50)
    return opcao


def main():
    while True:
        opcao = menu()
        if opcao == 5:
            break
        elif 1 <= opcao <= 4:

            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if opcao == 1:
                print(f"Resultado da soma: {num1} + {num2} = {soma(num1, num2)}")
            elif opcao == 2:
                print(f"Resultado da subtração: {num1} - {num2} = {subtracao(num1, num2)}")
            elif opcao == 3:
                print(f"Resultado da multiplicação: {num1} x {num2} = {multiplicacao(num1, num2)}")
            elif opcao == 4:
                print(f"Resultado da divisão: {num1} / {num2} = {divisao(num1, num2)}")
        else:
            print("Opção inválida. Tente novamente.")


main()
