# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np


def calculate_fuel(crab, position, iscostincreasing):
    if iscostincreasing:
        return abs(crab - position) * (abs(crab - position) + 1) / 2
    else:
        return abs(crab - position)


def align_crabs(position, crabs, iscostincreasing):
    fuel_consumed = 0
    for crab in crabs:
        fuel_consumed += calculate_fuel(crab, position, iscostincreasing)
    return fuel_consumed


def greedy(crabs, iscostincreasing):
    fuel_consumption = None
    position = None
    for x in range(min(crabs), max(crabs)+1):
        aux_fuel_consumption = align_crabs(x, crabs, iscostincreasing)
        if fuel_consumption is None or aux_fuel_consumption < fuel_consumption:
            fuel_consumption = aux_fuel_consumption
            position = x
    return position, fuel_consumption


# The value that occupies the central place in an ordered dataset is the median.
# It will be the point with less cost for the horizontal alignment in part 1
def median(crabs):
    crab_median = np.median(crabs)
    fuel_consumption = align_crabs(crab_median, crabs, False)
    return crab_median, fuel_consumption


def format_input(name):
    with open(name, 'r') as file:
        return [int(x) for x in file.readline().replace('\n', '').split(',')]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    formatted_input = format_input('test_input.txt')
    print(greedy(formatted_input, False))
    print(median(formatted_input))
    print(greedy(formatted_input, True))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
