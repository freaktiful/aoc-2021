

opening_chars = ['(', '[', '<', '{']
closing_chars = [')', ']', '>', '}']
pairs = {
    '(': ')',
    '[': ']',
    '<': '>',
    '{': '}'
}
points_part_1 = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}
points_part_2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}
incorrect_lines = []


def check_incorrect_line(line):
    pile = []
    for char in line:
        if char in opening_chars:
            pile.append(char)
        else:
            close_char = pile.pop()
            if pairs[close_char] != char:
                return points_part_1[char]
    return 0


def check_incorrect_lines(text):
    score = 0
    for i, line in enumerate(text):
        ind_score = check_incorrect_line(line)
        if ind_score > 0:
            incorrect_lines.append(i)
            score += ind_score
    return score


def remove_incorrect_lines(text):
    incorrect_lines.sort(reverse=True)
    for index in incorrect_lines:
        text.pop(index)


def calculate_score(sequence):
    curr_score = 0
    for char in sequence:
        curr_score *= 5
        curr_score += points_part_2[char]
    return curr_score


def check_incomplete_line(line):
    pile = []
    missing_sequence = []
    for char in line:
        if char in opening_chars:
            pile.append(char)
        else:
            if pile:
                pile.pop()
    while pile:
        missing_char = pile.pop()
        missing_sequence.append(pairs[missing_char])
    return calculate_score(missing_sequence)


def check_incomplete_lines(text):
    remove_incorrect_lines(text)
    total_score = []
    for line in text:
        partial_score = check_incomplete_line(line)
        if partial_score > 0:
            total_score.append(partial_score)
    total_score.sort()
    return total_score[int(len(total_score)/2)]


def format_input(name):
    with open(name, 'r') as file:
        return file.read().split('\n')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    formatted_input = format_input('input.txt')
    print(check_incorrect_lines(formatted_input))
    print(check_incomplete_lines(formatted_input))


