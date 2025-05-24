from os import system as limp
limp("cls") 


nome = input("Digite o seu nome: ")
opcao = input("Deseja imprimir somente as vogais (V) ou consoantes (C)? ").upper()

vogais = []
consoantes = []

for letra in nome:
    if letra.upper() in "AEIOU":
        vogais.append(letra)
    else:
        consoantes.append(letra)

if opcao == "V":
    print("Vogais:", vogais)
elif opcao == "C":
    print("Consoantes:", consoantes)
else:
    print("Opção inválida.")

