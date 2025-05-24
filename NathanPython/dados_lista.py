from os import system as limp
limp("cls")

print("Sistema de gerenciamento de dados pessoais\n")

dados_pessoais = []

while True:
    nome = input("Digite o seu nome: ")
    data_nascimento = input("Digite a sua data de nascimento no formato dd/mm/aaaa: ")
    altura = float(input("Digite a sua altura (em metros): ").replace(",", "."))
    peso = float(input("Digite o seu peso (em kg): "))
    cpf = input("Digite o seu CPF: ")
    telefone = input("Digite o seu telefone: ")

    dados_pessoais.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "altura": altura,
        "peso": peso,
        "cpf": cpf,
        "telefone": telefone
    })

    print("\n" + "*" * 50)
    print("DADOS PESSOAIS ARMAZENADOS:")

    for i, dado in enumerate(dados_pessoais, 1):
        print(f"\n[REGISTRO {i}]")
        print(f"1 - Nome: {dado['nome']}")
        print(f"2 - Data de nascimento: {dado['data_nascimento']}")
        print(f"3 - Altura: {dado['altura']} m")
        print(f"4 - Peso: {dado['peso']} kg")
        print(f"5 - CPF: {dado['cpf']}")
        print(f"6 - Telefone: {dado['telefone']}")
    print("\n" + "*" * 50)

    escolha = input("Deseja excluir o CPF de algum registro (s/n)? ")
    if escolha.lower() == "s":
        try:
            registro = int(input("Digite o número do registro (ex: 1, 2...): ")) - 1
            if 0 <= registro < len(dados_pessoais):
                dados_pessoais[registro]["cpf"] = None
                print(f"CPF do registro {registro + 1} excluído com sucesso.")
            else:
                print("Número de registro inválido!")
        except ValueError:
            print("Erro: Por favor, digite um número válido.")
    else:
        continuar = input("Deseja continuar cadastrando (s/n)? ")
        if continuar.lower() != "s":
            break

