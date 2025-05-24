from os import system as limp
limp("cls")


print("*"*50)
print("Se você esqueceu alguma tabuada, vou te ajudar!\n")
print("Vou te dar a tabuada do número que você digitar!\n")
print("*"*50)

while True:
    try:
        numero = int(input("Digite um número: "))
    except ValueError:
        print("Erro: Por favor, digite um número válido.")
        continue

    print("*"*50)
    print(f"Tabuada do {numero}\n")
    print("*"*50)



    contador = 1
    while contador <= 10:
        resultado = numero * contador
    

        print(f"{numero} x {contador:2d} = {resultado:2d}")
        contador += 1

    print("*"*50)
    print("Fim da tabuada!\n")
    print("*"*50)

