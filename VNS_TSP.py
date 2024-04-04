from City import *
import time
from plotter import plot_tour
import random


def two_opt(path, i, k):
    new_path = path[0:i]
    new_path.extend(reversed(path[i:k + 1]))
    new_path.extend(path[k + 1:])
    return new_path


def local_search(cities, path):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(path) - 2):
            for k in range(i + 1, len(path)):
                new_path = two_opt(path, i, k)
                new_distance = calculate_total_distance(cities, new_path)
                if new_distance < calculate_total_distance(cities, path):
                    path = new_path
                    improved = True
                    break
            if improved:
                break
    return path


def shake(path, k):
    for _ in range(k):
        i = random.randint(1, len(path) - 1)
        j = random.randint(1, len(path) - 1)
        path[i], path[j] = path[j], path[i]
    return path


def vns(cities, max_iterations, max_no_improv, k):
    best_path = generate_random_path(cities)
    best_distance = calculate_total_distance(cities, best_path)

    no_improv = 0
    for i in range(max_iterations):
        if no_improv >= max_no_improv:
            break
        k = 1
        while k <= 3:
            candidate_path = shake(best_path[:], k)
            candidate_path = local_search(cities, candidate_path)
            candidate_distance = calculate_total_distance(cities, candidate_path)
            if candidate_distance < best_distance:
                best_path, best_distance = candidate_path, candidate_distance
                no_improv = 0
                break
            k += 1
        no_improv += 1
    return best_path, best_distance


max_iterations_global = 20
max_no_improve = 100
k = 5

#cities_from_file = read_cities("./EIL76/eil76.tsp")
cities_from_file = read_cities("./BERLIN52/berlin52.tsp")
#cities_from_file = read_cities("./EIL101/eil101.tsp")
time_now = time.time()
best_path_global, best_distance_global = vns(cities_from_file, max_iterations_global, max_no_improve, k)
print("Time taken in seconds:", time.time() - time_now)
print("Best path found:", best_path_global)
print("Total distance:", best_distance_global)

plot_tour(cities_from_file, best_path_global)

