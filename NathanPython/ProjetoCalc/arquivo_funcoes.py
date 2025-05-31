import math

def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return "Erro: Divisão por zero não permitida."
    return num1 / num2

def exponenciacao(num1, num2):
    return num1 ** num2

def raiz(num1):
    if num1 < 0:
        return "Erro: Não é possível calcular a raiz quadrada de um número negativo."
    return math.sqrt(num1)

def seno(num1):
    return math.sin(math.radians(num1))

def cosseno(num1):
    return math.cos(math.radians(num1))
