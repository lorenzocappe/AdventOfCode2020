import math
from typing import List


class Tile:
    id = 0
    corners = {}
    image = []

    def __init__(self, text: list):
        if len(text) == 0:
            return

        self.id = int(text[0].split(' ')[1].strip(':'))

        self.corners = {'up': text[1], 'down': text[-1], 'left': '', 'right': ''}

        for index in range(1, len(text)):
            self.corners['left'] += (text[index][0])
            self.corners['right'] += (text[index][-1])

        self.image = text.copy()
        self.image.pop(0)
        return

    def __str__(self):
        return '{id: ' + str(self.id) + ', corners: ' + str(self.corners) + '}'

    def __repr__(self):
        return str(self.id)

    # def __eq__(self, other):
    #    return self.id == other.id

    def print_image(self):
        for line in self.image:
            print(line)
        return

    def flip(self, orientation: str):  # lr or ud
        if orientation == 'l' or orientation == 'r':
            self.image = self.image[::-1]
            self.corners['up'], self.corners['down'] = self.corners['down'], self.corners['up']
            self.corners['left'] = self.corners['left'][::-1]
            self.corners['right'] = self.corners['right'][::-1]

        if orientation == 'u' or orientation == 'd':
            for line in range(len(self.image)):
                self.image[line] = self.image[line][::-1]

            self.corners['left'], self.corners['right'] = self.corners['right'], self.corners['left']
            self.corners['up'] = self.corners['up'][::-1]
            self.corners['down'] = self.corners['down'][::-1]
        return

    def rotate(self):
        temp = ['' for _ in range(len(self.image[0]))]

        for index in range(len(self.image[0])):
            for index2 in range(len(self.image)):
                temp[index] = self.image[index2][index] + temp[index]
        self.image = temp

        temp2 = self.corners['left']
        self.corners['left'] = self.corners['down']
        self.corners['down'] = self.corners['right'][::-1]
        self.corners['right'] = self.corners['up']
        self.corners['up'] = temp2[::-1]
        return

    def is_next_to(self, other) -> tuple:
        result = {}
        if self.id != other.id:
            for my_corner in self.corners:
                for other_corner in self.corners:
                    if self.corners[my_corner] == other.corners[other_corner]:
                        result = 'd', {'my': my_corner[0], 'other': other_corner[0]}, {self.id: my_corner[0],
                                                                                       other.id: other_corner[0]}
                    if self.corners[my_corner] == other.corners[other_corner][::-1]:
                        result = 'r', {'my': my_corner[0], 'other': other_corner[0]}, {self.id: my_corner[0],
                                                                                       other.id: other_corner[0]}

        return result

    def highlight(self, pattern):
        for index_y in range(0, len(self.image) - len(pattern.image) + 1):
            for index_x in range(0, len(self.image[0]) - len(pattern.image[0]) + 1):
                flag = True
                for pattern_y in range(len(pattern.image)):
                    for pattern_x in range(len(pattern.image[0])):
                        if pattern.image[pattern_y][pattern_x] == '#' and self.image[index_y + pattern_y][index_x + pattern_x] != pattern.image[pattern_y][pattern_x]:
                            flag = False
                            break

                if flag:
                    for pattern_y in range(len(pattern.image)):
                        for pattern_x in range(len(pattern.image[0])):
                            if pattern.image[pattern_y][pattern_x] == '#':
                                self.image[index_y + pattern_y] = self.image[index_y + pattern_y][:index_x + pattern_x] + 'O' + self.image[index_y + pattern_y][index_x + pattern_x + 1:]

        return


def read_file() -> list:
    line_list = []

    file = open("input20.txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        line_list.append(line.strip('\n'))
    file.close()

    return line_list


def read_tiles(input_lines: list) -> list:
    temp = []
    tile_list = []
    for line in input_lines:
        if line == '':
            tile_list.append(Tile(temp))
            temp = []
        else:
            temp.append(line)
    tile_list.append(Tile(temp))

    return tile_list


def compose_image_puzzle(tile_list: List[Tile]) -> list:
    positioned_tile_set = {}
    not_positioned_tile_list = tile_list.copy()
    result_image = [[Tile([]) for _ in range(int(math.sqrt(len(not_positioned_tile_list))))]
                    for _ in range(int(math.sqrt(len(not_positioned_tile_list))))]

    not_positioned_tile = not_positioned_tile_list.pop(0)
    positioned_tile_set[not_positioned_tile] = [0, 0]

    while len(not_positioned_tile_list) > 0:
        # i pop the last and, if not positioned, put it back at the end of the list
        not_positioned_tile = not_positioned_tile_list.pop()

        flag = False
        for positioned_tile in positioned_tile_set:
            temp = positioned_tile.is_next_to(not_positioned_tile)
            # print(temp)
            if temp != {}:
                # if there is a connection between the two tiles
                # adjust the not positioned tile and then find its place respective from the positioned tile connected
                while True:
                    if (temp[1]['my'] == 'l' and temp[1]['other'] != 'r') or \
                            (temp[1]['my'] == 'r' and temp[1]['other'] != 'l') or \
                            (temp[1]['my'] == 'u' and temp[1]['other'] != 'd') or \
                            (temp[1]['my'] == 'd' and temp[1]['other'] != 'u'):
                        not_positioned_tile.rotate()
                        temp = positioned_tile.is_next_to(not_positioned_tile)
                    else:
                        break

                if temp[0] == 'r':
                    not_positioned_tile.flip(temp[1]['other'])
                    temp = positioned_tile.is_next_to(not_positioned_tile)
                    # print(temp)

                positioned_tile_set[not_positioned_tile] = positioned_tile_set[positioned_tile].copy()
                if temp[1]['my'] == 'l':
                    positioned_tile_set[not_positioned_tile][0] += -1
                if temp[1]['my'] == 'r':
                    positioned_tile_set[not_positioned_tile][0] += +1
                if temp[1]['my'] == 'd':
                    positioned_tile_set[not_positioned_tile][1] += -1
                if temp[1]['my'] == 'u':
                    positioned_tile_set[not_positioned_tile][1] += +1

                flag = True
                break

        # if the not positioned tile doesn't have connections with positioned tile put it back in the list
        if not flag:
            not_positioned_tile_list.insert(0, not_positioned_tile)

    min_x = len(positioned_tile_set)
    min_y = len(positioned_tile_set)
    for tile in positioned_tile_set:
        if positioned_tile_set[tile][0] < min_x:
            min_x = positioned_tile_set[tile][0]
        if positioned_tile_set[tile][1] < min_y:
            min_y = positioned_tile_set[tile][1]

    min_x *= -1
    min_y *= -1
    for tile in positioned_tile_set:
        positioned_tile_set[tile][0] += min_x
        positioned_tile_set[tile][1] += min_y

        result_image[positioned_tile_set[tile][1]][positioned_tile_set[tile][0]] = tile

    return result_image


def compose_image(image_puzzle: list) -> list:
    image = []
    for row in range(len(image_puzzle)):
        for index in range(len(image_puzzle[row][0].image) - 2, 0, -1):
            image.append('')
            for column in range(len(image_puzzle[row])):
                image[(row + 1) * (len(image_puzzle[row][0].image) - 2) - index] += image_puzzle[row][column].image[
                                                                                        index][1:-1]
    return image


def highlight_monsters(complete_image: list, monster_pattern: list):
    complete_image.insert(0, 'Tile 0001:')
    tile_complete_image = Tile(complete_image)

    monster_pattern.insert(0, 'Tile 0000:')
    tile_monster = Tile(monster_pattern)

    for flip in range(2):
        tile_monster.flip('l')
        for rotate in range(4):
            tile_monster.rotate()
            # print(tile_monster)
            tile_complete_image.highlight(tile_monster)

    complete_image.pop(0)
    monster_pattern.pop(0)
    return tile_complete_image.image


def count_habitat_roughness(image: list) -> int:
    result = 0
    for line in image:
        for character in line:
            if character == '#':
                result += 1

    return result


def main():
    input_lines = read_file()
    # print(input_lines)

    tile_list = read_tiles(input_lines)
    # for tile in tile_list:
    #    print(tile)

    image_puzzle = compose_image_puzzle(tile_list)
    # print(image_puzzle)
    # for tile in tile_list:
    #    print(tile)

    print(image_puzzle[0][0].id * image_puzzle[0][-1].id * image_puzzle[-1][0].id * image_puzzle[-1][-1].id)

    image = compose_image(image_puzzle)
    # for line in image:
    #    print(line)

    monster_pattern = ['                  # ',
                       '#    ##    ##    ###',
                       ' #  #  #  #  #  #   ']
    # print(monster_pattern)

    corrected_image = highlight_monsters(image, monster_pattern)
    # for line in corrected_image:
    #    print(line)

    print(count_habitat_roughness(corrected_image))


if __name__ == '__main__':
    main()
