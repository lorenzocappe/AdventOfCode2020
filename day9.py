def read_file() -> list:
    line_list = []

    file = open("input9.txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        line_list.append(int(line.strip('\n')))
    file.close()

    return line_list


def find_pair(number_list: list, number_index: int, preamble_length: int = 25) -> tuple:
    # print(number_list[number_index-preamble_length:number_index])
    # print(number_list[number_index])
    for index1 in range(number_index-preamble_length, number_index):
        for index2 in range(index1+1, number_index):
            if number_list[index1] + number_list[index2] == number_list[number_index]:
                return index1, index2

    return -1, -1


def find_first_invalid_number(numbers_list: list, preamble_length: int = 25) -> int:
    for index in range(preamble_length, len(numbers_list)):
        # print(index)
        temp = find_pair(numbers_list, index, preamble_length)
        if temp == (-1, -1):
            return numbers_list[index]
    return -1


def find_contiguous_set_sum(number_list: list, number_to_find: int) -> tuple:
    for index1 in range(0, len(number_list)-1):
        current_sum = number_list[index1]

        for index2 in range(index1 + 1, len(number_list)):
            if current_sum == number_to_find:
                return index1, index2

            if current_sum < number_to_find:
                current_sum += number_list[index2]

    return -1, -1


def main():
    input_lines = read_file()
    # print(input_lines)

    invalid_number = find_first_invalid_number(input_lines, 25)
    print(invalid_number)

    start, end = find_contiguous_set_sum(input_lines, invalid_number)
    contiguous_set = input_lines[start:end]
    mini = min(contiguous_set)
    maxi = max(contiguous_set)
    # print(str(mini)+' '+str(maxi))
    print(str(mini+maxi))


if __name__ == '__main__':
    main()
