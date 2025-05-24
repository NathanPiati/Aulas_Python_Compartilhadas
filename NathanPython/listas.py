from os import system as limp
limp("cls")



valores = [37, 48, 11, 29, 100, 99]

print("*"*50)
print("Posição dos números:")
print ("[0, 1, 2, 3, 4, 5]")
print("*"*50)

while True:
    
    print(valores)

    print("\n")
    selecao = int(input("Digite a posição do número que deseja deletar (-1 para sair): "))

    if selecao == -1:
        break
    if 0 <= selecao < len(valores):
        del valores[selecao]
    else:
        print("Posição inválida!")

print("\n")
print("Lista final:", valores)

