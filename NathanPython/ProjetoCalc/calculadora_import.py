import os
import arquivo_funcoes as fn
import historico as hist


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def exibir_menu():
    print("* " + " Bem-vindo à Calculadora Python ".center(46, "-") + " *")
    print("* " + " 1 - Soma".ljust(46) + " *")
    print("* " + " 2 - Subtração".ljust(46) + " *")
    print("* " + " 3 - Multiplicação".ljust(46) + " *")
    print("* " + " 4 - Divisão".ljust(46) + " *")
    print("* " + " 5 - Exponenciação".ljust(46) + " *")
    print("* " + " 6 - Raiz Quadrada".ljust(46) + " *")
    print("* " + " 7 - Seno".ljust(46) + " *")
    print("* " + " 8 - Cosseno".ljust(46) + " *")
    print("* " + " 9 - Tangente".ljust(46) + " *")
    print("* " + " 10 - Ver Histórico".ljust(46) + " *")
    print("* " + " 11 - Limpar Histórico".ljust(46) + " *")
    print("* " + " 0 - Sair".ljust(46) + " *")
    print("* " + "-" * 46 + " *")


def calculadora():
    while True:
        limpar_tela()
        exibir_menu()

        try:
            opcao = int(input("Digite a opção desejada: "))

            if opcao == 0:
                print("Saindo...")
                break

            elif opcao == 10:
                hist.exibir_historico()
                input("Pressione Enter para voltar ao menu...")

            elif opcao == 11:
                hist.deletar_historico()
                input("Pressione Enter para voltar ao menu...")

            elif opcao in [1, 2, 3, 4, 5]:
                numero1 = float(input("Digite o primeiro número: "))
                numero2 = float(input("Digite o segundo número: "))

                if opcao == 1:
                    resultado = fn.soma(numero1, numero2)
                    operacao = f"{numero1} + {numero2}"
                elif opcao == 2:
                    resultado = fn.subtracao(numero1, numero2)
                    operacao = f"{numero1} - {numero2}"
                elif opcao == 3:
                    resultado = fn.multiplicacao(numero1, numero2)
                    operacao = f"{numero1} * {numero2}"
                elif opcao == 4:
                    resultado = fn.divisao(numero1, numero2)
                    operacao = f"{numero1} / {numero2}"
                elif opcao == 5:
                    resultado = fn.exponenciacao(numero1, numero2)
                    operacao = f"{numero1} ^ {numero2}"

                print(f"Resultado: {resultado}")
                hist.salvar_historico(operacao, resultado)
                input("Pressione Enter para continuar...")

            elif opcao in [6, 7, 8, 9]:
                numero = float(input("Digite o número: "))

                if opcao == 6:
                    resultado = fn.raiz(numero)
                    operacao = f"√{numero}"
                elif opcao == 7:
                    resultado = fn.seno(numero)
                    operacao = f"sen({numero})"
                elif opcao == 8:
                    resultado = fn.cosseno(numero)
                    operacao = f"cos({numero})"
                elif opcao == 9:
                    resultado = fn.tangente(numero)
                    operacao = f"tan({numero})"

                print(f"Resultado: {resultado}")
                hist.salvar_historico(operacao, resultado)
                input("Pressione Enter para continuar...")

            else:
                print("Opção inválida. Tente novamente.")
                input("Pressione Enter para continuar...")

        except ValueError:
            print("Erro: Por favor, digite um número válido.")
            input("Pressione Enter para continuar...")

if __name__ == "__main__":
    calculadora()
