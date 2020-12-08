def read_file() -> list:
    line_list = []

    file = open("input6.txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        line_list.append(line.strip('\n'))
    file.close()

    return line_list


def divide_in_groups(input_lines: list) -> list:
    groups = []

    temp = []
    for line in input_lines:
        if line == '':
            groups.append(temp)
            temp = []
        else:
            temp.append(line)
    groups.append(temp)

    return groups


def count_group_answers_anyone(group_answers: list) -> int:
    temp = ""
    for answer in group_answers:
        temp = temp + answer
    return len(set(temp))


def sum_counts_group_answers_anyone(all_group_answers: list) -> int:
    result = 0
    for group_answers in all_group_answers:
        result += count_group_answers_anyone(group_answers)

    return result


def count_group_answers_everyone(group_answers: list) -> int:
    letters_list = list(group_answers[0])

    for answer in group_answers:
        letters_to_remove = []

        for letter in letters_list:
            if letter not in answer:
                letters_to_remove.append(letter)

        # in two step because it's bad to remove elements from a list you are iterating on
        for letter in letters_to_remove:
            letters_list.remove(letter)

    return len(letters_list)


def sum_counts_group_answers_everyone(all_group_answers: list) -> int:
    result = 0
    for group_answers in all_group_answers:
        result += count_group_answers_everyone(group_answers)

    return result


def main():
    input_lines = read_file()

    all_group_answers = divide_in_groups(input_lines)

    print(sum_counts_group_answers_anyone(all_group_answers))
    print(sum_counts_group_answers_everyone(all_group_answers))


if __name__ == '__main__':
    main()
