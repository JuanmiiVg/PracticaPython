def mostrar_menu():
    print("Menú de opciones")
    print("1- Sumar")
    print("2- Restar")
    print("3- Multiplicar")
    print("4- Dividir")
    print("5- Salir")
    print("6- Calcular el factorial de un número (Iterativo)") 

    opcion = int(input("Elige una opción: "))
    if opcion == 1:
        a = float(input("Introduce el primer número: "))
        b = float(input("Introduce el segundo número: "))
        print(sumar(a, b))
    elif opcion == 2:
        a = float(input("Introduce el primer número: "))
        b = float(input("Introduce el segundo número: "))
        print(restar(a, b))
    elif opcion == 3:
        a = float(input("Introduce el primer número: "))
        b = float(input("Introduce el segundo número: "))
        print(multiplicar(a, b))
    elif opcion == "4":
            try:
                num1 = float(input("Introduce el primer número: "))
                num2 = float(input("Introduce el segundo número: "))
                resultado = dividir(num1, num2)
                print(f"El resultado de la división es: {resultado}")
            except ZeroDivisionError:
                print("Error: No se puede dividir por cero.")
            except ValueError:
                print("Error: Ambos valores deben ser números.")
    elif opcion == 5:
        print("Saliendo del programa.")

       