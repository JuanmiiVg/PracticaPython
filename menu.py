def mostrar_menu():
    print("Menú de opciones")
    print("1- Sumar")
    print("2- Restar")
    print("3- Multiplicar")
    print("4- Dividir")
    print("5- Salir")

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
    elif opcion == 4:
        a = float(input("Introduce el primer número: "))
        b = float(input("Introduce el segundo número: "))
        print(dividir(a, b))
    elif opcion == 5:
        print("Saliendo del programa.")