from itertools import count
from os import system as limp
limp("cls") 


vogais = "aeiou"
print("\n")
frase = input("Digite uma frase: ").lower()

print("\n")
print("Frase:", frase)
print("\n")
print("*"*50)

contador_vogais_frase = 0

for palavra in frase.lower().split():

    contador_vogais_palavra = 0
    vogais_palavra = []
    for letra in palavra:
        if letra in vogais:
            contador_vogais_frase += 1
            contador_vogais_palavra += 1
            vogais_palavra.append(letra)

    print(f"Vogais na palavra [{palavra}]: {', '.join(vogais_palavra)} ({contador_vogais_palavra})")

print("\n")
print("*"*50)
print("Número de vogais na frase:", contador_vogais_frase)

