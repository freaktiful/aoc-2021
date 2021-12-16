import numpy as np
import sys

cave_map = []
map_height = 0
map_width = 0

rowNbr = [-1, 1, 0, 0]
colNbr = [0, 0, -1, 1]


def is_tile(row, col):
    return (0 <= row < map_height) and (0 <= col < map_width)


def find_min_cost_path_recursive(start, end):
    # not used function, but I worked on it and I'm not deleting it
    x, y = start
    z, w = end
    if not is_tile(x, y):
        return sys.maxsize
    if x == z and y == w:
        return cave_map[x][y]
    else:
        return cave_map[x][y] + \
           min(find_min_cost_path_recursive([x + rowNbr[1], y + colNbr[1]], end),
               find_min_cost_path_recursive([x + rowNbr[3], y + colNbr[3]], end))


def find_min_cost_dynamic(node_x, node_y):
    # not used function, but I worked on it and I'm not deleting it
    costs_matrix = [[0 for j in range(map_width)]for i in range(map_height)]
    for x in range(1, map_height):
        costs_matrix[x][0] = costs_matrix[x-1][0] + cave_map[x][0]
    for y in range(1, map_width):
        costs_matrix[0][y] = costs_matrix[0][y-1] + cave_map[0][y]
    for x in range(1, map_height):
        for y in range(1, map_height):
            costs_matrix[x][y] = cave_map[x][y] + min(costs_matrix[x][y-1], costs_matrix[x-1][y])
    return costs_matrix[node_x][node_y]


def find_min_cost_dijkstra(x, y):
    paths_matrix = [[sys.maxsize for j in range(map_width)] for i in range(map_height)]
    visited = [[False for j in range(map_width)] for i in range(map_height)]
    paths_matrix[0][0] = 0
    nodes_queue = [([0, 0], 0)]
    while len(nodes_queue) > 0:
        ([i, j],_) = nodes_queue.pop()
        if not visited[i][j]:
            for k in range(4):
                if is_tile(i + rowNbr[k], j + colNbr[k]) and not visited[i + rowNbr[k]][j + colNbr[k]]:
                    paths_matrix[i + rowNbr[k]][j + colNbr[k]] = \
                        min(paths_matrix[i][j] + cave_map[i + rowNbr[k]][j + colNbr[k]],
                            paths_matrix[i + rowNbr[k]][j + colNbr[k]])
                    nodes_queue.append(([i + rowNbr[k], j + colNbr[k]], paths_matrix[i + rowNbr[k]][j + colNbr[k]]))
                    nodes_queue = sorted(nodes_queue, key=lambda el: el[1], reverse=True)
            visited[i][j] = True
    return paths_matrix[x][y]


def format_input(name):
    output = []
    with open(name, 'r') as file:
        lines = file.read().split('\n')
        for line in lines:
            output.append([int(x) for x in list(line)])
    return output


def unfold_cave():
    # not optimizing this function. not the point of the exercise
    actual_cave = np.array([[0 for j in range(map_width * 5)]for i in range(map_height * 5)])
    actual_cave[0:map_height, 0:map_width] = cave_map

    aux_map = (np.array(cave_map) + 1)
    aux_map = np.where(aux_map > 9, 1, aux_map)
    actual_cave[map_height:map_height * 2, 0:map_width] = aux_map
    actual_cave[0:map_height, map_width:map_width * 2] = aux_map

    aux_map = aux_map + 1
    aux_map = np.where(aux_map > 9, 1, aux_map)
    actual_cave[map_height*2:map_height*3, 0:map_width] = aux_map
    actual_cave[map_height:map_height*2, map_width:map_width*2] = aux_map
    actual_cave[0:map_height, map_width*2:map_width * 3] = aux_map

    aux_map = aux_map + 1
    aux_map = np.where(aux_map > 9, 1, aux_map)
    actual_cave[map_height * 3:map_height * 4, 0:map_width] = aux_map
    actual_cave[map_height * 2:map_height * 3, map_width:map_width * 2] = aux_map
    actual_cave[map_height:map_height * 2, map_width * 2:map_width * 3] = aux_map
    actual_cave[0:map_height, map_width * 3:map_width * 4] = aux_map

    aux_map = aux_map + 1
    aux_map = np.where(aux_map > 9, 1, aux_map)
    actual_cave[map_height * 4:map_height * 5, 0:map_width] = aux_map
    actual_cave[map_height:map_height * 2, map_width * 3:map_width * 4] = aux_map
    actual_cave[map_height * 2:map_height * 3, map_width * 2:map_width * 3] = aux_map
    actual_cave[map_width * 3:map_width * 4, map_height:map_height * 2] = aux_map
    actual_cave[0:map_height, map_width * 4:map_width * 5] = aux_map

    aux_map = aux_map + 1
    aux_map = np.where(aux_map > 9, 1, aux_map)
    actual_cave[map_height:map_height * 2, map_width * 4:map_width * 5] = aux_map
    actual_cave[map_height * 2:map_height * 3, map_width * 3:map_width * 4] = aux_map
    actual_cave[map_height * 3:map_height * 4, map_width * 2:map_width * 3] = aux_map
    actual_cave[map_width * 4:map_width * 5, map_height:map_height * 2] = aux_map

    aux_map = aux_map + 1
    aux_map = np.where(aux_map > 9, 1, aux_map)
    actual_cave[map_height * 2:map_height * 3, map_width * 4:map_width * 5] = aux_map
    actual_cave[map_height * 3:map_height * 4, map_width * 3:map_width * 4] = aux_map
    actual_cave[map_height * 4:map_height * 5, map_width * 2:map_width * 3] = aux_map

    aux_map = aux_map + 1
    aux_map = np.where(aux_map > 9, 1, aux_map)
    actual_cave[map_height * 3:map_height * 4, map_width * 4:map_width * 5] = aux_map
    actual_cave[map_height * 4:map_height * 5, map_width * 3:map_width * 4] = aux_map

    aux_map = aux_map + 1
    aux_map = np.where(aux_map > 9, 1, aux_map)
    actual_cave[map_height * 4:map_height * 5, map_width * 4:map_width * 5] = aux_map

    return actual_cave.tolist()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cave_map = format_input('input.txt')
    map_height = len(cave_map)
    map_width = len(cave_map[0])
    # print(find_min_cost_path_recursive([0, 0], [map_width - 1, map_height - 1]) - cave_map[0][0])
    # print(find_min_cost_dynamic(map_width - 1, map_height - 1))
    print(find_min_cost_dijkstra(map_width - 1, map_height - 1))
    cave_map = unfold_cave()
    map_height = len(cave_map)
    map_width = len(cave_map[0])
    # print(find_min_cost_dynamic(map_width - 1, map_height - 1))
    print(find_min_cost_dijkstra(map_width - 1, map_height - 1))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
