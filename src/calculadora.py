def soma(a, b):
    """Retorna a soma de a e b."""
    return a + b

def subtracao(a, b):
    """Retorna a subtração de a e b."""
    return a - b

def multiplicacao(a, b):
    """Retorna a multiplicação de a e b."""
    return a * b

def divisao(a, b):
    """Retorna a divisão de a por b. Levanta erro se divisão por zero."""
    if b == 0:
        raise ValueError("Não é possível dividir por zero.")
    return a / b
