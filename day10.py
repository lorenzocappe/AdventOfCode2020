def read_file() -> list:
    line_list = []

    file = open("input10.txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        line_list.append(int(line.strip('\n')))
    file.close()

    return line_list


def find_number_jolt_differences(joilt_adapters: list) -> list:
    result = [0, 0, 1]

    adapter_list = joilt_adapters
    adapter_list.sort()

    previous_adapter = 0
    for adapter in adapter_list:
        result[adapter-previous_adapter-1] += 1
        previous_adapter = adapter

    return result


def find_number_ways_reach_max(joilt_adapters: list) -> int:
    result = {0: 1}

    adapter_list = joilt_adapters
    adapter_list.sort()

    for adapter in adapter_list:
        result[adapter] = 0
        for index in range(1, 4):
            if adapter - index in result:
                result[adapter] += result[adapter-index]
        # print(str(adapter)+' '+str(result[adapter]))

    return result[max(adapter_list)]


def main():
    input_lines = read_file()
    # print(input_lines)

    number_joint_differences = find_number_jolt_differences(input_lines)
    # print(number_joint_differences)
    print(number_joint_differences[0]*number_joint_differences[2])
    print(find_number_ways_reach_max(input_lines))


if __name__ == '__main__':
    main()
