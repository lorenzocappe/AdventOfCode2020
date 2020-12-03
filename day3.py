def read_file():
    list = []

    file = open("input3.1.txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        list.append(line.strip('\n'))
    file.close()

    return list


def check_slope(slope_map, slope_down, slope_right):
    starting_point = [0, 0]
    number_of_trees = 0

    while True:
        starting_point[0] = (starting_point[0] + slope_right) % len(slope_map[0])
        starting_point[1] += slope_down

        if starting_point[1] >= len(slope_map):
            break

        if slope_map[starting_point[1]][starting_point[0]] == '#':
            number_of_trees += 1

    return number_of_trees


def main():
    line_list = read_file()

    print(check_slope(line_list,1,3))

    total_sum_number_trees = 1
    for slope in range(4):
        total_sum_number_trees *= check_slope(line_list, 1, 2*slope+1)
    total_sum_number_trees *= check_slope(line_list, 2, 1)

    print(total_sum_number_trees)

    #for i in range(len(line_list)):
    #    print(line_list[i])


if __name__ == '__main__':
    main()
