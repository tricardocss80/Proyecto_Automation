# Una escuela tiene alumnos, cuyas características son:
# *Nombre
# *Apellido
# *Nota Matematica
# *Nota Lengua
# *Nota geografía
# *Promedio

# -Los alumnos pueden dar exámenes.
# La escuela también tiene profesores que tienen las siguientes características:
# *Nombre
# *Apellido
# *Materia que enseña

# -Los profesores toman exámenes y le dan al alumno una nota.
# Se deben cargar distintos alumnos y profesores, que los alumnos den exámenes que toman los profesores y que el
# resultado sea una nota. El alumno siempre debe tener un promedio (al principio las tres notas son 0).

alumno = []

#def promedio(n_mate, n_lengua, n_geo):
#    return(n_mate + n_lengua + n_geo) / 3

class Escuela():
    def __init__(self,nombre,apellido,materia):
        self.nombre = nombre
        self.apellido = apellido
        self.materia = materia

    def mostrar(self):
        return self.nombre, self.apellido, self.materia




class Alumnos():
    def __init__(self, nombre, apellido):
        super.  self.nombre = nombre
        self.apellido = apellido
        self.n_mate = 0
        self.n_lengua = 0
        self.n_geo = 0


alumnos = Alumnos()