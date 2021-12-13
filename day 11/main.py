import numpy as np

rowNbr = [-1, -1, 1, 1, -1, 1, 0, 0]
colNbr = [-1, 1, 1, -1, 0, 0, -1, 1]


def is_tile(row, col, height, width):
    return (0 <= row < height) and (0 <= col < width)


def flash_octopus(octopus_field, row, col):
    for k in range(8):
        if is_tile(row + rowNbr[k], col + colNbr[k], len(octopus_field), octopus_field[0].size):
            octopus_field[row + rowNbr[k]][col + colNbr[k]] += 1


def is_flashing(x): return x >= 10


def octopus_step(octopus_field, width, height):
    number_of_flashes = 0
    all_flashed = False
    flashed = np.array([[False for j in range(width)] for i in range(height)])
    # https://stackoverflow.com/questions/17005536/increase-all-of-a-lists-values-by-an-increment
    # list comprehension is faster for smaller sizes of matrix
    # octopus_field = [x + 1 for x in octopus_field]
    # numpy is faster for bigger sizes of matrix
    octopus_field = octopus_field + 1
    octopus_flashing = np.where(is_flashing(octopus_field))
    while octopus_flashing[0].size > 0:
        one_flash = False
        for i in range(octopus_flashing[0].size):
            if not flashed[octopus_flashing[0][i]][octopus_flashing[1][i]]:
                number_of_flashes += 1
                one_flash = True
                flashed[octopus_flashing[0][i]][octopus_flashing[1][i]] = True
                flash_octopus(octopus_field, octopus_flashing[0][i], octopus_flashing[1][i])
        all_flashed = np.all(flashed)
        if not one_flash:
            break
        octopus_flashing = np.where(is_flashing(octopus_field))
    octopus_field = np.where(octopus_field >= 10, 0, octopus_field)
    return octopus_field, number_of_flashes, all_flashed


def make_fixed_number_of_flashes(octopus_field):
    count_flashes = 0
    width = len(octopus_field[0])
    height = len(octopus_field)
    for i in range(100):
        octopus_field, flashes, all_flashed = octopus_step(octopus_field, width, height)
        count_flashes += flashes
    return count_flashes


def min_number_steps_for_all_flashes(octopus_field):
    width = len(octopus_field[0])
    height = len(octopus_field)
    count = 0
    all_flashed = False
    while not all_flashed:
        octopus_field, flashes, all_flashed = octopus_step(octopus_field, width, height)
        count += 1
    return count


def format_input(name):
    output = []
    with open(name, 'r') as file:
        lines = file.read().split('\n')
        for line in lines:
            output.append([int(x) for x in list(line)])
    return output


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    formatted_input = np.array(format_input('input.txt'))
    print(make_fixed_number_of_flashes(formatted_input))
    print(min_number_steps_for_all_flashes(formatted_input))
