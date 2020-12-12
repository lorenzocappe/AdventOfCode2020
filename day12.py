import math


def read_file() -> list:
    line_list = []

    file = open("input12.txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        line_list.append(line.strip('\n'))
    file.close()

    return line_list


def get_navigation_instructions(input_list: list) -> list:
    result = []
    for line in input_list:
        temp = [line[0], int(line[1:])]
        result.append(temp)

    return result


def compute_navigation_instructions_part1(navigation_instructions: list, starting_angle: int = 0) -> dict:
    # x(east), y(north), angle difference between ship bow (ship forward) and east (counter-clockwise)
    result = {'x': 0, 'y': 0, 'a': starting_angle}
    # print(result)

    for instruction in navigation_instructions:
        if instruction[0] == 'N':
            result['y'] += instruction[1]
        if instruction[0] == 'S':
            result['y'] -= instruction[1]

        if instruction[0] == 'E':
            result['x'] += instruction[1]
        if instruction[0] == 'W':
            result['x'] -= instruction[1]

        if instruction[0] == 'L':
            result['a'] = (result['a'] + instruction[1]) % 360
        if instruction[0] == 'R':
            result['a'] = (result['a'] - instruction[1]) % 360

        if instruction[0] == 'F':
            result['x'] += int(math.cos(math.radians(result['a']))) * instruction[1]
            result['y'] += int(math.sin(math.radians(result['a']))) * instruction[1]

        # print(instruction)
        # print(result)

    return result


def compute_navigation_instructions_part2(navigation_instructions: list, starting_waypoint: dict) -> dict:
    # x(east), y(north)
    result = {'x': 0, 'y': 0}
    # waypoint = {'x': 10, 'y': 1}
    waypoint = starting_waypoint

    # print(waypoint)
    # print(result)
    # print()
    for instruction in navigation_instructions:
        if instruction[0] == 'N':
            waypoint['y'] += instruction[1]
        if instruction[0] == 'S':
            waypoint['y'] -= instruction[1]

        if instruction[0] == 'E':
            waypoint['x'] += instruction[1]
        if instruction[0] == 'W':
            waypoint['x'] -= instruction[1]

        if instruction[0] == 'L' or instruction[0] == 'R':
            if instruction[0] == 'R':
                instruction[1] *= -1    # this way i can consider the angle as negative and perform the right operation
            temp = waypoint.copy()

            # x' = -sin(a)y + cos(a)x
            waypoint['x'] = int(math.cos(math.radians(instruction[1]))) * temp['x']
            waypoint['x'] -= int(math.sin(math.radians(instruction[1]))) * temp['y']
            # y' = sin(a)x + cos(a)y
            waypoint['y'] = int(math.cos(math.radians(instruction[1]))) * temp['y']
            waypoint['y'] += int(math.sin(math.radians(instruction[1]))) * temp['x']

            if instruction[0] == 'R':
                instruction[1] *= -1    # this way i can consider the angle as negative and perform the right operation

        if instruction[0] == 'F':
            result['x'] += waypoint['x'] * instruction[1]
            result['y'] += waypoint['y'] * instruction[1]

        # print(instruction)
        # print(waypoint)
        # print(result)
        # print()

    return result


def main():
    input_lines = read_file()

    navigation_instructions = get_navigation_instructions(input_lines)

    final_point = compute_navigation_instructions_part1(navigation_instructions, 0)     # start facing east
    # print(final_point)
    print(str(abs(final_point['x']) + abs(final_point['y'])))
    # print()

    final_point = compute_navigation_instructions_part2(navigation_instructions, {'x': 10, 'y': 1})
    # print(final_point)
    print(str(abs(final_point['x']) + abs(final_point['y'])))
    # print()


if __name__ == '__main__':
    main()
