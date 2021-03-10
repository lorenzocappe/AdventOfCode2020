def print_floor(floor: list):
    for index_y in range(len(floor) - 1, -1, -1):
        temp = ''
        for index_x in range(len(floor[0])):
            temp += floor[index_y][index_x]
        print(temp)
    print()


def transform_subject_number(subject_number: int, loop_size: int, standard_divisor: int) -> int:
    result = 1
    for index in range(loop_size):
        result *= subject_number
        result = result % standard_divisor

    return result


def find_loop_size(subject_number: int, key: int, standard_divisor: int) -> int:
    value = 1
    loop_size = 0

    while value != key:
        loop_size += 1
        value *= subject_number
        value = value % standard_divisor

    return loop_size


def main():
    standard_divisor = 20201227
    init_subject_number = 7
    public_keys = {'card': 8987316, 'door': 14681524}

    # print(input_lines)
    loop_size = {'card': find_loop_size(init_subject_number, public_keys['card'], standard_divisor),
                 'door': find_loop_size(init_subject_number, public_keys['door'], standard_divisor)}

    encryption_keys = {'card': transform_subject_number(public_keys['card'], loop_size['door'], standard_divisor),
                       'door': transform_subject_number(public_keys['door'], loop_size['card'], standard_divisor)}

    print('card public key: ' + str(public_keys['card']))
    print('door public key: ' + str(public_keys['door']))

    print('card loop size: ' + str(loop_size['card']))
    print('card loop size: ' + str(loop_size['door']))

    print('card encryption key: ' + str(encryption_keys['card']))
    print('door encryption key: ' + str(encryption_keys['door']))


if __name__ == '__main__':
    main()
