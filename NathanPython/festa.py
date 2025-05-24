from os import system as limp
limp("cls")


def festa():
    convidados = {}  
    presentes = {}   

    while True:
        print("\nSistema de Convidados")
        print("\n")
        print("1. Adicionar convidado")
        print("2. Mostrar quantidade de convidados")
        print("3. Mostrar lista de convidados")
        print("4. Enviar presente para um convidado")
        print("5. Sair (digite '12345')")

        opcao = input("Escolha uma opção: ")

        
        if opcao == "1":
            nome = input("Digite o nome do convidado: ")
            indice = len(convidados) + 1  
            convidados[nome] = indice
            print(f"{nome} foi adicionado como convidado.")

        
        elif opcao == "2":
            print(f"Quantidade de convidados: {len(convidados)}")

        
        elif opcao == "3":
            if len(convidados) == 0:
                print("Não há convidados cadastrados.")
            else:
                print("Lista de convidados:")
                for nome, indice in convidados.items():
                    print(f"{indice}. {nome}")

        
        elif opcao == "4":
            if len(convidados) == 0:
                print("Não há convidados cadastrados. Adicione alguns convidados primeiro.")
            else:
                
                print("Escolha um convidado para enviar um presente:")
                for indice, nome in enumerate(convidados.keys(), 1):
                    print(f"{indice}. {nome}")
                
                escolha = input("Digite o número do convidado: ")
                
                
                if escolha.isdigit() and 1 <= int(escolha) <= len(convidados):
                    nome_convidado = list(convidados.keys())[int(escolha) - 1]
                    presente = input(f"Digite o presente para {nome_convidado}: ")
                    presentes[nome_convidado] = presente
                    print("*" * 50)
                    print(f"Presente enviado para {nome_convidado}: {presente}")
                    print("*" * 50)
                else:
                    print("Escolha inválida. Tente novamente.")
        
        
        elif opcao == "5" or opcao == "12345":
            print("Sistema finalizado.")
            break

        else:
            print("Opção inválida. Tente novamente.")


festa()
