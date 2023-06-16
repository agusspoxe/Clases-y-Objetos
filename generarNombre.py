import requests

class GenerarNombre:
    def __init__(self):
        my_user_data = self.generate_name_and_email()
        self.nombre = my_user_data["nombre"]
        self.correo = my_user_data["correo"]

    def get_nombre(self):
        return self.nombre

    def get_correo(self):
        return self.correo

    def generate_name_and_email(self):
        uri = 'https://randomuser.me/api/?results=1'
        r = requests.get(uri)
        randomuser = r.json()
        user = randomuser["results"][0]
        return {
        "nombre": f'{user["name"]["first"]} {user["name"]["last"]}',
        "correo": user["email"]
        }

if __name__ == "__main__":
    gen = GenerarNombre()
    my_user_data = gen.generate_name_and_email()
    print(my_user_data["nombre"])
    print(my_user_data["correo"])