'''
This module utilizes APIs to gather data that is used for
creating graphs

Author: Nathan Chau
Date: 3/5/2023
'''
import json
import urllib.request


headers = {
    'User-Agent':
    "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"
          }


def get_pokemon(file: str):
    '''Gathers the data of the original 151
    Pokemon and saves into a file
    '''
    request = urllib.request.Request(
        'https://pokeapi.co/api/v2/pokemon?limit=151',
        headers=headers
                                    )
    with urllib.request.urlopen(request) as response:
        data = response.read()
        pokemon = json.loads(data)
    with open(file, 'w', encoding='UTF-8') as data_file:
        json.dump(pokemon, data_file)


def get_smash_chars(file: str):
    '''Gathers the data of characters from
    Smash Ultimate and saves into a file
    '''
    request = urllib.request.Request(
        'https://smashbros-unofficial-api.vercel.app/api/v1/ultimate' +
        '/characters',
        headers=headers
                                    )
    with urllib.request.urlopen(request) as response:
        data = response.read()
        characters = json.loads(data)
    with open(file, 'w', encoding='UTF-8') as data_file:
        json.dump(characters, data_file)
