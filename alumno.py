from request_example import generate_name_and_email

class Alumno:

    def __init__(self):        
        dict = generate_name_and_email()
        self.turno = "A"
        self.nombre = dict["fullname"]
        self.correo = dict["correo"]
        self.nota = None

    def __str__(self):
        buffer = []
        buffer.append(f"NOMBRE: {self.nombre}") #traer return de request?
        buffer.append(f" Turno: {self.turno}\n")
        buffer.append(f"  Nota: {self.nota}")

        return "".join(buffer)

    def setNota(self, nota):
        self.nota = nota

    def convocar_examen(self, turno):
        if self.nota >= 5 and turno == self.turno:
            print(f"{self.correo}")
            print(f"    Estimado/a {self.nombre}, su nota media ha sido un {self.nota} ha sivo vd convocado al blablabla")


if __name__ == "__main__":
    print(Alumno())
