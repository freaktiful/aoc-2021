import numpy as np

rowNbr = [-1, 0, 1]
colNbr = [-1, 0, 1]


def enlarge_map(old_matrix, character):
    new_matrix = np.array([[character for x in range(len(old_matrix) + 2)] for y in range(len(old_matrix[0]) + 2)])
    new_matrix[1:len(old_matrix) + 1, 1:len(old_matrix[0]) + 1] = old_matrix
    return new_matrix


def is_safe(row, col, height, width):
    return (0 <= row < height) and (0 <= col < width)


def decode_pixel(x, y, matrix, key, char):
    binary_number = ''
    for row in range(3):
        for col in range(3):
            binary_number += matrix[x + rowNbr[row]][y + colNbr[col]] if is_safe(x + rowNbr[row], y + colNbr[col], len(matrix), len(matrix[0])) else char
    decoded_number = int(binary_number.replace('.', '0').replace('#', '1'), 2)
    return key[decoded_number]


def enhance_image(matrix, key, char):
    enhanced = np.array([['' for x in range(len(matrix))] for y in range(len(matrix[0]))])
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            enhanced[x, y] = decode_pixel(x, y, matrix, key, char)
    return enhanced


def format_input(name):
    with open(name, 'r') as file:
        key = list(file.readline().replace('\n', ''))
        file.readline()
        data = file.read().split('\n')
        data = [list(d) for d in data]
        return key, np.array(data)


def part_1(input_data, key):
    # enlarge and enhance once
    data = enlarge_map(input_data, '.')
    data = enhance_image(data, key, '.')
    # enlarge and enhance twice
    data = enlarge_map(data, key[0])
    data = enhance_image(data, key, key[0])
    # return result matrix
    return data


def part_2(input_data, key):
    # first enhancement
    data = enlarge_map(input_data, '.')
    data = enhance_image(data, key, '.')
    # rest of the enhancements until 50
    for i in range(1, 50):
        if ((i+1) % 2) == 0:
            data = enlarge_map(data, key[0])
            data = enhance_image(data, key, key[0])
        else:
            data = enlarge_map(data, key[511] if key[0] == '#' else key[0])
            data = enhance_image(data, key, key[511] if key[0] == '#' else key[0])
    return data


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    key, data = format_input('input.txt')
    data_part_1 = part_1(data, key)
    count_part_1 = np.count_nonzero(data_part_1 == '#')
    print(count_part_1)
    data_part_2 = part_2(data, key)
    count_part_2 = np.count_nonzero(data_part_2 == '#')
    print(count_part_2)