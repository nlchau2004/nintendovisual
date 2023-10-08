'''
This module takes in data created by fileio.py
and creates a graph based on that data.

The end result is a horizontal bar graph.

Author: Nathan Chau
Date: 3/5/2023
'''
import matplotlib.pyplot as plt


def create_titles(option):
    '''Returns a tuple of variables to be
    used for labeling the graph
    '''
    assert option in ('Pokemon', 'Smash'), 'Invalid option!'
    if option == 'Pokemon':
        title = 'Number of Pokemon for each type (Gen 1)'
        y_axis = 'Types'
        x_axis = 'Number of Pokemon'
    elif option == 'Smash':
        title = 'Number of Smash Characters in a Series'
        y_axis = 'Series'
        x_axis = 'Number of Smash Characters'

    return title, y_axis, x_axis


def create_graph(given_data, titles):
    '''Creates a graph through given data and
    titles
    '''
    nums = []
    cols = []
    for data in given_data:
        nums.append(data[0])
        cols.append(data[1])

    plt.barh(nums, cols)
    plt.title(titles[0])
    plt.ylabel(titles[1])
    plt.xlabel(titles[2])

    plt.show()
