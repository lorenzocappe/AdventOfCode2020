def read_file():
    number_list = []

    file = open("input1.txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        number_list.append(int(line))
    file.close()

    return number_list


def two_sum_to(number, num_list, starting_index):
    for i in range(starting_index, len(num_list)):
        for j in range(i+1, len(num_list)):
            if num_list[i]+num_list[j] == number:
                return [num_list[i], num_list[j]]
    return []


def three_sum_to(number, num_list, starting_index):
    for i in range(starting_index, len(num_list)):
        temp = two_sum_to(number-num_list[i], num_list, i+1)
        if len(temp) != 0:
                temp.append(num_list[i])
                return temp
    return []


def main():
    num_list = read_file()

    result = two_sum_to(2020, num_list, 0)
    print(result[:])
    print(str(result[0] * result[1]))
    print()

    result = three_sum_to(2020, num_list, 0)
    print(result[:])
    print(str(result[0] * result[1] * result[2]))
    print()


if __name__ == '__main__':
    main()
