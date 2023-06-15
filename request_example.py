import requests

def generate_name_and_email():
    uri = f'https://randomuser.me/api/?results=1'
    r = requests.get(uri)
    randomuser = r.json()
    user = randomuser["results"][0]
    my_user_data = {
        "fullname": f'{user["name"]["first"]} {user["name"]["last"]}',
        "correo": user["email"]
    }

    return my_user_data


def main():
    my_user = generate_name_and_email()[0]
    print(f"NOMBRE: {my_user['nombre']}")
    print(f"CORREO: {my_user['correo']}")

if __name__ == "__main__":
    main()