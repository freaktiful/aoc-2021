from collections import Counter
from math import ceil


class PolymerSequencer(object):

    _sequence = ''

    _rules = {}

    _occurrences = {}

    def __init__(self, initial_sequence, rules):
        self._rules = {}
        self._sequence = initial_sequence
        self.add_rules(rules)
        self.initialize_occurrences()

    def add_rules(self, rules):
        for key, value in rules:
            self._rules[key] = value
            self._occurrences[key] = 0

    def initialize_occurrences(self):
        for i in range(len(self._sequence)-2, -1, -1):
            seq = self._sequence[i: i+2]
            if seq in self._rules:
                self._occurrences[seq] += 1

    def insertion_step_part_1(self):
        for i in range(len(self._sequence)-2, -1, -1):
            if self._sequence[i: i+2] in self._rules:
                aux_seq = self._sequence[:i+1] + self._rules[self._sequence[i: i+2]] + self._sequence[i+1:]
                self._sequence = aux_seq

    def insertion_step_part_2(self):
        aux_dict = self._occurrences.copy()
        for oc, value in aux_dict.items():
            self._occurrences[oc] -= value
            first, last = oc
            self._occurrences[first + self._rules[oc]] += value
            self._occurrences[self._rules[oc] + last] += value

    @property
    def rules(self):
        return self._rules

    @property
    def sequence(self):
        return self._sequence

    @property
    def occurrences(self):
        return self._occurrences


def part_1(polymer_sequencer):
    for step in range(10):
        polymer_sequencer.insertion_step_part_1()
    counter = Counter(polymer_sequencer.sequence).most_common()
    # without destructuring
    return counter[0][1] - counter[len(counter) - 1][1]


def part_2(polymer_sequencer):
    for step in range(40):
        polymer_sequencer.insertion_step_part_2()
    final_occurrences = polymer_sequencer.occurrences

    totals = Counter()
    for (first, second), n in final_occurrences.items():
        totals[first] += n
        totals[second] += n
    # https://blog.teclado.com/destructuring-in-python/
    # turns out destructuring works pretty much as it does in javascript
    (_, most), *_, (_, least) = totals.most_common()

    return ceil((most - least) / 2)


def format_input(name):
    rules = []
    with open(name, 'r') as file:
        seq = file.readline().replace('\n', '')
        file.readline()
        lines = file.read().split('\n')
        for line in lines:
            rules.append(line.split(' -> '))
    return PolymerSequencer(seq, rules)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sequencer = format_input('input.txt')

    print(part_1(sequencer))
    print(part_2(sequencer))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
