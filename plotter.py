import matplotlib.pyplot as plt
from itertools import permutations, combinations
from random import shuffle
import random
import numpy as np
import statistics
import pandas as pd
import seaborn as sns


def plot_tour(cities, path):
    # Convert the list of City objects into a dictionary for easy lookup
    city_dict = {city.name: (city.x, city.y) for city in cities}

    # Find the coordinates for each city name in the path
    path_coords = [city_dict[city_name] for city_name in path if city_name in city_dict]

    # Unpack the coordinates into two lists: one for x and one for y
    xs, ys = zip(*path_coords)

    # Plot the tour
    plt.figure(figsize=(10, 6))  # Set the figure size
    plt.plot(xs, ys, '-o')  # Plot the path as lines connecting dots

    # Optionally, plot the city names
    for city_name in path:
        if city_name in city_dict:
            x, y = city_dict[city_name]
            plt.text(x, y, city_name)

    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Tour Plot')
    plt.show()
