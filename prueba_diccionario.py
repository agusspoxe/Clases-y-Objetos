import requests
# recuerda instalar la libreria
#     Win: pip install requests
#     Mac: pip3 install requests

def get_json_from(uri):
    r = requests.get(uri)
    # print(r.status_code)
    # print(r.headers['content-type'])
    # print(r.encoding)
    # print(r.text)
    # print(r.json())

    return r.json()

def pretty(d, indent=0):
    for key, value in d.items():
        print('  ' * indent + str(key))
        if isinstance(value, dict):
            pretty(value, indent+1)
        else:
            print('\t' * (indent+1) + str(value))

def main():
    results = "1"  # input("Cuantos quieres? ")
    uri = f'https://randomuser.me/api/?results={results}'
    dict = get_json_from(uri)

    for user in dict["results"]:
        name = user ["name"]
       
        fullname = f"{user["name"]["first"]}{user["name"]["last"]}
        print(fullname)