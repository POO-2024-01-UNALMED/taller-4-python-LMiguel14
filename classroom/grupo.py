from classroom.asignatura import Asignatura         ############## 

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo= "grupo predeterminado", asignaturas=[],  estudiantes = []): #estudiantes con parametro por defecto
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = list(estudiantes)


    def listadoAsignaturas(self, **kwargs):
        for x in kwargs:
            self._asignaturas.append(Asignatura(kwargs[x]))
        

    def agregarAlumno(self, alumno, lista= None):
        if lista is None:
            lista= []
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista
        
    def __str__(self):
        return "Grupo de estudiantes: " + self._grupo
    

    #@ classmethod
    #def asignarNombre(cls, nombre="Grado 10"):
    #    cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    #@ classmethod
    #def asignarNombre(cls, nombre="Grado 4"):

    #    cls.grado = nombre
