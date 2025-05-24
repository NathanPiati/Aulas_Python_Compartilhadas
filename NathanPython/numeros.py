from os import system as limp
limp("cls") 


pares = 0

while True:
    try:
        num = int(input("Digite um número inteiro: "))

        if num % 2 == 0:
            print("O número é par!")
            pares += 1
        else:
            print("O número é impar!")

        if pares == 3:
            print("Obrigado!")
            break

    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido.")



from os import system as limp
limp("cls")

pares = 0

for _ in range(10):  # Repete 10 vezes
    try:
        num = int(input("Digite um número inteiro: "))

        if num % 2 == 0:
            print("O número é par!")
            pares += 1
        else:
            print("O número é impar!")

        if pares == 3:
            print("Obrigado!")
            break

    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido.")

