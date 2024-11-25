# menu.py
from operaciones import (
    sumar, restar, multiplicar, dividir,
    factorial_iterativo, factorial_recursivo,
    fibonacci_iterativo
)

def mostrar_menu():
    while True:
        print("\nMenú:")
        print("1- Sumar")
        print("2- Restar")
        print("3- Multiplicar")
        print("4- Dividir")
        print("5- Factorial (Iterativo)")
        print("6- Factorial (Recursivo)")
        print("7- Fibonacci")
        print("8- Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            try:
                num1 = float(input("Introduce el primer número: "))
                num2 = float(input("Introduce el segundo número: "))
                resultado = sumar(num1, num2)
                print(f"El resultado de la suma es: {resultado}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif opcion == "2":
            try:
                num1 = float(input("Introduce el primer número: "))
                num2 = float(input("Introduce el segundo número: "))
                resultado = restar(num1, num2)
                print(f"El resultado de la resta es: {resultado}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif opcion == "3":
            try:
                num1 = float(input("Introduce el primer número: "))
                num2 = float(input("Introduce el segundo número: "))
                resultado = multiplicar(num1, num2)
                print(f"El resultado de la multiplicación es: {resultado}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif opcion == "4":
            try:
                num1 = float(input("Introduce el primer número: "))
                num2 = float(input("Introduce el segundo número: "))
                resultado = dividir(num1, num2)
                print(f"El resultado de la división es: {resultado}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif opcion == "5":
            try:
                num = int(input("Introduce un número para calcular el factorial (Iterativo): "))
                resultado = factorial_iterativo(num)
                print(f"El factorial (iterativo) de {num} es: {resultado}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif opcion == "6":
            try:
                num = int(input("Introduce un número para calcular el factorial (Recursivo): "))
                resultado = factorial_recursivo(num)
                print(f"El factorial (recursivo) de {num} es: {resultado}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif opcion == "7":
            try:
                num = int(input("Introduce el índice de Fibonacci: "))
                resultado = fibonacci_iterativo(num)
                print(f"El {num}-ésimo número de Fibonacci es: {resultado}")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Intenta de nuevo.")
