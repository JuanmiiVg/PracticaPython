# operaciones.py

def sumar(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    return "Error: valores no numéricos"

def restar(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a - b
    return "Error: valores no numéricos"

def multiplicar(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        resultado = 0
        for _ in range(abs(b)):
            resultado += abs(a)
        if (a < 0 and b > 0) or (a > 0 and b < 0):
            resultado = -resultado
        return resultado
    return "Error: valores no numéricos"