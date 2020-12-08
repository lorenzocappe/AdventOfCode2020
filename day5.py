def read_file():
    line_list = []

    file = open("input5.txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        line_list.append(line.strip('\n'))
    file.close()

    return line_list


def binary_partitioning(moves_list: str, partitioning_letters: str = 'LR') -> int:
    start = 0
    end = 2 ** len(moves_list) - 1

    lower_move = partitioning_letters[0]
    # upper_move = partitioning_letters[1]

    for move in moves_list:
        middle = int((start + end) / 2)
        # print(str(start)+' '+str(middle)+' '+str(end))
        if move == lower_move:
            end = middle
        else:
            start = middle + 1

    # print(str(start)+' '+str(middle)+' '+str(end))
    return start  # == end


def read_row(boarding_pass):
    return binary_partitioning(boarding_pass[:7], "FB")


def read_column(boarding_pass):
    return binary_partitioning(boarding_pass[7:], "LR")


def read_boarding_pass(boarding_pass):
    seat_id = read_row(boarding_pass) * 8 + read_column(boarding_pass)
    # print(boarding_pass+' '+str(id))
    return seat_id


def max_seat_id(boarding_pass_list):
    maxi = -1
    for boarding_pass in boarding_pass_list:
        temp = read_boarding_pass(boarding_pass)
        if temp > maxi:
            maxi = temp

    return maxi


def create_boarding_id_list(boarding_pass_list):
    boarding_id_list = []

    for boarding_pass in boarding_pass_list:
        boarding_id_list.append(read_boarding_pass(boarding_pass))

    return boarding_id_list


def find_seat(boarding_id_list):
    # boarding_id_list.append(651)   #check integrity adding missing seat
    boarding_id_list.sort()
    print(boarding_id_list)

    personal_seat_id = -1
    for index in range(len(boarding_id_list)):
        if index != len(boarding_id_list) - 1:  # and index != 0:
            if boarding_id_list[index] != boarding_id_list[index + 1] - 1:
                personal_seat_id = boarding_id_list[index] + 1

    return personal_seat_id


def main():
    boarding_pass_list = read_file()
    # print(boarding_pass_list)

    print(max_seat_id(boarding_pass_list))
    print(find_seat(create_boarding_id_list(boarding_pass_list)))


if __name__ == '__main__':
    main()
