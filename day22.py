def read_file() -> list:
    line_list = []

    file = open("input22.txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        line_list.append(line.strip('\n'))
    file.close()

    return line_list


def read_player_decks(input_lines: list) -> list:
    result = []

    temp = []
    for line in input_lines:
        if line == '':
            result.append(temp)
        elif 'Player' in line:
            temp = []
        else:
            temp.append(int(line))
    result.append(temp)

    return result


def play_combat(player_decks: list) -> tuple:
    playable_decks = [player_decks[0].copy(), player_decks[1].copy()]
    while len(playable_decks[0]) > 0 and len(playable_decks[1]) > 0:
        # print('pl1 deck: '+str(playable_decks[0]))
        # print('pl2 deck: '+str(playable_decks[1]))

        temp1 = playable_decks[0].pop(0)
        temp2 = playable_decks[1].pop(0)
        # print('pl1: '+str(temp1))
        # print('pl2: '+str(temp2))

        if temp1 > temp2:
            # print('pl1 win')
            playable_decks[0].append(temp1)
            playable_decks[0].append(temp2)
        else:
            # print('pl2 win')
            playable_decks[1].append(temp2)
            playable_decks[1].append(temp1)
        # print()

    if len(playable_decks[0]) == 0:
        return 2, playable_decks[1]
    else:
        return 1, playable_decks[0]


def play_recursive_combat(player_decks: list) -> tuple:
    playable_decks = [player_decks[0].copy(), player_decks[1].copy()]
    # print('game')
    while len(playable_decks[0]) > 0 and len(playable_decks[1]) > 0:
        # print('pl1 deck: ' + str(playable_decks[0]))
        # print('pl2 deck: ' + str(playable_decks[1]))

        temp1 = playable_decks[0].pop(0)
        temp2 = playable_decks[1].pop(0)
        # print('pl1: ' + str(temp1))
        # print('pl2: ' + str(temp2))

        if temp1 <= len(playable_decks[0]) and temp2 <= len(playable_decks[1]):
            winner = play_recursive_combat(playable_decks)[0]
        else:
            if temp1 > temp2:
                winner = 1
            else:
                winner = 2

        if winner == 1:
            # print('pl1 win')
            playable_decks[0].append(temp1)
            playable_decks[0].append(temp2)
        else:
            # print('pl2 win')
            playable_decks[1].append(temp2)
            playable_decks[1].append(temp1)
        # print()

    if len(playable_decks[0]) == 0:
        return 2, playable_decks[1]
    else:
        return 1, playable_decks[0]


def calculate_score(finishing_deck: list) -> int:
    result = 0
    finishing_deck = finishing_deck[::-1]

    for index in range(len(finishing_deck)):
        result += (index+1) * finishing_deck[index]

    return result


def main():
    input_lines = read_file()
    # print(input_lines)

    player_decks = read_player_decks(input_lines)
    # print(player_decks)

    # print(play_combat(player_decks))

    print(player_decks)
    print(calculate_score(play_combat(player_decks)[1]))
    print(player_decks)

    print(calculate_score(play_recursive_combat(player_decks)[1]))


if __name__ == '__main__':
    main()
