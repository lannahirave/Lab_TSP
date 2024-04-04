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


citiesFromFile = read_cities("BERLIN52/berlin52.tsp")
file_path = "BERLIN52/berlin52.opt.tour"

tour_sequence = read_tour_file(file_path)
print("Tour sequence:", tour_sequence)
plotter.plot_tour(citiesFromFile, tour_sequence)
