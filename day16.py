def read_file() -> list:
    line_list = []

    file = open("input16.txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        line_list.append(line.strip('\n'))
    file.close()

    return line_list


def compute_rules(input_lines: list) -> dict:
    result = {}

    for line in input_lines:
        if line == '':
            break
        temp = line.split(': ')
        result[temp[0]] = []
        for interval in temp[1].split(' or '):
            numbers = interval.split('-')
            result[temp[0]].append([int(numbers[0]), int(numbers[1])])

    return result


def compute_personal_tickets(input_lines: list) -> list:
    starting_point = -1
    for index in range(len(input_lines)):
        if input_lines[index] == 'your ticket:':
            starting_point = index + 1
            break

    ticket = []
    for num in input_lines[starting_point].split(','):
        ticket.append(int(num))

    return ticket


def compute_nearby_tickets(input_lines: list) -> list:
    starting_point = -1
    for index in range(len(input_lines)):
        if input_lines[index] == 'nearby tickets:':
            starting_point = index + 1
            break

    result = []
    for index in range(starting_point, len(input_lines)):
        ticket = []
        for number in input_lines[index].split(','):
            ticket.append(int(number))
        result.append(ticket)

    return result


def is_number_in_interval(number: int, interval: list) -> bool:
    if number < interval[0] or number > interval[1]:
        return False
    return True


def get_ticket_invalid_fields(ticket: list, rules: dict) -> list:
    ticket_invalid_fields = []
    for number in ticket:
        flag = False
        for rule in rules:
            for interval in rules[rule]:
                if is_number_in_interval(number, interval):
                    flag = True

        if not flag:
            ticket_invalid_fields.append(number)

    # print(ticket_invalid_fields)
    return ticket_invalid_fields


def get_ticket_scanning_error_rate(nearby_tickets: list, rules: dict) -> int:
    scanning_error_rate = 0
    for ticket in nearby_tickets:
        ticket_invalid_fields = get_ticket_invalid_fields(ticket, rules)
        if len(ticket_invalid_fields) < len(ticket):
            for field in ticket_invalid_fields:
                scanning_error_rate += field

    return scanning_error_rate


def get_valid_tickets(nearby_tickets: list, rules: dict) -> list:
    valid_tickets = []
    for ticket in nearby_tickets:
        ticket_invalid_fields = get_ticket_invalid_fields(ticket, rules)
        if len(ticket_invalid_fields) == 0:
            valid_tickets.append(ticket)

    return valid_tickets


def assign_rules(valid_tickets: list, rules: dict) -> list:
    not_assigned_rules = list(rules.keys())

    assigned_rules = ['' for _ in range(len(valid_tickets[0]))]

    while len(not_assigned_rules) > 0:
        rule = not_assigned_rules.pop(0)

        list_valid_columns = []
        for column in range(len(valid_tickets[0])):
            if assigned_rules[column] != '':
                continue

            flag = True
            for ticket in valid_tickets:

                if not is_number_in_interval(ticket[column], rules[rule][0])\
                        and not is_number_in_interval(ticket[column], rules[rule][1]):
                    flag = False
                    break

            if flag:
                list_valid_columns.append(column)

        if len(list_valid_columns) == 1:
            assigned_rules[list_valid_columns[0]] = rule
        else:
            not_assigned_rules.append(rule)

    return assigned_rules


def main():
    input_lines = read_file()
    # print(input_lines)

    rules = compute_rules(input_lines)
    # print(rules)

    personal_tickets = compute_personal_tickets(input_lines)
    # print(personal_tickets)

    nearby_tickets = compute_nearby_tickets(input_lines)
    # print(nearby_tickets)

    print(get_ticket_scanning_error_rate(nearby_tickets, rules))

    valid_tickets = get_valid_tickets(nearby_tickets, rules)
    # print(valid_tickets)

    assigned_rules = assign_rules(valid_tickets, rules)
    # print(assigned_rules)

    result = 1
    for index in range(len(assigned_rules)):
        if 'departure' in assigned_rules[index]:
            result *= personal_tickets[index]
    print(result)


if __name__ == '__main__':
    main()
