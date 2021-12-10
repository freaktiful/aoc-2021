
def count_unique_digits_in_output(digits):
    count = 0
    for digit in digits:
        count += len([x for x in digit[1] if len(x) == 2 or len(x) == 3 or len(x) == 4 or len(x) == 7])
    return count


def is_two(array, combination):
    return not combination['f2'] in array and not combination['b2'] in array and \
           combination['c2'] in array and combination['a2'] in array and \
           combination['d2'] in array


def is_three(array, combination):
    return combination['c2'] in array and combination['f2'] in array and \
           combination['a2'] in array and combination['d2'] in array and \
           not combination['b2'] in array


def is_five(array, combination):
    return not combination['c2'] in array and combination['f2'] in array and \
           combination['a2'] in array and combination['b2'] in array and \
           combination['d2'] in array


def is_zero(array, combination):
    return not combination['d2'] in array


def is_six(array, combination):
    return combination['d2'] in array and combination['e2'] in array


def is_nine(array, combination):
    return combination['d2'] in array and combination['c2'] in array


def assign_two_three_five(two, three, five, two_b, three_b, five_b, combination):
    combination['g2'] = [y for y in two if y in three and y in five and y not in combination.values()][0]
    combination['e2'] = [y for y in two_b if y not in three_b and y not in five_b and y not in combination.values()][0]
    return True, combination


def solve_two_three_five(aux1, aux2, aux3, combination):
    if is_two(aux1, combination):
        if is_three(aux2, combination) and is_five(aux3, combination) or \
           is_three(aux3, combination) and is_five(aux2, combination):
            return assign_two_three_five(aux1, aux2, aux3, aux1, aux2, aux3, combination)
    if is_two(aux2, combination):
        if is_three(aux1, combination) and is_five(aux3, combination) or \
           is_three(aux3, combination) and is_five(aux1, combination):
            return assign_two_three_five(aux1, aux2, aux3, aux2, aux1, aux3, combination)
    if is_two(aux3, combination):
        if is_three(aux1, combination) and is_five(aux2, combination) or \
           is_three(aux2, combination) and is_five(aux1, combination):
            return assign_two_three_five(aux1, aux2, aux3, aux3, aux1, aux2, combination)
    return False, combination


def solve_puzzle_segments_five(line, combination):
    # All the segments can be figured out without checking any more combinations
    combination_numbers_two_three_five = [x for x in line if len(x) == 5]
    aux1 = list(combination_numbers_two_three_five[0])
    aux2 = list(combination_numbers_two_three_five[1])
    aux3 = list(combination_numbers_two_three_five[2])
    return solve_two_three_five(aux1, aux2, aux3, combination)


def solve_puzzle_segments_three_four(line, combination):
    combination_number_seven = list([x for x in line if len(x) == 3][0])
    # there is only one possibility for this segment, so it is gonna be correctly assigned always.
    combination['a2'] = list(filter(lambda y: y != combination['c2'] and y != combination['f2'],
                                    combination_number_seven))[0]
    combination_number_four = list([x for x in line if len(x) == 4])[0]
    aux = list(filter(lambda z: z != combination['c2'] and z != combination['f2']
                                    and z != combination['a2'], combination_number_four))
    combination['b2'] = aux[0]
    combination['d2'] = aux[1]
    solved, combination = solve_puzzle_segments_five(line, combination)
    if not solved:
        combination['b2'] = aux[1]
        combination['d2'] = aux[0]
        solved, combination = solve_puzzle_segments_five(line, combination)
    return solved, combination


def solve_line(line):
    combination_number_one = list([x for x in line if len(x) == 2][0])
    this_try = {'c2': combination_number_one[0], 'f2': combination_number_one[1]}
    solved, combination = solve_puzzle_segments_three_four(line, this_try)
    if not solved:
        this_try = {'c2': combination_number_one[1], 'f2': combination_number_one[0]}
        solved, combination = solve_puzzle_segments_three_four(line, this_try)
    return solved, combination


def decode_number(combination, number):
    switcher = {
        2: '1',
        3: '7',
        4: '4',
        7: '8'
    }
    if len(number) in switcher:
        return switcher[len(number)]
    else:
        if len(number) == 5:
            aux = list(number)
            if is_two(aux, combination):
                return '2'
            if is_three(aux, combination):
                return '3'
            if is_five(aux, combination):
                return '5'
        if len(number) == 6:
            aux = list(number)
            if is_zero(aux, combination):
                return '0'
            if is_six(aux, combination):
                return '6'
            if is_nine(aux, combination):
                return '9'


def decode_numbers(combination, line):
    decoded_number = ''
    for number in line:
        decoded_number += decode_number(combination, number)
    return decoded_number


def solve_display(lines):
    digits_sum = 0
    for line in lines:
        solved, combination = solve_line(line[0])
        if solved:
            digits_sum += int(decode_numbers(combination, line[1]))
    return digits_sum


def format_input(name):
    segments = []
    with open(name, 'r') as file:
        lines = file.read().split('\n')
        for line in lines:
            aux = line.split(' | ')
            aux_input = aux[0].split(' ')
            aux_output = aux[1].split(' ')
            segments.append([aux_input, aux_output])
    return segments


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    formatted_input = format_input('input.txt')
    print(count_unique_digits_in_output(formatted_input))
    print(solve_display(formatted_input))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
