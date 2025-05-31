import math

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b

def exponenciacao(a, b):
    return a ** b

# def raiz(a):
#     if a < 0:
#         return "Erro: Raiz de número negativo"
#     return math.sqrt(a)

def raiz (numero1, numero2):
    res = numero1 ** (1/numero2)
    return res


def seno(a):
    return math.sin(math.radians(a))

def cosseno(a):
    return math.cos(math.radians(a))

def tangente(a):
    angulo = a % 180
    if angulo == 90 or angulo == -90:
        return "Erro: Tangente indefinida"
    return math.tan(math.radians(a))
