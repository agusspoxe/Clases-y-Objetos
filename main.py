from alumno import Alumno
from aula import Aula
from profesor import Profesor

CANT_AULAS = 5
CANT_ALUMNOS = 33

aulas = []
for i in range(CANT_AULAS):
    aulas.append(Aula())

profesores = [
    Profesor("Juanito Balerrama", 0, 10),
    Profesor("Manolito Pomporretas", 0, 10),
    Profesor("Teres Rabal", 0, 10),
]

alumnos = []
for i in range(CANT_ALUMNOS):
    alumnos.append(Alumno())

aulas[0].set_profesor(profesores[0])
aulas[1].set_profesor(profesores[1])
aulas[2].set_profesor(profesores[2])
aulas[4].set_profesor(profesores[0])

contador = 0
while contador < CANT_ALUMNOS:
    aulas[contador % CANT_AULAS - 1].add(alumnos[contador])
    contador += 1

contador = 0
for aula in aulas:
    print("\n" * 1)
    contador += 1    
    print(f"AULA {contador} ----------------------------- ")


    print("PUNTUAR:---------------------------------------")
    try:
        aula.puntuar()
    except Exception as e:
        print(e)

    print("LISTAR:---------------------------------------")
    aula.listar()

    print("CONVOCAR:---------------------------------------")

    try:
        aula.convocar_examen("A")
    except Exception as e:
        print(e)

print()
