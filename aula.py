import random

class Aula:
    def __init__(self, profesor = None):
        self.alumnos = []
        self.profesor = profesor if profesor is not None else profesor

    def add(self, alumno):
        self.alumnos.append(alumno)

    def listar(self):
        print(f"PROFESOR: {self.profesor}")
        for alumno in self.alumnos:
            print(alumno)

    def convocar_examen(self):
        if not self.profesor:
            raise Exception(f'No se puede convocar un aula sin profesor')

        if len(self.alumnos) <= 0:
            raise Exception(f'No se puede convocar un aula sin alumnos')

        print(f"PROFESOR: {self.profesor}")
        for alumno in self.alumnos:
            alumno.convocar_examen()

    def puntuar(self):
        if not self.profesor:
            raise Exception(f'No se puede puntuar un aula sin profesor')

        if len(self.alumnos) <= 0:
            raise Exception(f'No se puede puntuar un aula sin alumnos')

        for alumno in self.alumnos:
            alumno.setNota(self.profesor.generar_nota())
            print(alumno)

    def set_profesor(self, profesor):
        self.profesor = profesor


# class Aula:
#     def __init__(self):
#         self.alumnos = []
#         self.profesor = None
    
#     def add(self, alumno):
#         self.alumnos.append(alumno)
    
#     def listar(self):
#         print(f"PROFESOR: {self.profesor}")
#         for alumno in self.alumnos:
#             print(alumno)
    
#     def convocar_examen(self, turno):
#         if not self.profesor:
#             raise Exception(f'No se puede convocar un aula sin profesor')

#         if len(self.alumnos) <= 0:
#             raise Exception(f'No se puede convocar un aula sin alumnos')

#         print(f"PROFESOR: {self.profesor}")
#         for alumno in self.alumnos:
#             alumno.convocar_examen(turno)

#     def puntuar(self):
#         if not self.profesor:
#             raise Exception(f'No se puede puntuar un aula sin profesor')

#         if len(self.alumnos) <= 0:
#             raise Exception(f'No se puede puntuar un aula sin alumnos')

#         for alumno in self.alumnos:
#             alumno.setNota(self.profesor.generar_nota())
#             print(alumno)
    
#     def set_profesor(self, profesor):
#         self.profesor = profesor