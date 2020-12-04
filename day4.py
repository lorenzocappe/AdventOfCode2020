def read_file():
    list = []

    file = open("input4.1.txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        list.append(line.strip('\n'))
    file.close()

    return list


def create_passports(batch_list):
    passport_list = []
    temp = {}

    for line in batch_list:
        if line == '':
            passport_list.append(temp)
            temp = {}
        else:
            sequences = line.split(' ')
            for pair in sequences:
                key, value = pair.split(':')
                temp[key] = value
    passport_list.append(temp)  #for last element, without black line after

    return passport_list


def is_valid_passport_part1(passport):
    key_list = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'] #, 'cid']  #optional

    for key in key_list:
        if key not in passport:
            return False
    return True


def count_valid_passports_part1(passport_list):
    number_valid_passports = 0

    for passport in passport_list:
        if is_valid_passport_part1(passport):
            number_valid_passports += 1

    return number_valid_passports


def is_valid_passport_part2(passport):
    eye_color_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    if is_valid_passport_part1(passport):
        if len(passport['byr']) != 4 or int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
            print('byr: '+passport['byr'])
            return False

        if len(passport['iyr']) != 4 or int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
            print('iyr: '+passport['iyr'])
            return False

        if len(passport['eyr']) != 4 or int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
            print('eyr: '+passport['eyr'])
            return False

        if passport['hgt'][-2:] == 'cm':
            if int(passport['hgt'][:-2]) < 150 or int(passport['hgt'][:-2]) > 193:
                print('hgt: '+passport['hgt'])
                return False
        elif passport['hgt'][-2:] == 'in':
            if int(passport['hgt'][:-2]) < 59 or int(passport['hgt'][:-2]) > 76:
                print('hgt: '+passport['hgt'])
                return False
        else:
            print('hgt: '+passport['hgt'])
            return False

        if len(passport['hcl']) == 7 and passport['hcl'][:1] == '#':
            if not passport['hcl'][1:4].isalnum():
                print('hcl: '+passport['hcl'])
                return False
        else:
            print('hcl: '+passport['hcl'])
            return False

        if passport['ecl'] not in eye_color_list:
            print('ecl: '+passport['ecl'])
            return False

        if len(passport['pid']) != 9 or (not passport['pid'].isdigit()):
            print('pid: '+passport['pid'])
            return False

        return True
    else:
        return False


def count_valid_passports_part2(passport_list):
    number_valid_passports = 0

    for passport in passport_list:
        if is_valid_passport_part2(passport):
            number_valid_passports += 1

    return number_valid_passports


def main():

    batch_list = read_file()
    passport_list = create_passports(batch_list)

    number_valid_passports = count_valid_passports_part1(passport_list)
    print(number_valid_passports)

    number_valid_passports = count_valid_passports_part2(passport_list)
    print(number_valid_passports)

if __name__ == '__main__':
    main()
