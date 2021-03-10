def read_file() -> list:
    line_list = []

    file = open("input14.txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        line_list.append(line.strip('\n'))
    file.close()

    return line_list


def compute_input(input_lines: list) -> list:
    result = []

    for line in input_lines:
        temp = line.split(' = ')

        if temp[0] != 'mask':
            temp = ['mem', temp[0].strip('mem[').strip(']'), int(temp[1])]

        result.append(temp)

    return result


def run_program(adjusted_input: list) -> dict:
    mask = ''
    mem = {}

    for line in adjusted_input:
        if line[0] == 'mask':
            mask = line[1]
        if line[0] == 'mem':
            mem[line[1]] = apply_mask(mask, line[2])

    return mem


def from_dec_to_bin(number: int) -> str:
    result = ''
    for index in range(36):
        if number > 0:
            result = str(number % 2) + result
            number = int(number / 2)
        else:
            result = '0' + result
    return result


def from_bin_to_dec(number: str) -> int:
    result = 0
    for index in range(36):
        if number[35 - index] != '0':
            result += 2**index

    return result


def apply_mask(mask: str, number: int) -> int:
    temp = from_dec_to_bin(number)

    for index in range(36):
        if mask[index] != 'X':
            temp = temp[:index] + mask[index] + temp[index+1:]

    return from_bin_to_dec(temp)


def main():
    input_lines = read_file()
    # print(input_lines)

    adjusted_input = compute_input(input_lines)
    # print(adjusted_input)

    memory = run_program(adjusted_input)
    print(memory)

    result = 0
    for address in memory:
        result += memory[address]

    print(result)


if __name__ == '__main__':
    main()
