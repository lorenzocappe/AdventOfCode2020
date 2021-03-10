def read_input(input_line: str) -> list:
    result = []
    for ch in input_line:
        result.append(int(ch))

    return result


def play_game(starting_cup_sequence: list, number_moves: int) -> list:
    current_cup_sequence = starting_cup_sequence.copy()
    for index in range(len(current_cup_sequence)):
        current_cup_sequence[index] -= 1

    current_cup = current_cup_sequence[0]
    move = 0
    while move < number_moves:
        current_cup_index = current_cup_sequence.index(current_cup)
        # print('current cup: '+str(current_cup))
        # print('cc ind: '+str(current_cup_index))
        # print(current_cup_sequence)

        destination_cup = (current_cup_sequence[current_cup_index] - 1) % len(current_cup_sequence)
        # print(destination_cup)

        cups_after_current = []
        for _ in range(3):
            popping_point = current_cup_index + 1
            if popping_point >= len(current_cup_sequence):
                popping_point = 0
            # print(popping_point)
            cups_after_current.append(current_cup_sequence.pop(popping_point))
        # print(cups_after_current)

        while destination_cup in cups_after_current:
            destination_cup = (destination_cup - 1) % (len(current_cup_sequence) + 3)
        # print(destination_cup)

        # print(current_cup_sequence)
        destination_index = (current_cup_sequence.index(destination_cup) + 1) % len(current_cup_sequence)
        # print(destination_index)

        if current_cup_index+1 >= len(current_cup_sequence):
            current_cup = current_cup_sequence[0]
        else:
            current_cup = current_cup_sequence[current_cup_index+1]

        for index in range(2, -1, -1):
            current_cup_sequence.insert(destination_index, cups_after_current[index])

        # print()
        move += 1

    for index in range(len(current_cup_sequence)):
        current_cup_sequence[index] += 1
    return current_cup_sequence


def calculate_sequence_result(cup_sequence: list):
    starting_point = cup_sequence.index(1)
    result = ''
    for index in range(1, len(cup_sequence)):
        result += str(cup_sequence[(starting_point+index) % len(cup_sequence)])

    return result


def main():
    input_line = '135468729'
    # print(input_line)

    starting_cup_sequence = read_input(input_line)
    # print(starting_cup_sequence)

    finishing_cup_sequence = play_game(starting_cup_sequence, 100)
    print(calculate_sequence_result(finishing_cup_sequence))

    for index in range(10, 10000001):
        starting_cup_sequence.append(index)
    print(calculate_sequence_result(play_game(starting_cup_sequence, 10000000)))


if __name__ == '__main__':
    main()
