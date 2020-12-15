def read_file() -> list:
    line_list = []

    file = open("input15.txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        line_list.append(line.strip('\n'))
    file.close()

    return line_list


def compute_input_part1(input_lines: list) -> list:
    starting_numbers = input_lines[0].split(',')

    current_numbers = []
    for number in starting_numbers:
        current_numbers.append(int(number))

    return current_numbers


def compute_input_part2(input_lines: list) -> dict:
    starting_numbers = input_lines[0].split(',')

    current_numbers = {}
    for index in range(len(starting_numbers)):
        current_numbers[int(starting_numbers[index])] = index

    return current_numbers


def find_th_number_part1(starting_numbers: list, index_to_find: int) -> int:
    current_numbers = starting_numbers.copy()

    current_index = len(current_numbers) - 1
    while True:
        last_seen = current_index
        for index in range(current_index - 1, -1, -1):
            if current_numbers[current_index] == current_numbers[index]:
                last_seen = index
                break

        if last_seen == current_index:
            current_numbers.append(0)
        else:
            current_numbers.append(current_index - last_seen)

        current_index += 1

        if current_index == index_to_find:
            break

    # print(current_numbers)
    return current_numbers[index_to_find]


def find_th_number_part2(starting_numbers: dict, index_to_find: int) -> int:
    current_numbers = starting_numbers.copy()

    current_index = len(current_numbers) - 1

    last_seen = -1
    for i in current_numbers:
        if current_numbers[i] == current_index:
            last_seen = i
            break

    while True:
        if last_seen in current_numbers:
            temp = current_index - current_numbers[last_seen]

            current_numbers[last_seen] += temp
            last_seen = temp

        else:
            current_numbers[last_seen] = current_index
            last_seen = 0

        current_index += 1

        if current_index == index_to_find:
            break

    return last_seen


def main():
    input_lines = read_file()
    # print(input_lines)

    current_numbers_part1 = compute_input_part1(input_lines)
    # print(current_numbers_part1)

    print(find_th_number_part1(current_numbers_part1, 2020 - 1))    # 2020th spoken is the index 2019

    current_numbers_part2 = compute_input_part2(input_lines)
    # print(current_numbers_part2)

    # print(find_th_number_part2(current_numbers_part2, 2020 - 1))
    print(find_th_number_part2(current_numbers_part2, 30000000 - 1))


if __name__ == '__main__':
    main()
