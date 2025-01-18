import requests
import json

while True:

    poke = input("Which Pokemon to Know About? ")
    req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke.lower()}")

    if req.status_code == 200:
        r_poke = req.json()
        print(f"Name is \t {r_poke['name']}")


        r_w = r_poke['weight']
        weight = int(r_w)/10
        print(f"Pokemon Weight is {weight} kg")
        print(f"Pokemon Species is {r_poke['species']['name']}")
        print("Pokemon Types: ")
        for type in r_poke['types']:
            print(type['type']['name'])
        print("Pokemon Abilties: ")
        for ability in r_poke['abilities']:
            print(ability['ability']['name'])
    else:
        print("Pokemon not found")
    Search_again = input("Search again y/n?")
    if Search_again != 'y':
        break