#listas
autos = ['Ford', 'Chevrolet' , 'Fiat']
print(autos)
print(autos[2])
print(autos[-1])
print(autos[0::2])
autos.append('Dodge')
print(autos)
autos.insert(1,'Ferrari')
print(autos)
del autos[2]
print(autos)
print(len(autos))
autos[2] = 'Porche'
print(autos)
if autos[2] == 'Porche':
    print('Todo bien')
else:
    print('Todo mal')

#tuplas(no se pueden modificar)

colores = ('amarillo','azul','verde')
print(colores)

print('amarillo' in colores)
if 'amarillo' in colores:
    print('El amarillo existe')

#diccionarios

usuario = {id: 1 , 'name': 'Riki', 'age': 37, 'casado': True}
print(usuario['name'])

print(usuario['casado'])

usuario['name'] = 'Nancy Dupla'
print(usuario['name'])

usuario['name'] = 'Nanci Tupla'
print(usuario)

usuario['apellido'] = 'Algo'
print(usuario)

del usuario['apellido']
print(usuario)

print(usuario.keys())
print(usuario.values())
if id(usuario):
    print('Tiene id')

usuario.clear()
print(usuario)

del usuario
print(usuario)
