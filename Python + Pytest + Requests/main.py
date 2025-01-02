import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'USER_TOKEN'
HEADER = {'Content-Type': 'application/json',
          'trainer_token': TOKEN
}

body_creation = {
    "name": "generate",
    "photo_id": -1
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_creation)
print(response.text)

pokemon_id = response.json()['id']

body_change_name_pokemon = {
    "pokemon_id": pokemon_id,
    "name": "generate"
}

responce_change_name_pokemon = requests.patch(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name_pokemon)
print(responce_change_name_pokemon.text)

body_move_pokemon_in_pokeball = {
    "pokemon_id": pokemon_id
}

responce_move_pokemon_in_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_move_pokemon_in_pokeball)
print(responce_move_pokemon_in_pokeball.text)