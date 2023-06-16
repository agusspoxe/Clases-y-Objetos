import requests

class Alumno:
    def __init__(self):
        self.datos_persona = self.generar_datos_persona_aleatoria()

    def generar_datos_persona_aleatoria(self):
        r = requests.get("https://randomuser.me/api/")
        data = r.json()
        results = data["results"]
        if results:
            person = results[0]
            datos = {
                "nombre": person["name"]["first"],
                "apellido": person["name"]["last"],
                "correo": person["email"],
                "pais": person["location"]["country"]
            }
            return datos
        else:
            return None

    def obtener_datos_persona(self):
        return self.datos_persona

persona = Alumno()

datos_persona = persona.obtener_datos_persona()

if datos_persona:
    print("Datos de persona aleatoria generados:")
    print("Nombre:", datos_persona["nombre"])
    print("Apellido:", datos_persona["apellido"])
    print("Correo electrónico:", datos_persona["correo"])
    print("País:", datos_persona["pais"])
else:
    print("No se pudieron generar los datos de persona aleatoria.")


# import requests

# def __init__(self):
#     self.alumnos =

# def generate_name_and_email():
#     uri = 'https://randomuser.me/api/?results=10'
#     r = requests.get(uri)
#     randomuser = r.json()
#     user = randomuser["results"][0]
#     my_user_data = {
#         "nombre": f'{user["name"]["first"]} {user["name"]["last"]}',
#         "correo": user["email"]
#     }

#     return [my_user_data]

# def main():
#     my_user = generate_name_and_email()[0]
#     print(f"NOMBRE: {my_user['nombre']}")
#     print(f"CORREO: {my_user['correo']}")

# if __name__ == "__main__":
#     main()





# recuerda instalar la libreria
#     Win: pip install requests
#     Mac: pip3 install requests

# def get_json_from(uri):
#     r = requests.get(uri)
#     # print(r.status_code)
#     # print(r.headers['content-type'])
#     # print(r.encoding)
#     # print(r.text)
#     # print(r.json())

#     return r.json()

# def pretty(d, indent=0):
#     for key, value in d.items():
#         print('  ' * indent + str(key))
#         if isinstance(value, dict):
#             pretty(value, indent+1)
#         else:
#             print('\t' * (indent+1) + str(value))

# def main():
#     results = "1"  # input("Cuantos quieres? ")
#     uri = f'https://randomuser.me/api/?results=1{results}'
#     dict = get_json_from(uri)

#     for user in dict["results"]:
#         pretty(user)

# # Viejo request: No funciona a la priemra en windows:

# import json
# import urllib.request

# def get_json_from(uri):
#     urlopenRet = urllib.request.urlopen(urlData)
#     data = urlopenRet.read()
#     encoding = urlopenRet.info().get_content_charset('utf-8')
#     JSON_object = json.loads(data.decode(encoding))

#     return JSON_object