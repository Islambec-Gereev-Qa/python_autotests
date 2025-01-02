import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'USER_TOKEN'
TRAINER_ID = '14537'
HEADER = {'Content-Type': 'application/json',
          'trainer_token': TOKEN
}

def test_get_list_trainers_status_code_200():
    response_code = requests.get(url = f'{URL}/trainers', headers = HEADER, params = {'trainer_id' : TRAINER_ID})
    assert response_code.status_code == 200

def test_string_my_trainer_name():
    response_name = requests.get(url = f'{URL}/trainers', headers = HEADER, params = {'trainer_id' : TRAINER_ID})
    assert response_name.json()["data"][0]["trainer_name"] == 'АферисТ'