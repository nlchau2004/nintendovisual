'''
This program loads a json file stored within a
text file and creates a nested list of data
based on the type of data

Author: Nathan Chau
Date: 3/5/2023
'''
import json
import urllib.request


headers = {
    'User-Agent':
    "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"
          }


def generate_pokemon_data(data_file: str):
    '''Creates a sorted nested list that counts
    the amount of pokemon within a type
    (Dual-type Pokemon count for each type)
    '''
    poke_types = [
                 ['bug', 0], ['dragon', 0],
                 ['electric', 0], ['fighting', 0],
                 ['fire', 0], ['flying', 0],
                 ['ghost', 0], ['grass', 0],
                 ['ground', 0], ['ice', 0],
                 ['normal', 0], ['poison', 0],
                 ['psychic', 0], ['rock', 0],
                 ['water', 0], ['fairy', 0]
                 ]

    with open(data_file, 'r', encoding='UTF-8') as file:
        data = json.load(file)

    for pokemon in data['results']:
        request = urllib.request.Request(pokemon['url'], headers=headers)
        with urllib.request.urlopen(request) as response:
            pokemon_data_types = response.read()
            pokemon_types = json.loads(pokemon_data_types)
        for pokemon_type in pokemon_types['types']:
            for i in poke_types:
                if pokemon_type['type']['name'] in i:
                    i[1] += 1

    poke_types.sort(key=lambda x: x[1])
    return poke_types


def generate_smash_data(data_file: str):
    '''This function first determines the series
    within Smash.

    Then it counts the amount of characters that
    originate from a series and returns a sorted
    nested list
    '''
    smash_series = set()
    num_of_char_per_series = []

    with open(data_file, 'r', encoding='UTF-8') as file:
        data = json.load(file)

    for character in data:
        smash_series.add(character['series']['name'])

    for series in list(smash_series):
        num_of_char_per_series.append([series, 0])

    for character in data:
        for series in num_of_char_per_series:
            if character['series']['name'] in series:
                series[1] += 1

    num_of_char_per_series.sort(key=lambda x: x[1])
    return num_of_char_per_series
