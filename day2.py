def read_file():
    list = []

    file = open("input2.1.txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        list.append(line.strip('\n'))
    file.close()

    return list


class Password:
    letter = ''
    min = 0
    max = 0
    word = ""
    number_letters = {}

    def __init__(self, letter, min, max, word):
        self.letter = letter
        self.min = min
        self.max = max
        self.word = word
        self.compute_number_letters()
        return

    def compute_number_letters(self):
        self.number_letters = {}

        for i in self.word:
            if i in self.number_letters:
                self.number_letters[i] += 1
            else:
                self.number_letters[i] = 1
        return

    def is_valid_part1(self):
        if self.min != 0 and self.letter not in self.number_letters:
            return False
        if self.number_letters[self.letter] > self.max:
            return False
        if self.number_letters[self.letter] < self.min:
            return False
        return True

    def is_valid_part2(self):
        if self.word[self.min-1] == self.word[self.max-1]:
            return False
        if self.word[self.min-1] != self.letter and self.word[self.max-1] != self.letter:
            return False
        return True

    def __str__(self):
        return self.word+" "+self.letter+" "+str(self.min)+"-"+str(self.max)


def compute_password_list(line_list):
    password_list = []
    for i in range(len(line_list)):
        temp = line_list[i].split()
        interval = temp[0].split('-')

        min = int(interval[0])
        max = int(interval[1])
        letter = temp[1][0]
        word = temp[2]

        password_list.append(Password(letter, min, max, word))
    return password_list


def main():
    line_list = read_file()
    password_list = compute_password_list(line_list)

    number_valid_part1 = 0
    number_valid_part2 = 0
    for i in password_list:
        if i.is_valid_part1():
            number_valid_part1 += 1
        if i.is_valid_part2():
            number_valid_part2 += 1

    print(number_valid_part1)
    print(number_valid_part2)


if __name__ == '__main__':
    main()