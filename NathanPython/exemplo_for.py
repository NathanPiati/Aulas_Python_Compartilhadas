from os import system as limp
limp("cls")

valor = int(input("Digite um valor: "))

for x in range(valor + 1):

    if x % 10 == 0 and x > 0:

        continue
    
    print(f"O valor de X é: {x}")



