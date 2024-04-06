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
    for i in range(len(path) - 1):
        city1 = cities[path[i] - 1]
        city2 = cities[path[i + 1] - 1]
        total_distance += calculate_distance(city1, city2)
    total_distance += calculate_distance(cities[path[-1] - 1], cities[path[0] - 1])
    return total_distance


def read_atsp_from_file(file_path, num_values_per_row):
    matrix = []
    with open(file_path, 'r') as file:
        for _ in range(7):
            next(file)

        numbers = []
        for line in file:
            if line.strip() == "EOF":
                break

            parts = line.split()
            for part in parts:
                numbers.append(int(part))

    for i in range(0, len(numbers), num_values_per_row):
        matrix.append(numbers[i:i + num_values_per_row])

    # check that diagonal is > 10000
    for i in range(len(matrix)):
        if matrix[i][i] < 1000000 and matrix[i][i] != 0:
            raise Exception("Invalid matrix")

    return matrix


def calculate_total_distance_from_matrix(distance_matrix, path):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distance_matrix[path[i] - 1][path[i + 1] - 1]
    total_distance += distance_matrix[path[-1] - 1][path[0] - 1]
    return total_distance


def generate_random_path(cities):
    path = list(range(1, len(cities)+1))
    shuffle(path)
    return path

