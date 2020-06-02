programa = True
usuario = 0
lista = []

while programa == True:
    usuario = usuario + 1
    print('Usuario Nª: ' + str(usuario))

    nombre = input('tu nombre: ')
    apellido = input('tu apellido: ')
    telefono = input('tu telefono: ')

    diccionario = {'usuario': usuario, 'nombre': nombre, 'apellido': apellido, 'telefono': telefono}

    lista.append(diccionario)

    print(lista)
