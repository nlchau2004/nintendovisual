'''
This module acts as the main file and includes
the interactive section of Workout Project 4.

Author: Nathan Chau
Date: 3/5/2023
'''
import sys
import apis
import graph
import fileio


def create_data():
    '''Scrapes data from both PokeAPI
    and Unofficial Smash Ultimate API
    '''
    print('Generating data...')
    apis.get_pokemon('pokemon.txt')
    apis.get_smash_chars('smash.txt')


def main():
    '''This function acts as the UI for
    the program.

    It will prompt the user for which API
    they would like to graph.

    They may continue to do so until typing
    'Quit.'
    '''
    create_data()

    while True:
        try:
            print('Hello there! What would you like to graph?')
            user_input = input('Pokemon\nSmash\nQuit\n')

            if user_input == 'Quit':
                sys.exit()
            if user_input == 'Pokemon':
                data = fileio.generate_pokemon_data('pokemon.txt')
            elif user_input == 'Smash':
                data = fileio.generate_smash_data('smash.txt')

            print('Creating graph...')
            titles = graph.create_titles(user_input)
            graph.create_graph(data, titles)
        except AssertionError as ex:
            print(ex)


if __name__ == '__main__':
    main()
