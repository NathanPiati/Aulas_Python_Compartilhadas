from time import sleep as s

numero1 = input("Digite um número: ")
numero2 = input("Digite o segundo número: ")

try:
    num1 = int(numero1)
    num2 = int(numero2)

    if num1 == num2:
        print("Os números são iguais!")
        print("Por favor digite dois números diferentes.")
    elif num1 > num2:
        print("-"*30)
        print(".", end="")
        s(0.5)
        print(".", end="")
        s(0.5)
        print(".")
        print(f"{num1} é maior que {num2}")
    else:
        print("-"*30)
        print(f"{num2} é maior que {num1}")

except:

    print("Erro: Por favor, digite um número.")

input("Pressione qualquer tecla para sair...")