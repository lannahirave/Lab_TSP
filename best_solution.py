import plotter
from City import *


def read_tour_file(file_path):
    tour = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.startswith('EOF'):
                break
            elif line.strip().isdigit():
                tour.append(int(line.strip()))
    return tour


# cities_from_file = read_cities("BERLIN52/berlin52.tsp")
# cities_from_file = read_cities("./EIL76/eil76.tsp")
cities_from_file = read_cities("./EIL101/eil101.tsp")
#file_path = "BERLIN52/berlin52.opt.tour"
#file_path = "EIL76/eil76.opt.tour"
file_path = "EIL101/eil101.opt.tour"

tour_sequence = read_tour_file(file_path)
print("Tour sequence:", tour_sequence)
print("Total distance:", calculate_total_distance(cities_from_file, tour_sequence))
plotter.plot_tour(cities_from_file, tour_sequence)
