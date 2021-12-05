

ocean_floor_map = {}


def is_45_degrees_diagonal(start, end):
    return max(start[0], end[0]) - min(start[0], end[0]) == max(start[1], end[1]) - min(start[1], end[1])


def mark_map(key):
    if key in ocean_floor_map:
        ocean_floor_map[key] += 1
    else:
        ocean_floor_map[key] = 1


def move_horizontally(start, end):
    for x in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
        mark_map(str(x) + ',' + str(start[1]))


def move_vertically(start, end):
    for y in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
        mark_map(str(start[0]) + ',' + str(y))


def move_diagonally(start, end):
    # for diagonal lines we have to take into account the direction - increment - of the line
    inc_y = 1 if start[1] < end[1] else -1
    y = start[1]
    for x in range(start[0], end[0] + 1 if start[0] < end[0] else end[0] - 1, 1 if start[0] < end[0] else -1):
        mark_map(str(x) + ',' + str(y))
        y += inc_y


def mark_movement_in_map(mov, include_diagonals):
    start = mov[0]
    end = mov[1]
    if start[0] == end[0]:
        move_vertically(start, end)
    if start[1] == end[1]:
        move_horizontally(start, end)
    if include_diagonals and (start[0] != end[0] and start[1] != end[1]):
        if is_45_degrees_diagonal(start, end):
            move_diagonally(start, end)


def map_terrain(readings, include_diagonals):
    ocean_floor_map.clear()
    for movement in readings:
        mark_movement_in_map(movement, include_diagonals)
    return len([x for x in ocean_floor_map.values() if x > 1])


def format_input(name):
    arr_movements = []
    with open(name, 'r') as file:
        string_input = file.read().split('\n')
        for movement in string_input:
            elements = movement.split(' -> ')
            first = [int(x) for x in elements[0].split(',')]
            second = [int(y) for y in elements[1].split(',')]
            arr_movements.append([first, second])
    return arr_movements


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    formatted_input = format_input('input.txt')
    print(map_terrain(formatted_input, False))
    print(map_terrain(formatted_input, True))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
