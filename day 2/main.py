
import numpy as np

move_forward = 'forward'
move_up = 'up'
move_down = 'down'

def move_submarine_part_1(data):
    forward_arr = np.array([int(x[1]) for x in data if x[0] == move_forward])
    down_arr = np.array([int(y[1]) for y in data if y[0] == move_down])
    up_arr = np.array([int(z[1]) for z in data if z[0] == move_up])

    forward = np.sum(forward_arr)
    depth = np.sum(down_arr) - np.sum(up_arr)

    return forward * depth


def f_move_forward(steps, aim, forward, depth):
    forward += steps
    depth += (steps * aim)
    return aim, forward, depth

def f_move_down(steps, aim, forward, depth):
    aim += steps
    return aim, forward, depth

def f_move_up(steps, aim, forward, depth):
    aim -= steps
    return aim, forward, depth

def move_submarine_part_2(data):
    movements = {move_forward: f_move_forward, move_down: f_move_down, move_up: f_move_up}
    aim = 0
    depth = 0
    forward = 0
    for step in data:
        aim, forward, depth = movements[step[0]](int(step[1]), aim, forward, depth)
    return forward * depth


def format_input(name):
    out = []
    with open(name, 'r') as file:
        aux_arr = file.read().split('\n')
        for el in aux_arr:
            out.append(el.split(' '))
        return out


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    array_data = format_input('input.txt')
    position_part_1 = move_submarine_part_1(array_data)
    print(position_part_1)
    position_part_2 = move_submarine_part_2(array_data)
    print(position_part_2)

