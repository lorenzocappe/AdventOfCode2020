def read_file() -> list:
    line_list = []

    file = open("input8.txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        line_list.append(line.strip('\n'))
    file.close()

    return line_list


def run_program(boot_code: list) -> tuple:
    accumulator = 0
    cursor = 0

    not_run_value = -1
    instructions_run = [not_run_value for _ in range(len(boot_code))]

    index = 1
    while True:
        if cursor == len(boot_code):
            return accumulator, cursor, True

        if instructions_run[cursor] != not_run_value:
            break
        instructions_run[cursor] = index
        index += 1

        instruction = boot_code[cursor].split(' ')
        if instruction[0] == 'acc':
            accumulator += int(instruction[1])
            cursor += 1
        elif instruction[0] == 'jmp':
            cursor += int(instruction[1])
        else:    # elif instruction[0] == 'nop':
            cursor += 1

        # print(instructions_run)
        # print(boot_code)
        # print(accumulator)
        # print(cursor)
        # print(index)

    return accumulator, cursor, False


def check_boot_code_accumulator(boot_code: list) -> int:
    return run_program(boot_code)[0]


def check_boot_code_termination(boot_code: list) -> bool:
    return run_program(boot_code)[2]


def change_line_of_code(boot_code: list, line_number: int, instruction: str, argument: int):
    boot_code[line_number] = instruction+' '+str(argument)
    return


def correct_boot_code(boot_code: list):
    list_nop_jmp = []
    for index in range(len(boot_code)):
        line_to_change = boot_code[index].split(' ')
        if line_to_change[0] == 'nop' or line_to_change[0] == 'jmp':
            list_nop_jmp.append(index)
    # print(list_nop_jmp)

    for index in range(len(list_nop_jmp)):
        temp_code = list(boot_code)

        changed_line = boot_code[list_nop_jmp[index]].split(' ')
        if changed_line[0] == 'nop':
            changed_line[0] = 'jmp'
        elif changed_line[0] == 'jmp':
            changed_line[0] = 'nop'
        # print(changed_line)

        change_line_of_code(temp_code, list_nop_jmp[index], changed_line[0], changed_line[1])
        if check_boot_code_termination(temp_code):
            change_line_of_code(boot_code, list_nop_jmp[index], changed_line[0], changed_line[1])
            return


def main():
    input_lines = read_file()
    # print(input_lines)
    print(run_program(input_lines))

    correct_boot_code(input_lines)
    # print(input_lines)
    print(run_program(input_lines))


if __name__ == '__main__':
    main()
