#Sacar promedio
def promedio(mate,lite,fisi):
    return (mate+lite+fisi)/3

#Ingreso de datos
def datos_del_alumno(nombre,apellido,prom):
    print("El alumno "+nombre+""+apellido+"tiene como promedio: "+str(prom))

#Ver aprovacion de alumno:
def estado_aprobacion(prom):
    if prom >= 6:
        print("Aprobado")
        if prom >= 9:
            print("Alumno destacado")
    elif prom >= 4:
        print("A recuperatorio")
    else:
        print("Insuficiente")

nombre = input("Ingresa tu nombre por favor: ")
apellido = input("Ingresa tu apellido por favor: ")
mate = float(input("Ingresa por favor tu nota de Matematica: "))
lite = float(input("Ingresa por favor tu nota de Literatura: "))
fisi = float(input("Ingresa por favor tu nota de Fisica: "))

prom = promedio(mate,lite,fisi)
datos_del_alumno(nombre,apellido,prom)
estado_aprobacion(prom)