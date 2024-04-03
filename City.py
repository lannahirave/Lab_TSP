from random import shuffle, uniform
from math import sqrt


class City:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y


def read_cities(file_path):
    cities = []
    with open(file_path, 'r') as file:
        for line in range(6):
            next(file)

        for line in file:
            if line.strip() == "EOF":
                break

            parts = line.split()
            city_name = int(parts[0])
            x = float(parts[1])
            y = float(parts[2])
            cities.append(City(city_name, x, y))

    return cities


def calculate_distance(city1, city2):
    return sqrt((city1.x - city2.x) ** 2 + (city1.y - city2.y) ** 2)


def calculate_total_distance(cities, path):
    total_distance = 0
    for i in range(len(path)):
        total_distance += calculate_distance(cities[path[i]], cities[path[(i + 1) % len(path)]])
    return total_distance


def generate_random_path(cities):
    path = list(range(1, len(cities)))
    shuffle(path)
    path.insert(0, cities[0].name)
    return path

