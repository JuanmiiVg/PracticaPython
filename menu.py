def mostrar_menu():
    while True:
        print("Menú:")
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
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            print(f"El resultado de la suma es: {sumar(num1, num2)}")
        
        elif opcion == "2":
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            print(f"El resultado de la resta es: {restar(num1, num2)}")
        
        elif opcion == "3":
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            print(f"El resultado de la multiplicación es: {multiplicar(num1, num2)}")
        
        elif opcion == "4":
            try:
                num1 = float(input("Introduce el primer número: "))
                num2 = float(input("Introduce el segundo número: "))
                print(f"El resultado de la división es: {dividir(num1, num2)}")
            except ZeroDivisionError:
                print("Error: No se puede dividir por cero.")
            except ValueError:
                print("Error: Ambos valores deben ser números.")
        
        elif opcion == "5":
            try:
                num = int(input("Introduce un número para calcular el factorial: "))
                print(f"El factorial (iterativo) de {num} es: {factorial_iterativo(num)}")
            except ValueError as e:
                print(e)
           	 
    	elif opcion == "6":
        	try:
            	num = int(input("Introduce un número para calcular el factorial: "))
            	print(f"El factorial (recursivo) de {num} es: {factorial_recursivo(num)}")
        	except ValueError as e:
            	print(e)
        elif opcion == "7": 
            try: num = int(input("Introduce el índice de Fibonacci: ")) 
                print(f"El {num}-ésimo número de Fibonacci es: {fibonacci_iterativo(num)}") 
            except ValueError as e: print("Error:", e)
        elif opcion == "8":
                print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")