import random
class Alumno:
    def __init__(self, nombre, turno, correo):
        self.nombre = nombre
        self.turno = turno
        self.correo = correo
        self.nota = 0

    def set_nota(self, nota):
        self.nota = nota

    def describe(self):
        print((f"Alumno/a {self.nombre} del turno {self.turno} con la nota nota:{self.nota}"))
        
    def convocar_examen(self):
        if self.nota <= 5:   
            print(f"{self.nombre} tienes que ir al examen del 23 de julio de 2023")

class Aula:
    def __init__(self):
        self.alumnos = []
    
    def add(self, alumno : Alumno):
        self.alumnos.append(alumno)
    
    def listar(self):
        for alumno in self.alumnos:
            alumno.set_nota(random.randrange(0, 10))
            alumno.describe()
            
    def tos_palexamen(self):
        for alumno in self.alumnos:
            alumno.convocar_examen()
 

aula1 = Aula()
aula1.add(Alumno("juan", "A", "Juan@correo.com"))
aula1.add(Alumno("brand", "c", "brand@correo.com"))
aula1.add(Alumno("tiryon", "A", "tiryon@correo.com"))
aula1.add(Alumno("cersey", "b", "cersey@correo.com"))
aula1.add(Alumno("arya", "b", "arya@correo.com"))
aula1.add(Alumno("jhon", "c", "jhon@correo.com"))

aula1.listar()
aula1.tos_palexamen()

