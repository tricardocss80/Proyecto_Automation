
#*Marca / *Puertas / *Color
# Marcas posibles y sus precios: -Ford $100000 / -Chevrolet: $120000 / -Fiat: $80000
# -Por la cantidad de puertas se añade un precio: -2: $50000 / -4: $65000 / -5: $78000
#Dependiendo del color, se deben sumar: -Blanco: $10000 / -Azul: $20000 / -Negro: $30000
# Deben imprimirse los datos de cada compra y el precio total.


for i in range(5):
    precio = 0
    nombre = input("Ingrese por favor su nombre: ")
    apellido = input("Ingrese por favor su apellido: ")

    marca = input("Ingrese por favor la marca de su nuevo auto: ")
    if marca == 'Ford':
        precio = precio + 100000
    elif marca == 'Chevrolet':
        precio = precio + 120000
    elif marca == 'Fiat':
        precio = precio + 80000

    puertas = input("Ingrese por favor la cantidad de puertas de su nuevo auto: ")
    if puertas == '2':
        precio = precio + 50000
    elif puertas == '4':
        precio = precio + 65000
    elif puertas == '5':
        precio = precio + 78000

    color = input("Ingrese por favor el color de su nuevo auto: ")
    if color == 'blanco':
        precio = precio + 10000
    elif color == 'azul':
        precio = precio + 20000
    elif color == 'negro':
        precio = precio + 30000
    print("El señor " + nombre + " " + apellido + " eligio el auto " + marca + " con " + puertas + " puertas, de color " + color + " y su precio es " + str(
            precio))