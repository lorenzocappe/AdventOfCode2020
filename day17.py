def read_file() -> list:
    line_list = []

    file = open("input17.txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        line_list.append(line.strip('\n'))
    file.close()

    return line_list


def main():
    input_lines = read_file()
    print(input_lines)


if __name__ == '__main__':
    main()
