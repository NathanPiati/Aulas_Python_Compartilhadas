import math

def soma(num1, num2):
    """Soma dois números"""
    return num1 + num2

def subtracao(num1, num2):
    """Subtrai o segundo número do primeiro"""
    return num1 - num2

def multiplicacao(num1, num2):
    """Multiplica dois números"""
    return num1 * num2

def divisao(num1, num2):
    """Divide o primeiro número pelo segundo. Verifica divisão por zero"""
    if num2 == 0:
        return "Erro: Divisão por zero não permitida."
    return num1 / num2

def exponenciacao(num1, num2):
    """Calcula a exponenciação (num1 elevado a num2)"""
    return num1 ** num2

def raiz(num1):
    """Calcula a raiz quadrada de um número. Verifica números negativos"""
    if num1 < 0:
        return "Erro: Não é possível calcular a raiz quadrada de um número negativo."
    return math.sqrt(num1)

def seno(num1):
    """Calcula o seno de um número (em graus)"""
    return math.sin(math.radians(num1))

def cosseno(num1):
    """Calcula o cosseno de um número (em graus)"""
    return math.cos(math.radians(num1))
