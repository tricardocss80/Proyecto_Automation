ford = 100000
chevrolet = 120000
fiat = 80000

p2 = 50000
p4 = 65000
p5 = 78000

blanco = 10000
azul = 20000
negro = 30000

cont = 0

hay_cliente = 'si'


def marca_input():
    marca = ""
    while marca != "ford" and marca != "chevrolet" and marca != "fiat":
        marca = input("Ingrese por favor la marca de su nuevo auto: ")
        if marca != "ford" and marca != "chevrole" and marca != "fiat":
            print("Debe elegir una marca disponible")
    return marca


def puertas_input():
    puertas = ""
    while puertas != '2' and puertas != '4' and puertas != '5':
        puertas = input("Ingrese por favor la cantidad de puertas de su nuevo auto: ")
        if puertas != '2' and puertas != '4' and puertas != '5':
            print("Debe elegir la cantidad de puertas disponible")
    return puertas


def color_input():
    color = ""
    while color != 'blanco' and color != 'azul' and color != 'negro':
        color = input("Ingrese por favor el color de su nuevo auto: ")
        if color != 'blanco' and color != 'azul' and color != 'negro':
            print("Debe elegir un color disponible")
    return color


def precio_marcas(marca):
    if marca == "ford":
        return ford
    elif marca == "chevrolet":
        return chevrolet
    elif marca == "fiat":
        return fiat


def precio_puertas(puertas):
    if puertas == '2':
        return p2
    elif puertas == '4':
        return p4
    elif puertas == '5':
        return p5


def precio_color(color):
    if color == "blanco":
        return blanco
    elif color == "azul":
        return azul
    elif color == "negro":
        return negro



def pregunta(texto, opciones):
    seleccionado = ""
    while opciones.index(seleccionado):
        seleccionado = input(texto)
        if opciones.index(seleccionado):
            print("Debe elegir la opcion correcta")
    return marca


while hay_cliente == 'si':
    cont = cont + 1
    print('Cliente Nº ' + str(cont))

    nombre = input("Ingrese por favor su nombre: ")
    apellido = input("Ingrese por favor su apellido: ")

    marca = marca_input
    puertas = puertas_input()
    color = color_input()
    precio = precio_marcas(marca) + precio_puertas(puertas) + precio_color(color)

