from user import User

class Alumno(User):

    def __init__(self, nombre, turno, correo):
        super().__init__()
        self.turno = turno
        self.nota = 0

    def __str__(self):
        buffer = []
        buffer.append(f"Alumno: {self.nombre.ljust(8)}\n")
        buffer.append(f" Turno: {self.turno}\n")
        buffer.append(f"  Nota: {round(self.nota, 2)}")

        return "".join(buffer)

    def setNota(self, nota):
        self.nota = nota
        

    def convocar_examen(self):
        if self.nota >= 5:
            print(f"{self.correo}")
            print(f"    Estimado/a {self.nombre}, su nota media ha sido un {round(self.nota, 2)}")
