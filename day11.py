def read_file() -> list:
    line_list = []

    file = open("input11.txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        line_list.append(line.strip('\n'))
    file.close()

    return line_list


def check_adjacent_seats(seat_layout: list, row: int, column: int, part: int) -> dict:
    result = {'#': 0, 'L': 0, '.': 0}
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:

                if part == 1:
                    if 0 <= row + i < len(seat_layout) and 0 <= column + j < len(seat_layout[row]):
                        result[seat_layout[row+i][column+j]] += 1

                if part == 2:
                    cost = 1    # vector length for checking
                    while True:
                        if 0 <= row + i * cost < len(seat_layout) and 0 <= column + j * cost < len(seat_layout[row]):
                            if seat_layout[row+i*cost][column+j*cost] == '.':
                                cost += 1
                            else:
                                result[seat_layout[row+i*cost][column+j*cost]] += 1
                                break
                        else:
                            result['.'] += 1
                            break

    return result


def apply_round_of_seat_rules(seat_layout: list, part: int) -> bool:
    old_seat_layout = seat_layout.copy()
    if part == 1:
        number_occupied_seats_seen = 4
    else:
        number_occupied_seats_seen = 5

    flag = False
    for row in range(len(old_seat_layout)):
        for column in range(len(old_seat_layout[row])):
            if old_seat_layout[row][column] == 'L':
                if check_adjacent_seats(old_seat_layout, row, column, part)['#'] == 0:
                    flag = True
                    seat_layout[row] = seat_layout[row][:column] + '#' + seat_layout[row][column+1:]

            if old_seat_layout[row][column] == '#':
                if check_adjacent_seats(old_seat_layout, row, column, part)['#'] >= number_occupied_seats_seen:
                    flag = True
                    seat_layout[row] = seat_layout[row][:column] + 'L' + seat_layout[row][column+1:]

    return flag


def simulate_seating_area(seat_layout: list, part: int):
    while True:
        flag = apply_round_of_seat_rules(seat_layout, part)
        if not flag:
            break

    return


def count_number_seat_occupied(seat_layout: list) -> int:
    number_seat_occupied = 0
    for row in seat_layout:
        for seat in row:
            if seat == '#':
                number_seat_occupied += 1

    return number_seat_occupied


def main():
    input_lines = read_file()
    simulate_seating_area(input_lines, 1)
    #    for i in input_lines:
    #        print(i)
    #    print()
    print(count_number_seat_occupied(input_lines))

    input_lines = read_file()
    simulate_seating_area(input_lines, 2)
    #   for i in input_lines:
    #       print(i)
    #   print()
    print(count_number_seat_occupied(input_lines))


if __name__ == '__main__':
    main()
