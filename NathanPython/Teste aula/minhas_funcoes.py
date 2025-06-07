def somar(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("O primeiro argumento deve ser um número")
        
    return a + b


def subtrair(a, b):
    return a - b
