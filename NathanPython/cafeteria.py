import sys

class Cafeteria:
    def __init__(self):
        self.initUI()

    def initUI(self):
        print("ESCOLHA UMA BEBIDA ABAIXO:")

        opcoes = ["1 - CAFÉ EXPRESSO", "2 - CAFÉ COM LEITE", "3 - CAPPUCINO", "4 - ÁGUA QUENTE", "5 - LEITE PURO"]
        for opcao in opcoes:
            print(opcao)

        opcao = input("Digite a opção desejada: ")
        if opcao == "1":
            print("Cafe expresso")
        elif opcao == "2":
            print("Cafe com leite")
        elif opcao == "3":
            print("Cappuccino")
        elif opcao == "4":
            print("Agua quente")
        elif opcao == "5":
            print("Leite puro")

        # Validação de código do menu secreto
        elif opcao == "75452":
            print("*"*45)

            print("\n")
            print("+++++++ Menu secreto liberado via código! +++++++")
            print("\n")
            print("*"*50 )
            print("-"*50 ) 
            print("*"*50 ) 
            print("-"*50 ) 
            print ("","MANUTENÇÃO DA MÁQUINA", "", sep="*"*14)
            print ("\nESCOLHA UMA OPERAÇÃO DE MANUTENÇÃO ABAIXO:")
            print("\n1 - LIMPAR MAQUINA")
            print("2 - ABRIR GAVETA DE MOEDAS")
            print("3 - ABRIR GAVETA DE CAFÉ")
            print("4 - ABRIR GAVETA DE LEITE")

            manutencao = input("Digite a opção desejada: ")
            if manutencao == "1":
                print("Máquina limpa")
            elif manutencao == "2":
                print("Gaveta de moedas aberta")
            elif manutencao == "3":
                print("Gaveta de café aberta")
            elif manutencao == "4":
                print("Gaveta de leite aberta")
            else:
                print("Operação de manutenção inválida")
        else:
            print("Opção inválida")


if __name__ == '__main__':
    ex = Cafeteria()

