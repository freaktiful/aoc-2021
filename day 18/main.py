import math


class SnailfishNumber:

    def __init__(self, value, left, right):
        self._value = int(value) if value is not None else value
        self._left = self.decode_number(left) if left is None or left.startswith('[') \
            else SnailfishNumber(left, None, None)
        self._right = self.decode_number(right) if right is None or right.startswith('[') \
            else SnailfishNumber(right, None, None)

    @property
    def is_number_pair(self):
        return self._value is None and type(self._left._value) == int and type(self._right._value) == int

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @property
    def value(self):
        return self._value

    def add_values(self, value):
        self._value += value

    def split(self):
        if self._value is not None:
            if self._value >= 10:
                left = math.floor(self._value/2)
                right = math.ceil(self._value/2)
                self._value = None
                self._left = SnailfishNumber(left, None, None)
                self._right = SnailfishNumber(right, None, None)
                return True
            else:
                return False
        else:
            splitted = self._left.split()
            if not splitted:
                splitted = self._right.split()
            return splitted

    def reduce(self):
        exploded, left, right, add_l, add_r = self.explode()
        if exploded:
            self.reduce()
        else:
            splitted = self.split()
            if splitted:
                self.reduce()

    def explode(self, level=0):
        if level == 4 and self.is_number_pair:
            left = self._left.value
            right = self._right.value
            self._value = 0
            self._left = None
            self._right = None
            return True, left, right, False, False
        else:
            if self._value is None and self._left is not None and self._right is not None:
                exploded, value_left, value_right, add_l, add_r = self._left.explode(level+1)
                if exploded:
                    if not add_r:
                        add_r = self.add_right(value_right, self._right)
                    return True, value_left, value_right, add_l, add_r
                else:
                    exploded, value_left, value_right, add_l, add_r = self._right.explode(level+1)
                    if exploded:
                        if not add_l:
                            add_l = self.add_left(value_left, self._left)
                        return True, value_left, value_right, add_l, add_r
                    else:
                        return False, None, None, False, False
            else:
                return False, None, None, False, False

    @staticmethod
    def add_left(value, subtree):
        if subtree.value is not None:
            subtree.add_values(value)
            return True
        else:
            added = subtree.add_left(value, subtree.right)
            if not added:
                added = subtree.add_left(value, subtree.left)
            return added

    @staticmethod
    def add_right(value, subtree):
        if subtree.value is not None:
            subtree.add_values(value)
            return True
        else:
            added = subtree.add_right(value, subtree.left)
            if not added:
                added = subtree.add_right(value, subtree.right)
            return added

    @staticmethod
    def decode_number(number):
        if number is None:
            return number
        else:
            queue = []
            first = ''
            for i in range(1, len(number)):
                first += number[i]
                if number[i] != '[' and number[i] != ']' and i == 1:
                    number = number[i + 1:]
                    break
                if number[i] == '[':
                    queue.append(number[i])
                if number[i] == ']':
                    queue.pop()
                if len(queue) == 0:
                    number = number[i+1:]
                    break
            second = ''
            for i in range(1, len(number)):
                if number[i] != '[' and number[i] != ']' and i == 1:
                    second = number[i]
                    number = number[i + 2:]
                    break
                if number[i] == '[':
                    queue.append(number[i])
                if number[i] == ']':
                    queue.pop()
                if len(queue) == 0:
                    number = number[i + 2:]
                    break
                second += number[i]
            return SnailfishNumber(None, first, second)

    def print_number(self):
        if self._value is not None:
            return self._value
        else:
            value_left = str(self._left.print_number())
            value_right = str(self._right.print_number())
            return '['+value_left+','+value_right+']'

    def magnitude(self):
        if self._value is not None:
            return self._value
        else:
            return (3 * self._left.magnitude()) + (2 * self._right.magnitude())


def sum_snailfish(val1, val2):
    aux = SnailfishNumber(None, val1.print_number(), val2.print_number())
    aux.reduce()
    return aux


def format_input(name):
    output = []
    with open(name, 'r') as file:
        operands = file.read().split('\n')
        for oper in operands:
            left, right = read_left_right(oper)
            output.append([left, right])
    return output


def read_left_right(oper):
    left = ''
    right = ''
    oper = oper[1:len(oper)-1]
    if oper[0] != '[':
        aux = oper.find(',')
        left = oper[0: aux]
        right = oper[aux+1:]
    else:
        pile = []
        length_left = 0
        for i in range(len(oper)):
            if oper[i] == '[':
                pile.append(oper[i])
            if oper[i] == ']':
                pile.pop()
            if len(pile) == 0:
                length_left = i
                break
        left = oper[0:length_left+1]
        right = oper[length_left+2:]
    return left, right


def part_1(snailfishes):
    snail_list = []
    for snailfish in snailfishes:
        s = SnailfishNumber(None, snailfish[0], snailfish[1])
        snail_list.append(s)
    first_operand = snail_list[0]
    for i in range(1, len(snail_list)):
        partial_sum = sum_snailfish(first_operand, snail_list[i])
        partial_sum.print_number()
        first_operand = partial_sum
    return partial_sum, partial_sum.magnitude()


def part_2(snailfishes):
    snail_list = []
    for snailfish in snailfishes:
        s = SnailfishNumber(None, snailfish[0], snailfish[1])
        snail_list.append(s)
    max_sum = 0
    for snail in snail_list:
        for snail_2 in snail_list:
            partial_sum = sum_snailfish(snail, snail_2)
            partial_magnitude = partial_sum.magnitude()
            if partial_magnitude > max_sum:
                max_sum = partial_magnitude
    return max_sum


if __name__ == '__main__':

    formatted_input = format_input('input.txt')
    number, magnitude = part_1(formatted_input)
    print(number.print_number())
    print(magnitude)

    print(part_2(formatted_input))







