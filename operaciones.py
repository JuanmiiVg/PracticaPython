# operaciones.py

def sumar(a, b):
    """Suma dos números."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Ambos valores deben ser int o float")
    return a + b

def restar(a, b):
    """Resta dos números."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Ambos valores deben ser int o float")
    return a - b

def multiplicar(a, b):
    """Multiplica dos números usando sumas repetidas."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Ambos valores deben ser int o float")
    resultado = 0
    for _ in range(abs(int(b))):
        resultado += a
    return resultado if b >= 0 else -resultado

def dividir(a, b):
    """Divide dos números de manera iterativa sin usar el operador '/'."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Ambos valores deben ser int o float")
    if b == 0:
        raise ValueError("El divisor no puede ser cero")
    resultado = 0
    a_temp = abs(a)
    b_temp = abs(b)
    while a_temp >= b_temp:
        a_temp -= b_temp
        resultado += 1
    resultado = resultado if (a >= 0) == (b >= 0) else -resultado
    return resultado

def factorial_iterativo(n):
    """
    Calcula el n-ésimo número de Fibonacci de forma iterativa.
    :param n: El índice del número de Fibonacci que se quiere calcular.
    :return: El n-ésimo número de Fibonacci.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("El número debe ser un entero no negativo.")
    
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def factorial_recursivo(n):
    """Calcula el factorial de un número de forma recursiva."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("El número debe ser un entero positivo.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursivo(n - 1)

def fibonacci_iterativo(n):
    """Calcula el n-ésimo número de Fibonacci de forma iterativa."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("El número debe ser un entero no negativo.")
    
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
