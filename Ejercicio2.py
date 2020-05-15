print("Elige tu propio camino")

inicio = input("Escribe empezar para comenzar el programa: ")
inicio = ""


while(inicio != 'empezar'):
    print("Debes ingresar la palabra empezar para iniciar el programa")


while(inicio == 'empezar'):
    print("""¿Que camino queres elegir?
        Escribi la opcion deseada con un numero

        1- Quiero saludar
        2- Quiero multiplicar
        3- Quiero salir del programa    """)
    opcion = input("Ingresa una opcion: ")
    if opcion == '1':
        print("Hola como estas")
    elif opcion == '2':
        numero1 = float(input("Introduce un valor a multiplicar: "))
        numero2 = float(input("Introduce un valor a multiplicar: "))
        print("El resultado es: ", numero1 * numero2)
    elif opcion == '3':
        print("Excelente decision")
        break