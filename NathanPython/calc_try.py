from os import system as limp
limp("cls")


def calculadora():
    print("-" * 50)
    print("* " + " Testando try e except".center(46, "-") + " *")
    print("* " + " Calculadora Python ".center(46, "-") + " *")
    print("-" * 50)

    
    num1 = input("Digite o primeiro número: ")
    num2 = input("Digite o segundo número: ")
    operacao = input("Digite a operação (+, -, *, /): ")

    try:
         
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        
        print("Erro: entradas inválidas.")
        return None

    
    try:
        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            if num2 == 0:
                
                raise ZeroDivisionError("Erro: divisão por zero.")
            resultado = num1 / num2
        else:
            
            print("Erro: operação inválida.")
            return None
        
        
        print("* " + f"Operação realizada com sucesso! Resultado: {resultado}".ljust(46) + " *")
        return resultado
    
    except ZeroDivisionError as e:
        
        print(e)
        return None


calculadora()



