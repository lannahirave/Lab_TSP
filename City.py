import math


class City:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def distance(self, city):
        x_diff = abs(self.x - city.x)
        y_diff = abs(self.y - city.y)
        distance = math.sqrt((x_diff ** 2) + (y_diff ** 2))
        return distance


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
    return math.sqrt((city1.x - city2.x)**2 + (city1.y - city2.y)**2)


def calculate_total_distance(cities, path):
    total_distance = 0
    for i in range(len(path)):
        total_distance += calculate_distance(cities[path[i]], cities[path[(i + 1) % len(path)]])
    return total_distance