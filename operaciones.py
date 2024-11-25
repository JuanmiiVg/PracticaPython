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

# Crear función dividir
def dividir(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Ambos valores deben ser int o float")
    if b == 0:
        raise ValueError("El divisor no puede ser cero")
    resultado = 0
    while a >= b:
        a -= b
        resultado += 1
    return resultado

# factorial_iterativo.py
def factorial_iterativo(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("El número debe ser un entero positivo.")
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


# factorial_recursivo.py
def factorial_recursivo(n):
	if not isinstance(n, int) or n < 0:
    	raise ValueError("El número debe ser un entero positivo.")
	if n == 0 or n == 1:
    	return 1
	return n * factorial_recursivo(n - 1)
        
# fibonacci.py
def fibonacci_iterativo(n):
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