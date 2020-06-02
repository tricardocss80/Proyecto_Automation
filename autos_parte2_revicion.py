
def calcular_precio(marca,puerta,color,ventas):
    marcas = {'ford': 100000, 'fiat': 80000, 'chevrolet':120000}
    colores = {'azul': 10000, 'blanco': 20000, 'negro': 30000}
    puertas = {2: 50000, 4: 65000, 5: 78000}
    precio = marcas[marca] + colores[color] + puertas[puerta]
    if ventas > 5 and ventas < 11:
        precio = precio * 0.9
    elif ventas > 10 and ventas < 51:
        precio = precio * 0.85
    elif ventas > 50:
        precio = precio * 0.82
    return precio

mas_clientes = 'si'
ventas = []
marcas = ['ford', 'fiat', 'chevrolet']
puertas = [2, 4, 5]
colores = ['azul', 'blanco', 'negro']


while mas_clientes == 'si':
    nombre = input("Ingrese por favor su nombre: ")
    apellido = input("Ingrese por favor su apellido: ")
    marca = ''
    puerta = 0
    color = ''
    while marca not in marcas:
        marca = input("Ingrese por favor una marca: ")
        marca = marca.lower()
    while puerta not in puertas:
        puerta = int(input('Ingrese por favor el numero de puertas: '))
    while color not in colores:
        color = input('Ingrese por favor un color: ')


    ventas.append({'nombre':nombre, 'apellido':apellido, 'marca': marca, 'puertas':puerta, 'color':color})
    mas_clientes = input('¿Hay mas clientes?')

largo = len(ventas)

for i in ventas:
    precio = calcular_precio(i['marca'],i['puertas'],i['color'],largo)
    print("La persona: " + i['nombre']+ " "+ i['apellido']+" ""compro un auto "+ i['marca'] + " de "
            +str(i['puertas'])+ " puertas y color "+ i['color']+ " con un precio de $" +str(precio))
