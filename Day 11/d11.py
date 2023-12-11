import numpy as np
from itertools import combinations
from collections import deque
import math 

def calculate_distance(coord1, coord2):
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])

def expand(galaxy_array):
    rows_to_insert = np.where(np.all(galaxy_array == '.', axis=1))[0]
    cols_to_insert = np.where(np.all(galaxy_array == '.', axis=0))[0]

    for i in rows_to_insert[::-1]:
        galaxy_array = np.insert(galaxy_array, i + 1, '.', axis=0)

    for j in cols_to_insert[::-1]:
        galaxy_array = np.insert(galaxy_array, j + 1, '.', axis=1)

    return galaxy_array
        
def digit_mask(galaxy_array):
    mask = np.where(galaxy_array == "#")

    count = 439
    total_replacements = len(mask[0])
    counts = np.arange(439)

    for i in range(total_replacements):
        row, col = mask[0][i], mask[1][i]
        galaxy_array[row, col] = str(counts[i])
    
    return galaxy_array, count 

def calculate_distance_multiplier(coord1, coord2, empty_rows, empty_cols, multiplier):
    minx, maxx = min(coord1[0], coord2[0]), max(coord1[0], coord2[0])
    miny, maxy = min(coord1[1], coord2[1]), max(coord1[1], coord2[1])

    temp = (maxx - minx) + (maxy - miny)
    temp += multiplier * len([y for y in empty_rows if y > miny and y < maxy])
    temp += multiplier * len([x for x in empty_cols if x > minx and x < maxx])

    return temp

def main():
    file_path = 'd11.txt'

    with open(file_path, 'r') as file:
        lines = [list(line.strip()) for line in file]

    galaxy_array_base = np.array(lines, dtype=str)

    print("Part One Code")
    galaxy_array = expand(galaxy_array_base)
    indices = np.argwhere(galaxy_array == "#")
    positioning = [tuple(index) for index in indices]
    count = len(positioning)
    pairs = list(combinations(positioning, 2))
    distances = {pair: calculate_distance(pair[0], pair[1]) for pair in pairs}
    print(sum(distances.values()))

    print("Part Two Code")
    indices = np.argwhere(galaxy_array_base == "#")
    positioning = [tuple(index) for index in indices]
    pairs = list(combinations(positioning, 2))
    
    empty_row_indexes = [i for i, row in enumerate(galaxy_array_base) if all([galaxy == '.' for galaxy in row])]
    empty_col_indexes = [i for i in range(len(galaxy_array_base[0])) if all([row[i] == '.' for row in galaxy_array_base])]
    
    distances = {pair: calculate_distance_multiplier(pair[0], pair[1], empty_col_indexes, empty_row_indexes, 999999) for pair in pairs}
    print(sum(distances.values()))
    
if __name__ == "__main__":
    main()
