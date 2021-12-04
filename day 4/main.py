
import numpy as np


def check_number(card, number):
    # Marks a checked number as '-1'
    for i, line in enumerate(card):
        if number in line:
            card[i] = [-1 if x == number else x for x in card[i]]
    return card


def check_card(card):
    # This can be done in only one loop because the height and width of the matrix are the same
    trans_card = card.T
    for i in range(card.shape[0]):
        if np.all(card[i] == card[i][0]):
            return True
        if np.all(trans_card[i] == trans_card[i][0]):
            return True
    return False


def score(card, number):
    unmarked_sum = card[card != -1].sum()
    return unmarked_sum * number


def bingo(input_numbers, input_cards):
    for n in input_numbers:
        for c in input_cards:
            c = check_number(c, n)
            if check_card(np.array(c)):
                return score(np.array(c), n)


def rigged_bingo(input_numbers, input_cards):
    for n in input_numbers:
        aux_cards = input_cards[:]
        for i, c in enumerate(aux_cards):
            c = check_number(c, n)
            if check_card(np.array(c)):
                if len(input_cards) > 1:
                    input_cards.remove(c)
                else:
                    return score(np.array(c), n)


def format_input(name):
    arr_cards = []
    with open(name, 'r') as file:
        input_numbers = [int(x) for x in file.readline().replace('\n', '').split(',')]
        aux = []
        input_cards = file.read().split('\n')
        for i, line in enumerate(input_cards):
            if line != '':
                aux.append([int(x) for x in line.strip().replace('  ', ' ').split(' ')])
            else:
                if len(aux) > 0:
                    arr_cards.append(aux)
                    aux = []
            if i == len(input_cards) - 1:
                arr_cards.append(aux)
        return input_numbers, arr_cards


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numbers, cards = format_input('input.txt')
    print(bingo(numbers, cards))
    print(rigged_bingo(numbers, cards))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
