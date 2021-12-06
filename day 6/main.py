school = []
adult_day_limit = 6
newborn_day_limit = 9
newborn_day_limit_part_2 = 8


class Lanternfish:
    def __init__(self, age=None):
        if age:
            self.newborn = False
            self.spawner = age
        else:
            self.newborn = True
            self.spawner = newborn_day_limit

    def pass_day(self):
        if self.spawner == 0:
            self.spawner = adult_day_limit
            self.newborn = False
            school.append(Lanternfish())
        else:
            self.spawner -= 1


def simulate_day():
    for fish in school:
        fish.pass_day()


def part_1(initial_fishies):
    school.clear()
    for i in initial_fishies:
        school.append(Lanternfish(int(i)))
    for i in range(0, 80):
        simulate_day()
    return len(school)


class School:
    population = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    def __init__(self, days_to_spawn_array):
        for days_to_spawn in days_to_spawn_array:
            self.population[days_to_spawn] += 1

    def pass_day(self):
        aux_population = {}
        for i in self.population:
            if i == 0:
                previous_adults = self.population[adult_day_limit + 1] if adult_day_limit + 1 in self.population else 0
                aux_population[newborn_day_limit_part_2] = self.population[i]
                aux_population[adult_day_limit] = self.population[i] + previous_adults
            else:
                if i - 1 != adult_day_limit:
                    aux_population[i - 1] = self.population[i]
        self.population.clear()
        self.population = aux_population.copy()


def part_2(initial_fishies):
    fishies = School(initial_fishies)
    for i in range(0, 256):
        fishies.pass_day()
    return sum(fishies.population.values())


def format_input(name):
    with open(name, 'r') as file:
        return [int(x) for x in file.read().replace('\n', '').split(',')]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    formatted_input = format_input('input.txt')
    print(part_1(formatted_input))
    print(part_2(formatted_input))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
