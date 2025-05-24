from os import system as Limpar
Limpar("cls")


try:
    x = float(input("Digite um valor:"))
    z = float(input("Digite um valor 2:"))

    if x > z:
        print("O valor é maior que Z!")
    elif x == z:
        print("O valor é igual a Z.")    

# Não precisa usar diferente por já conter as outras condições       
 
    elif x != z:
        print("O valor é diferente de Z.")    
    elif x >= z:
        print("O valor é maior ou igual a Z.")
    elif x < z:
        print("O valor é menor que Z!")    
    elif x <= z:
        print("O valor é menor ou igual a Z.")    

except ValueError:
    print("Erro: Por favor, digite um número válido.")


print("Fim do programa!");