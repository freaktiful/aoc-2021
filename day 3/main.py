
import numpy as np

def bool2int(x):
    y = 0
    for i,j in enumerate(x):
        y += j<<i
    return y


def get_rate(x, height):
    return x >= height


def part_1(data):
    arr = np.array(data)
    height = np.shape(arr)[0] / 2
    sum_arr = np.sum(arr, axis=0)
    gamma_rate = [get_rate(x, height) for x in sum_arr]
    epsilon_rate = [not get_rate(y, height) for y in sum_arr]
    return bool2int(gamma_rate[::-1]) * bool2int(epsilon_rate[::-1])


def part_2(data, index, compare_equal):
    arr = np.array(data)
    if np.shape(arr)[0] == 1:
        return bool2int(arr[0][::-1])
    else:
        height = np.shape(arr)[0] / 2
        sum_arr = np.sum(arr, axis=0)
        new_arr = [x for x in data if (compare_equal and (bool(x[index]) == get_rate(sum_arr[index], height))) or
                   (not compare_equal and (bool(x[index]) != get_rate(sum_arr[index], height)))]
        return part_2(new_arr, index + 1, compare_equal)


def format_input(name):
    out = []
    with open(name, 'r') as file:
        aux_arr = file.read().split('\n')
        for el in aux_arr:
            out.append(list(map(int,el)))
        return out


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    array_data = format_input('input.txt')
    print(part_1(array_data))
    oxygen_generator = part_2(array_data, 0, True)
    co2_scrubber = part_2(array_data, 0, False)
    print(oxygen_generator * co2_scrubber)

