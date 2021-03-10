def read_file() -> list:
    line_list = []

    file = open("input18.txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        line_list.append(line.strip('\n'))
    file.close()

    return line_list


def precedence(operator: str, type: str) -> int:
    if operator == '+' and type == 'part2':
        return 2
    # if operator == '*':
    #    return 1
    return 1


def execute_operand(operand1: str, operand2: str, operator: str) -> str:
    if operator == '*':
        return str(int(operand1) * int(operand2))
    if operator == '+':
        return str(int(operand1) + int(operand2))
    return ''


# check Shunting-yard algorithm dijkstra
def evaluate(expression: str, type: str) -> int:
    expression = expression.replace('(', '( ')
    expression = expression.replace(')', ' )')

    token_list = expression.split(' ')
    # print(token_list)

    operator_stack = []
    value_stack = []
    while len(token_list) > 0:
        token = token_list.pop(0)
        if token == '(':
            operator_stack.append(token)
        elif token == ')':
            while len(operator_stack) > 0 and operator_stack[-1] != '(':
                operator = operator_stack.pop()
                operand1 = value_stack.pop()
                operand2 = value_stack.pop()
                value_stack.append(execute_operand(operand1, operand2, operator))
            operator_stack.pop()
        elif token == '+' or token == '*':
            while len(operator_stack) > 0 and operator_stack[-1] != '(' and precedence(token, type) <= precedence(operator_stack[-1], type):
                operator = operator_stack.pop()
                operand1 = value_stack.pop()
                operand2 = value_stack.pop()
                value_stack.append(execute_operand(operand1, operand2, operator))
            operator_stack.append(token)
        else:
            value_stack.append(token)
        # print(value_stack)
        # print(operator_stack)
        # print()

    while len(operator_stack) > 0:
        operator = operator_stack.pop()
        operand1 = value_stack.pop()
        operand2 = value_stack.pop()
        value_stack.append(execute_operand(operand1, operand2, operator))
    # print(value_stack)
    # print(operator_stack)

    return int(value_stack[0])


def sum_all_results(expression_list: list, type: str) -> int:
    result = 0
    for expression in expression_list:
        # print(evaluate(expression, type))
        result += evaluate(expression, type)

    return result


def main():
    input_lines = read_file()
    # print(input_lines)

    print(sum_all_results(input_lines, 'part1'))

    print(sum_all_results(input_lines, 'part2'))


if __name__ == '__main__':
    main()
