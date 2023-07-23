import requests


def parsing(link):
    num_astronauts = 0
    try:
        r = requests.get(link, auth=("user", "pass"))
        num_astronauts = len(r.json()["people"])
    except Exception as ex:
        print(ex)
    return num_astronauts
