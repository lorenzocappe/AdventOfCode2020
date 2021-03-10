def read_file() -> list:
    line_list = []

    file = open("input24.txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        line_list.append(line.strip('\n'))
    file.close()

    return line_list


class Tile:

    def __init__(self, identification_str: str):
        self.position = {'x': 0, 'y': 0}
        self.is_white = False

        self.find_position(identification_str)
        if (self.position['x'] + self.position['y']) % 2 != 0:
            print(identification_str)
            print('err')
            print(self)
        return

    def find_position(self, identification_str: str):
        prev = ''
        for ch in identification_str:
            if ch == 'w':
                self.position['x'] += -1
                if prev != 's' and prev != 'n':
                    self.position['x'] += -1
            elif ch == 'e':
                self.position['x'] += +1
                if prev != 's' and prev != 'n':
                    self.position['x'] += +1

            elif ch == 's':
                self.position['y'] += -1
            elif ch == 'n':
                self.position['y'] += +1

            prev = ch
        return

    def __str__(self):
        result = '(' + str(self.position['x']) + ',' + str(self.position['y']) + ')'
        if self.is_white:
            result += ' white'
        else:
            result += ' black'
        return result

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.position['x'] == other.position['x'] and self.position['y'] == other.position['y']


def position_floor(tile_list: list) -> list:
    positioned_tiles = []

    for tile in tile_list:
        temp = Tile(tile)

        if temp in positioned_tiles:
            index = positioned_tiles.index(temp)
            positioned_tiles[index].is_white = True
        else:
            positioned_tiles.append(Tile(tile))

    return positioned_tiles


def construct_floor(positioned_tiles: list) -> list:
    if (positioned_tiles[0].position['x'] + positioned_tiles[0].position['y']) % 2 == 0:
        starting_point = 1
    else:
        starting_point = 0

    min_x = 0
    min_y = 0
    for tile in positioned_tiles:
        if min_x > tile.position['x']:
            min_x = tile.position['x']
        if min_y > tile.position['y']:
            min_y = tile.position['y']
    for tile in positioned_tiles:
        tile.position['x'] -= min_x
        tile.position['y'] -= min_y

    for tile in positioned_tiles:
        if tile.position['y'] == 0:
            print(tile)

    max_x = 0
    max_y = 0
    for tile in positioned_tiles:
        if max_x < tile.position['x']:
            max_x = tile.position['x']
        if max_y < tile.position['y']:
            max_y = tile.position['y']

    floor = [[' ' for _1 in range(max_x+1)] for _2 in range(max_y+1)]

    for tile in positioned_tiles:
        if not tile.is_white:
            floor[tile.position['y']][tile.position['x']] = 'B'
        else:
            floor[tile.position['y']][tile.position['x']] = 'W'

    for index_y in range(len(floor)):
        for index_x in range(len(floor[0])):
            if floor[index_y][index_x] == ' ' and (index_x + index_y + starting_point) % 2 != 0:
                floor[index_y][index_x] = 'W'

    return floor


def expand_floor(floor: list):
    if floor[0][0] == ' ':
        starting_point = 0
    else:
        starting_point = 1

    flag_first = False
    flag_last = False
    for index_y in range(len(floor)):
        if floor[index_y][0] == 'B':
            flag_first = True
        if floor[index_y][-1] == 'B':
            flag_last = True

        if flag_first and flag_last:
            break

    if flag_first:
        starting_point += 1

    for index_y in range(len(floor)):
        if flag_first:
            floor[index_y].insert(0, ' ')
        if flag_last:
            floor[index_y].append(' ')

    if 'B' in floor[0]:
        temp = [' ' for _ in range(len(floor[0]))]
        floor.insert(0, temp)
        starting_point += 1
    if 'B' in floor[-1]:
        temp = [' ' for _ in range(len(floor[0]))]
        floor.append(temp)

    for index_y in range(len(floor)):
        for index_x in range(len(floor[0])):
            if floor[index_y][index_x] == ' ' and (index_x + index_y + starting_point) % 2 != 0:
                floor[index_y][index_x] = 'W'

    return


def change_floor_config(floor: list):
    change_list = []

    for index_y in range(len(floor)):
        for index_x in range(len(floor[0])):
            neighbors = find_neighbors(floor, index_x, index_y)

            if floor[index_y][index_x] == 'B' and (neighbors == 0 or neighbors > 2):
                change_list.append([index_x, index_y])
            if floor[index_y][index_x] == 'W' and neighbors == 2:
                change_list.append([index_x, index_y])

    # print(change_list)
    for change in change_list:
        if floor[change[1]][change[0]] == 'W':
            floor[change[1]][change[0]] = 'B'
        elif floor[change[1]][change[0]] == 'B':
            floor[change[1]][change[0]] = 'W'

    return


def find_neighbors(floor: list, index_x: int, index_y: int) -> int:
    result = 0
    for y in [-1, 1]:
        for x in [-1, 1]:
            if 0 <= index_x + x < len(floor[0]) and 0 <= index_y + y < len(floor):
                if floor[index_y+y][index_x+x] == 'B':
                    result += 1

    for x in [-2, 2]:
        if 0 <= index_x + x < len(floor[0]) and 0 <= index_y + y < len(floor):
            if floor[index_y][index_x + x] == 'B':
                result += 1

    return result


def find_number_black_tiles(floor: list) -> int:
    result = 0
    for index_y in range(len(floor)):
        for index_x in range(len(floor[0])):
            if floor[index_y][index_x] == 'B':
                result += 1

    return result


def print_floor(floor: list):

    for index_y in range(len(floor) - 1, -1, -1):
        temp = ''
        for index_x in range(len(floor[0])):
            temp += floor[index_y][index_x]
        print(temp)
    print()


def main():
    input_lines = read_file()
    # print(input_lines)

    positioned_tiles = position_floor(input_lines)
    # for tile in positioned_tiles:
    #    print(tile)

    floor = construct_floor(positioned_tiles)
    # print_floor(floor)
    print(find_number_black_tiles(floor))

    for index in range(1, 101):
        expand_floor(floor)
        change_floor_config(floor)

        print('day '+str(index)+': '+str(find_number_black_tiles(floor)))
        # print_floor(floor)


if __name__ == '__main__':
    main()
