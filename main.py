from alumno import Alumno
from aula import Aula
from profesor import Profesor

contador_aulas = 5

aulas = []
for i in range(contador_aulas):
    aulas.append(Aula())

profesores = [
    Profesor("Emilio Gutierrez", 0, 10),
    Profesor("Alicia Pomares", 0, 10),
    Profesor("Pilar Prieto", 0, 10),
]

alumnos = [
    Alumno("Andrea", "A", "andrea@gmail.com"),
    Alumno("Lucia", "A", "lucia@gmail.com"),
    Alumno("Cristina", "A", "cristina@gmail.com"),
    Alumno("Javier", "A", "javier@gmail.com"),
    Alumno("Cristian", "A", "cristian@gmail.com"),
    Alumno("Gloria", "A", "gloria@gmail.com"),
    Alumno("Hector", "A", "hector@gmail.com"),
    Alumno("Luis", "A", "luis@gmail.com"),
    Alumno("Yasmina", "A", "yasmina@gmail.com"),
    Alumno("Aroa", "A", "aroa@gmail.com"),
    Alumno("Sergio", "A", "sergio@gmail.com"),
    Alumno("Valeria", "A", "valeria@gmail.com"),
    Alumno("Nagore", "A", "nagore@gmail.com"),
    Alumno("Edurne", "A", "edurne@gmail.com"),
    Alumno("Raul", "A", "raul@gmail.com"),
    Alumno("Angel", "A", "angel@gmail.com"),
    Alumno("Jesus", "A", "jesus@gmail.com")
]

aulas[0].set_profesor(profesores[0])
aulas[1].set_profesor(profesores[1])
aulas[2].set_profesor(profesores[2])
aulas[4].set_profesor(profesores[0])

contador = 0
while contador < len(alumnos):
    aulas[contador % (len(aulas) - 1)].add(alumnos[contador])
    contador += 1

contador = 0
for aula in aulas:
    print(f"AULA {contador} ----------------------------- ")

    try:
        aula.puntuar()
    except Exception as e:
        print(e)

    try:
        aula.convocar_examen()
    except Exception as e:
        aula.listar()
        print(e)

    print("\n" * 3)
    contador += 1