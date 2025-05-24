from os import system as limp
limp("cls")

pessoas = 10

while pessoas > 0:
    print(f"Existem {pessoas} pessoas na sala.")
    pessoas -= 1

print("Fim da contagem!")