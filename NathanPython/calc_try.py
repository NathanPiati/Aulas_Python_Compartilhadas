from os import system as limp
limp("cls")


def calculadora():
    # Solicitar entradas do usuário
    print("* " + " Testando try e except".center(46, "-") + " *")
    print("* " + " Calculadora Python ".center(46, "-") + " *")
    print("-" * 50)
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")
    operacao = input("Digite a operação (+, -, *, /): ")

    try:
        # Tentar converter os números para float
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        # Se ocorrer ValueError ao tentar converter, imprime mensagem de erro e retorna None
        print("Erro: entradas inválidas.")
        return None

    # Realizar a operação conforme a string fornecida
    try:
        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            if num2 == 0:
                # Tratar caso de divisão por zero
                raise ZeroDivisionError("Erro: divisão por zero.")
            resultado = num1 / num2
        else:
            # Caso a operação não seja uma das esperadas
            print("Erro: operação inválida.")
            return None
        
        # Se tudo ocorrer bem, retorna o resultado
        print(f"Operação realizada com sucesso! Resultado: {resultado}")
        return resultado
    
    except ZeroDivisionError as e:
        # Captura o erro de divisão por zero e imprime a mensagem de erro
        print(e)
        return None

# Chama a função para rodar
calculadora()
