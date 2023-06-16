from alumno import Alumno
from aula import Aula
from profesor import Profesor

aulas =[Aula(Profesor("Manolo Gutierrez", 0, 9)),
        Aula(Profesor("Fernando Sanchez", 3, 6)),
        Aula(Profesor("Paula Tejero", 2, 7)),
        Aula(Profesor("Alicia Pomares", 1, 8)),
        Aula(Profesor("Alejandro SantaMaria", 2, 10))
        ]
CANTIDAD = {
    "alumnos" : 5
}

for i in range(CANTIDAD["alumnos"]):
    aulas[i % len(aulas)].add(Alumno())
contador = 0
for aula in range(len(aulas)):
    try:
        aulas[contador].puntuar()
        aulas[contador].convocar_examen()
        contador += 1
    except Exception as e:
        print(e)


# CANT_AULAS = 5

# aulas = []
# for i in range(CANT_AULAS):
#     aulas.append(Aula())

# profesores = [
#     Profesor("Carlos", 0, 10),
#     Profesor("Andres", 0, 10),
#     Profesor("Agustin", 0, 10)
# ]

# alumnos = [
#     Alumno("Jesus", "A", "jesussampayo@gmail.com"),
#     Alumno("Alejandro", "A", "alejandromartin@gmail.com"),
#     Alumno("Paula", "A", "paularivero@gmail.com"),
#     Alumno("Alenjandra", "A", "malejandracalderon@gmail.com"),
#     Alumno("Manuel", "A", "manuelvalverdeo@gmail.com"),
#     Alumno("Ines", "A", "inesbarajas@gmail.com"),
#     Alumno("Sharay", "A", "sharaymoreno@gmail.com"),
#     Alumno("Alonso", "A", "alonsogarcia@gmail.com"),
#     Alumno("Alba", "A", "albamaria@gmail.com"),
#     Alumno("Kevin", "A", "kevinfernandez@gmail.com"),
#     Alumno("Matias", "A", "matiasaldas@gmail.com"),
#     Alumno("Alberto", "A", "albertomolina@gmail.com"),
#     Alumno("Lucia", "A", "luciasanchez@gmail.com")
# ]

# aulas[0].set_profesor(profesores[0])
# aulas[1].set_profesor(profesores[1])
# aulas[2].set_profesor(profesores[2])
# aulas[4].set_profesor(profesores[0])

# contador = 0
# while contador < len(alumnos):
#     aulas[contador % (len(aulas) - 1)].add(alumnos[contador])
#     contador += 1

# contador = 0
# for aula in aulas:
#     print(f"AULA {contador} ----------------------------- ")

#     try:
#         aula.puntuar()
#     except Exception as e:
#         print(e)

#     try:
#         aula.convocar_examen("A")
#     except Exception as e:
#         aula.listar()
#         print(e)

#     print("\n" * 3)
#     contador += 1