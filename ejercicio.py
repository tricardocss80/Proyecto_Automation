#Ingresar el nombre y apellido de un alumno y sus notas de matemática, literatura y física.
#Se pide imprimir el nombre, el apellido y el promedio.
#Si el promedio es mayor a 6 entonces debe aparecer un cartel que diga "Aprobado". Caso contrario, si tiene menos de 4
# puntos imprimir "Insuficiente" y si tiene entre 4 y 5.99999 imprimir "A recuperatorio".
#En caso de tener 9 puntos o más, imprimir (aparte del aprobado) "Alumno destacado".


def promedio_materias(matematicas,literatura,fisica):
    return (matematicas + literatura + fisica)/3

print("Bienvenido al sistema de calificaciones de la escuela")

nombre = input("Ingresa tu nombre por favor: ")
apellido = input("Ingrese tu apellido por favor: ")
print("Como estas: "+nombre, apellido)

matematicas = float(input("Ingresa tu nota de Matematicas por favor: "))

literatura = float(input("Ingresa tu nota de Literatura por favor: "))

fisica = float(input("Ingresa tu nota de Fisica por favor: "))

print("TU INFORME")

promedio = promedio_materias(matematicas,literatura,fisica)
print(promedio)

if promedio > 6:
    print("Aprobado")
    if promedio >= 9:
        print("Alumno destacado")

elif 4 <= promedio <= 5.99999:
    print("A recuperatorio")
else:
    print("Insuficiente")

print("Gracias por utilizar el sistema de promedios de la escuela, que tengas buen dia...")