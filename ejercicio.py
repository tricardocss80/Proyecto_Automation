
def ingresar_datos():
    nombre = input("Ingrese su nombre por favor: ")
    print("Su nombre es: " +nombre)

    apellido = input("Ingrese su apellido por favor: ")
    print("Su nombre es: " + apellido)

ingresar_datos()

def ingresar_materias():
    matematicas = int(input("Ingrese su nota de Matematicas por favor: "))
    if matematicas <=10:
       print("Usted ingreso : " +str(matematicas))
    else:
        print("Debe ingresar un valor entre 1 y 10")
        return matematicas
