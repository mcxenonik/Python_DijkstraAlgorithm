import argparse
import string
from node import Node
from pqdict import PQDict


def read_table_from_file(filename):
    with open(filename, "r") as file:
        table_str = ""

        for line in file:
            table_str += line.replace("\n", "")

        table = [int(value) for value in table_str]
        table_width = len(line)

    return table, table_width


def build_graph(table, table_width):
    number_of_nodes = len(table)
    end_nodes = []
    graph = {}

    for id in range(number_of_nodes):
        node = Node(id, table[id])
        graph[node.id] = []

        if(node.value == 0):
            end_nodes.append(node)

        for j in range(0, 4):
            if (j == 0 and ((id + 1) % table_width != 0) and id + 1 < number_of_nodes):
                neighbour = Node(id + 1, table[id + 1])
                graph[node.id].append(neighbour)

            elif (j == 1 and id + table_width < number_of_nodes):
                neighbour = Node(id + table_width, table[id + table_width])
                graph[node.id].append(neighbour)

            elif (j == 2 and (id % table_width != 0) and id - 1 >= 0):
                neighbour = Node(id - 1, table[id - 1])
                graph[node.id].append(neighbour)

            elif (j == 3 and id - table_width >= 0):
                neighbour = Node(id - table_width, table[id - table_width])
                graph[node.id].append(neighbour)

    return graph, end_nodes


def dijkstra_algorithm(start_node, end_node, graph):
    distance = {}
    distance[start_node.id] = 0

    queueDijkstra = PQDict()
    queueDijkstra[start_node.id] = 0

    previous_on_path = {}

    while (len(queueDijkstra) > 0):
        node_id, _ = queueDijkstra.popitem()

        for neighbour in graph[node_id]:
            if (neighbour.id not in distance or distance[neighbour.id] > distance[node_id] + neighbour.value):
                distance[neighbour.id] = distance[node_id] + neighbour.value
                previous_on_path[neighbour.id] = node_id
                queueDijkstra[neighbour.id] = distance[neighbour.id]

    shortest_path = []
    current_node_id = end_node.id

    while (current_node_id != start_node.id):
        shortest_path.append(current_node_id)
        current_node_id = previous_on_path[current_node_id]

    shortest_path.append(start_node.id)
    shortest_path.reverse()

    return shortest_path


def prepare_result(table, table_width, shortest_path):
    result = ""
    for id in range(len(table)):
        if (id in shortest_path):
            result += str(table[id])
        else:
            result += " "

        if ((id + 1) % table_width == 0):
            result += "\n"

    return result


# def prepare_result2(table_list, list_of_nodes, shortest_path, table_width):
#     result = ""

#     for node_id in shortest_path:
#         table_list[node_id] = "*"

#     for id in range(len(table_list)):
#        if ((id + 1) % table_width == 0):
#            table_list.insert(id + 1, "\n")

#     return result.join(table_list)


def prepare_result2(table, table_width, shortest_path):
    result = ""
    for id in range(len(table)):
        if (id in shortest_path):
            result += str(table[id])
        else:
            result += " "

        if ((id + 1) % table_width == 0):
            result += "\n"

    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dijkstra Algorithm")
    parser.add_argument("filename", help="Name of file to load")
    args = parser.parse_args()

    table, table_width = read_table_from_file(args.filename)

    graph, end_nodes = build_graph(table, table_width)

    shortest_path = dijkstra_algorithm(end_nodes[0], end_nodes[1], graph)

    # result = prepare_result(table, table_width, shortest_path)
    result = prepare_result2(table, table_width, shortest_path)
 
    print(result)
