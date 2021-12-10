

rowNbr = [-1, 1, 0, 0]
colNbr = [0, 0, -1, 1]

basins = []


def is_tile_part_1(row, col, height, width):
    return (0 <= row < height) and (0 <= col < width)


def check_if_minimum(row, col, height, width, lava_tubes_map):
    for k in range(4):
        if is_tile_part_1(row + rowNbr[k], col + colNbr[k], height, width):
            if lava_tubes_map[row][col] >= lava_tubes_map[row + rowNbr[k]][col + colNbr[k]]:
                return False
    return True


def find_low_points(lava_tubes_map):
    risk_level = 0
    height = len(lava_tubes_map)
    width = len(lava_tubes_map[0])
    for row in range(0, height):
        for col in range(0, width):
            if check_if_minimum(row, col, height, width, lava_tubes_map):
                risk_level += lava_tubes_map[row][col] + 1
    return risk_level


def calculate_basin_parameter():
    basins.sort(reverse=True)
    return basins[0] * basins[1] * basins[2]


def is_tile_part_2(row, col, height, width, visited, lava_tubes_map, curr_value):
    return (0 <= row < height) and (0 <= col < width) and (visited[row][col] is False) and (lava_tubes_map[row][col] != 9)


def explore_basin(row, col, height, width, visited, lava_tubes_map, current_basin):
    visited[row][col] = True
    for k in range(4):
        if is_tile_part_2(row + rowNbr[k], col + colNbr[k], height, width, visited, lava_tubes_map, lava_tubes_map[row][col]):
            current_basin.append(str(row + rowNbr[k]) + ',' + str(col + colNbr[k]))
            explore_basin(row + rowNbr[k], col + colNbr[k], height, width, visited, lava_tubes_map, current_basin)


def find_basins(lava_tubes_map):
    height = len(lava_tubes_map)
    width = len(lava_tubes_map[0])
    visited = [[False for j in range(width)]for i in range(height)]
    basin = []
    for row in range(height):
        for col in range(width):
            if (visited[row][col] is False) and (lava_tubes_map[row][col] != 9):
                basin.append(str(row)+','+str(col))
                explore_basin(row, col, height, width, visited, lava_tubes_map, basin)
                if len(basin) > 1:
                    basins.append(len(basin))
                basin = []
    return calculate_basin_parameter()


def format_input(name):
    output = []
    with open(name, 'r') as file:
        lines = file.read().split('\n')
        for line in lines:
            output.append([int(x) for x in list(line)])
    return output


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    formatted_input = format_input('input.txt')
    print(find_low_points(formatted_input))
    print(find_basins(formatted_input))

