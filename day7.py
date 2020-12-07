def read_file() -> list:
    line_list = []

    file = open("input7.1.txt", "r")
    while True:
        line = file.readline()
        if not line:
            break
        line_list.append(line.strip('\n'))
    file.close()

    return line_list


def build_inverted_graph(input_lines: list) -> dict:
    graph = {}
    for line in input_lines:
        starting_line, finishing_line = line.split('bags contain ')  # mind the extra space

        starting_line_list = starting_line.split(' ')
        starting_node = starting_line_list[0]+'-'+starting_line_list[1]

        # maybe not the best to differentiate them only by the final s
        finishing_nodes = []
        if finishing_line != 'no other bags.':
            finishing_line_parts = finishing_line.split(', ')     # mind the extra space
            for temp in finishing_line_parts:
                line_list = temp.split(' ')
                finishing_nodes.append(line_list[1]+'-'+line_list[2])

        # inverted graph building line by line
        for node in finishing_nodes:
            if node not in graph:
                graph[node] = []
            graph[node].append(starting_node)

    return graph


def dfs_reachable_nodes(graph: dict, starting_node: str) -> list:
    reached_nodes = []
    queue = [starting_node]

    while len(queue) > 0:
        current_node = queue.pop()
        reached_nodes.append(current_node)

        if current_node in graph:
            for node in graph[current_node]:
                if node not in reached_nodes and node not in queue:
                    queue.append(node)

    return reached_nodes


def build_weighted_graph(input_lines: list) -> dict:
    graph = {}
    for line in input_lines:
        starting_line, finishing_line = line.split('bags contain ')  # mind the extra space

        starting_line_list = starting_line.split(' ')
        starting_node = starting_line_list[0] + '-' + starting_line_list[1]

        finishing_nodes = []
        if finishing_line != 'no other bags.':
            finishing_line_parts = finishing_line.split(', ')  # mind the extra space
            for temp in finishing_line_parts:
                line_list = temp.split(' ')
                finishing_nodes.append([line_list[1] + '-' + line_list[2], int(line_list[0])])

        if starting_node not in graph:
            graph[starting_node] = []
        if len(finishing_nodes) > 0:
            graph[starting_node] = finishing_nodes

    return graph


def dfs_number_of_bags(graph: dict, starting_node: str) -> int:
    null_number = 0

    nodes_number_of_bags = {}
    for bag in graph:
        if len(graph[bag]) == 0:
            nodes_number_of_bags[bag] = 1
        else:
            nodes_number_of_bags[bag] = null_number

    queue = [starting_node]
    while len(queue) > 0:
        current_node = queue[-1]    # .top()

        # if you already know the number of bags that bag is valued don't visit the node
        if nodes_number_of_bags[current_node] != null_number:
            queue.pop()
        else:
            current_node_number_of_bags = 1
            flag = True

            for node in graph[current_node]:
                if nodes_number_of_bags[node[0]] == null_number:
                    flag = False
                    queue.append(node[0])
                else:
                    current_node_number_of_bags += nodes_number_of_bags[node[0]] * node[1]

            # if you have been able to calculate the number of bags that bag is valued
            if flag:
                nodes_number_of_bags[current_node] = current_node_number_of_bags
                queue.pop()

    # -1 because you want to know how many bags the starting bag must contain
    return nodes_number_of_bags[starting_node] - 1


def main():
    input_lines = read_file()

    inverted_graph = build_inverted_graph(input_lines)
    list_reachable_nodes = dfs_reachable_nodes(inverted_graph, 'shiny-gold')
    print(str(len(list_reachable_nodes)-1))

    weighted_graph = build_weighted_graph(input_lines)
    print(dfs_number_of_bags(weighted_graph, 'shiny-gold'))


if __name__ == '__main__':
    main()
