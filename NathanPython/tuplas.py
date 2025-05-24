from os import system as limp
limp("cls")

def mostrar_dados(registros):
    print("\n" + "*" * 50)
    if not registros:
        print("Nenhum dado cadastrado.")
    else:
        print("DADOS CADASTRADOS:")
        for i, registro in enumerate(registros, 1):
            nome, data_nascimento, altura, peso, cpf, telefone = registro
            print(f"\n[REGISTRO {i}]")
            print(f"Nome: {nome}")
            print(f"Data de nascimento: {data_nascimento}")
            print(f"Altura: {altura} m")
            print(f"Peso: {peso} kg")
            print(f"CPF: {cpf}")
            print(f"Telefone: {telefone}")
    print("\n" + "*" * 50)


# Lista para armazenar os registros como tuplas
dados_pessoais = []

while True:
    print("\n--- MENU ---")
    print("1 - Cadastrar novo registro")
    print("2 - Mostrar todos os registros")
    print("3 - Excluir um registro")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o seu nome: ")
        data_nascimento = input("Digite a sua data de nascimento (dd/mm/aaaa): ")
        altura = float(input("Digite a sua altura (em metros): ").replace(",", "."))
        peso = float(input("Digite o seu peso (em kg): "))
        cpf = input("Digite o seu CPF: ")
        telefone = input("Digite o seu telefone: ")

        registro = (nome, data_nascimento, altura, peso, cpf, telefone)
        dados_pessoais.append(registro)
        print("Registro adicionado com sucesso!")

    elif opcao == "2":
        mostrar_dados(dados_pessoais)

    elif opcao == "3":
        mostrar_dados(dados_pessoais)
        if dados_pessoais:
            try:
                indice = int(input("Digite o número do registro que deseja excluir (ou 0 para cancelar): "))
                if indice == 0:
                    print("Exclusão cancelada.")
                elif 1 <= indice <= len(dados_pessoais):
                    del dados_pessoais[indice - 1]
                    print("Registro excluído com sucesso.")
                else:
                    print("Número de registro inválido.")
            except ValueError:
                print("Por favor, digite um número válido.")
        else:
            print("Não há registros para excluir.")

    elif opcao == "4":
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")

    input("Pressione Enter para continuar...")
