# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def process_data_part_1(data):
    cont = 0
    idx = 1
    while idx < len(data):
        if (int(data[idx]) >= int(data[idx - 1])):
            cont = cont + 1
        idx = idx + 1
    return cont

def process_data_part_2(data):
    cont = 0
    idx = 0
    while idx < len(data) - 3:
        print(data[idx + 3])
        pre = int(data[idx]) + int(data[idx +1]) + int(data[idx + 2])
        pos = int(data[idx +1]) + int(data[idx + 2]) + int(data[idx + 3])
        if (pos > pre):
            cont = cont + 1
        idx = idx + 1
    return cont


def format_input(name):
    with open(name, 'r') as file:
        return file.read().split('\n')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    array_data = format_input('input.txt')
    print(process_data_part_1(array_data))
    print(process_data_part_2(array_data))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
