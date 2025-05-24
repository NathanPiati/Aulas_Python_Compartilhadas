from os import system as limp
limp("cls") 


nome = input("Digite o seu nome: ")
data = input("Digite a sua data de nascimento: ")
cpf = input("Digite o seu CPF: ")
telefone = input("Digite o seu telefone: ")

info = {"Nome": nome, "Data": data, "CPF": cpf, "Telefone": telefone}

print( "*" * 50 + "\n" )
print("Dados inseridos:")
print( "*" * 50 + "\n" ) 

print(f"Nome: {info['Nome']}")
print(f"Data: {info['Data']}") 
print(f"CPF: {info['CPF']}")
print(f"Telefone: {info['Telefone']}")

chave_delete = input("Digite o nome da chave que deseja deletar (Nome, Idade, Cidade): ")

if chave_delete in info:
    del info[chave_delete]
    print(f"Registro '{chave_delete}' deletado com sucesso.")
else:
    print("Registro não encontrado no dicionário.")

