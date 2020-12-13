import math


def read_file() -> list:
    line_list = []

    file = open("input13.txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        line_list.append(line.strip('\n'))
    file.close()

    return line_list


def compute_input_part1(input_lines: list) -> dict:
    result = {'personal_timestamp': int(input_lines[0]), 'bus_timestamps': list()}

    for ID in input_lines[1].split(','):
        if ID != 'x':
            result['bus_timestamps'].append(int(ID))

    return result


def find_earliest_bus_part1(adjusted_input: dict) -> tuple:
    result = []

    for ID in adjusted_input['bus_timestamps']:
        result.append(math.ceil(adjusted_input['personal_timestamp'] / ID) * ID)

    earliest_bus_time = min(result)

    minutes_waited = earliest_bus_time - adjusted_input['personal_timestamp']
    earliest_bus_id = adjusted_input['bus_timestamps'][result.index(earliest_bus_time)]

    return earliest_bus_id, minutes_waited


def compute_input_part2(input_lines: list) -> list:
    result = []

    index = 0
    for ID in input_lines[1].split(','):
        if ID != 'x':
            result.append([index, int(ID)])

        index += 1

    return result


def find_join(bus_1: list, bus_2: list) -> list:
    timestamp = bus_1[0]

    while True:
        # print(str(timestamp)+' '+str(bus_2[0])+' '+str(bus_2[1]))
        if (timestamp + bus_2[0]) % bus_2[1] == 0:
            return [timestamp, bus_1[1]*bus_2[1]]
        else:
            timestamp += bus_1[1]


def find_earliest_bus_part2(adjusted_input: list):
    temp_input = adjusted_input.copy()

    while len(temp_input) > 1:
        bus_3 = find_join(temp_input[0], temp_input[1])
        # print(bus_3)
        # print(find_join(temp_input[1], temp_input[0]))
        temp_input.remove(temp_input[1])
        temp_input.remove(temp_input[0])
        temp_input.insert(0, bus_3)
        print(temp_input)

    return temp_input[0][0]


def main():
    input_lines = read_file()
    # print(input_lines)

    adjusted_input_part1 = compute_input_part1(input_lines)
    # print(adjusted_input_part1)

    earliest_bus_id, minutes_waited = find_earliest_bus_part1(adjusted_input_part1)
    print(earliest_bus_id*minutes_waited)

    adjusted_input_part2 = compute_input_part2(input_lines)
    # print(adjusted_input_part2)

    print(find_earliest_bus_part2(adjusted_input_part2))


if __name__ == '__main__':
    main()
