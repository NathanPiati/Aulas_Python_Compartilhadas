from itertools import count
from os import system as limp
limp("cls")

nome = input("Digite o seu nome: ")

letras = [letra for letra in nome]

print("*" * 50)
print("\n")
print("  ".join(letras))
print("\n")
print("*" * 50)

for letra in letras:
    print(letra)
    
print("\n")
print("*"*50)
print(f"Total de letras do seu nome é: {len(letras)}")
print("*"*50)


# for i in range(51):
#     print(i, end='; ')




# print(*[str(i) for i in range(51)], sep='; ')
