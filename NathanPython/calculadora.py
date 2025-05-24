


print("TESTE")
valor1 = float (input("digite um valor:"))
print(valor1)




from os import system as limp
limp("cls")

while True:
    try:
        numero1 = int(input("Digite o primeiro número: "))
        break
    except ValueError:
        print("Erro: Por favor, digite um número válido.")

while True:
    try:
        numero2 = int(input("Digite o segundo número: "))
        break
    except ValueError:
        print("Erro: Por favor, digite um número válido.")

resultado = numero1 * numero2
print(f"Resultado da multiplicação: {numero1} x {numero2} = {resultado}")