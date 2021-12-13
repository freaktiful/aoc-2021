
import itertools
import numpy as np


def fold_vertically(paper, axis):
    new_paper = [x for x in paper if x[0] < int(axis)]
    half_paper = [[int(axis) - (a[0] - int(axis)), a[1]] for a in paper if a[0] > int(axis)]
    return new_paper + half_paper


def fold_horizontally(paper, axis):
    new_paper = [y for y in paper if y[1] < int(axis)]
    half_paper = [[a[0], int(axis) - (a[1] - int(axis))] for a in paper if a[1] > int(axis)]
    return new_paper + half_paper


orders = {
    'x': fold_vertically,
    'y': fold_horizontally
}


def fold_all(paper, fold_orders):
    for order in fold_orders:
        paper = fold_paper(paper, order)
    return paper


def fold_paper(paper, order):
    fold = orders[order[0]](paper, order[1])
    fold.sort()
    folded = list(fold for fold, _ in itertools.groupby(fold))
    return folded


def format_input(name):
    points = []
    folds = []
    fold_order = 'fold along '
    with open(name, 'r') as file:
        lines = file.read().split('\n')
        for line in lines:
            if len(line) > 0:
                if fold_order not in line:
                    points.append([int(x) for x in line.split(',')])
                else:
                    folds.append(line.replace(fold_order, '').split('='))
    return points, folds


def print_result(paper):
    points_matrix = np.amax(np.array(paper), axis=0)
    printed_paper = [['0' for j in range(points_matrix[0]+1)] for i in range(points_matrix[1]+1)]
    for point in paper:
        printed_paper[point[1]][point[0]] = 'X'
    return np.matrix(printed_paper)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    initial_paper, folding_orders = format_input('input.txt')

    print(len(fold_paper(initial_paper, folding_orders[0])))

    folded_paper = fold_all(initial_paper, folding_orders)
    print(print_result(folded_paper))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

