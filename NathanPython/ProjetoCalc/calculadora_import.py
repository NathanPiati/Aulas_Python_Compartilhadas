import os
import arquivo_funcoes as af

def limpar_tela():
    """Limpa a tela do terminal"""
    os.system("cls" if os.name == "nt" else "clear")

def exibir_menu():
    """Exibe o menu de opções da calculadora com '*' no final de cada linha"""
    print("* " + " Calculadora Python ".center(46, "-") + " *")
    print("* " + " 1 - Soma".ljust(46) + " *")  
    print("* " + " 2 - Subtração".ljust(46) + " *")
    print("* " + " 3 - Multiplicação".ljust(46) + " *")
    print("* " + " 4 - Divisão".ljust(46) + " *")
    print("* " + " 5 - Exponenciação".ljust(46) + " *")
    print("* " + " 6 - Raiz".ljust(46) + " *")
    print("* " + " 7 - Seno".ljust(46) + " *")
    print("* " + " 8 - Cosseno".ljust(46) + " *")
    print("* " + " 9 - Sair".ljust(46) + " *")
    print("* " + "-" * 46 + " *")


def calculadora():
    """Função principal da calculadora"""
    while True:
        limpar_tela()
        exibir_menu()

        try:
            opcao = int(input("Digite a opção desejada: "))

            if opcao == 9:
                print("Saindo...")
                break

            if 1 <= opcao <= 8:
                numero1 = float(input("Digite o primeiro número: "))
                if opcao != 6:  # Raiz quadrada só usa um número
                    numero2 = float(input("Digite o segundo número: "))

                if opcao == 1:
                    resultado = af.soma(numero1, numero2)
                elif opcao == 2:
                    resultado = af.subtracao(numero1, numero2)
                elif opcao == 3:
                    resultado = af.multiplicacao(numero1, numero2)
                elif opcao == 4:
                    resultado = af.divisao(numero1, numero2)
                elif opcao == 5:
                    resultado = af.exponenciacao(numero1, numero2)
                elif opcao == 6:
                    resultado = af.raiz(numero1)
                elif opcao == 7:
                    resultado = af.seno(numero1)
                elif opcao == 8:
                    resultado = af.cosseno(numero1)

                print(f"Resultado: {resultado}")
                
                # Pausa para ver o resultado antes de continuar
                input("Pressione Enter para continuar...")

            else:
                print("Opção inválida. Tente novamente.")

        except ValueError:
            print("Erro: Por favor, digite um número válido.")

if __name__ == "__main__":
    calculadora()
