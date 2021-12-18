

def shoot_probe(vx, vy, area):
    init_v = (vx, vy)
    probe_x = vx
    probe_y = vy
    y_values = [probe_y]
    while True:
        if (min(area[0]) <= probe_x <= max(area[0])) and (min(area[1]) <= probe_y <= max(area[1])):
            return True, max(y_values), init_v
        if (probe_x > max(area[0])) or (probe_y < min(area[1])):
            return False, None, None
        if vx > 0:
            vx -= 1
        if vx < 0:
            vx += 1
        probe_x += vx
        vy -=1
        probe_y += vy
        y_values.append(probe_y)


def aim_and_shoot_probe(area):
    heights = []
    hits = []
    max_x_v = max(area[0]) + 1
    for x in range(1, max_x_v):
        for y in range(min(area[1]), abs(min(area[1]))):
            achieved, height, hit = shoot_probe(x, y, area)
            if achieved:
                heights.append(height)
                hits.append(hit)
    return max(heights), len(hits)


def format_input(name):
    with open(name, 'r') as file:
        coords = file.readline().replace('target area: ', '').split(', ')
        x_coord = [int(x) for x in coords[0].replace('x=', '').split('..')]
        y_coord = [int(y) for y in coords[1].replace('y=', '').split('..')]
        return [x_coord, y_coord]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    target_area = format_input('input.txt')
    print(aim_and_shoot_probe(target_area))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
