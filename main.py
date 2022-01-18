import argparse
import string
from node import Node
from pqdict import PQDict


def read_table_from_file(filename):
    with open(filename, "r") as file:
        text_graph = ""

        for line in file:
            text_graph += line.replace("\n", "")

        table_width = len(line)

    return text_graph, table_width


def build_graph(text_graph, table_width):
    num_of_nodes = len(text_graph)
    list_of_nodes = []
    end_nodes = []
    graph = {}

    for i in range(num_of_nodes):
        node = Node(i, int(text_graph[i]))
        list_of_nodes.append(node)
        graph[node.id] = []

        if(node.value == 0):
            end_nodes.append(node.id)

        for j in range(0, 4):
            if(j == 0 and ((i + 1) % table_width != 0) and i + 1 < num_of_nodes):
                neighbour = Node(i + 1, int(text_graph[i + 1]))
                graph[node.id].append((neighbour.id, neighbour.value))

            elif(j == 1 and i + table_width < num_of_nodes):
                neighbour = Node(i + table_width, int(text_graph[i + table_width]))
                graph[node.id].append((neighbour.id, neighbour.value))

            elif(j == 2 and (i % table_width != 0) and i - 1 >= 0):
                neighbour = Node(i - 1, int(text_graph[i - 1]))
                graph[node.id].append((neighbour.id, neighbour.value))

            elif(j == 3 and i - table_width >= 0):
                neighbour = Node(i - table_width, int(text_graph[i - table_width]))
                graph[node.id].append((neighbour.id, neighbour.value))

    return graph, list_of_nodes, end_nodes


def shortest_path_dijkstra(start_node, end_node, graph):
    dist = {}
    dist[start_node] = 0

    queueDijkstra = PQDict()
    queueDijkstra[start_node] = 0

    prev_on_path = {}

    while (len(queueDijkstra) > 0):
        v, _ = queueDijkstra.popitem()

        for neighbour, cost in graph[v]:
            if (neighbour not in dist or dist[neighbour] > dist[v] + cost):
                dist[neighbour] = dist[v] + cost
                prev_on_path[neighbour] = v
                queueDijkstra[neighbour] = dist[neighbour]

    shortest_path = []
    current_node = end_node

    while current_node != start_node:
        shortest_path.append(current_node)
        current_node = prev_on_path[current_node]

    shortest_path.append(start_node)
    shortest_path.reverse()

    return shortest_path


def prepare_result(list_of_nodes, shortest_path, table_width):
    result = ""
    for node in list_of_nodes:
        if (node.id in shortest_path):
            result += str(node.value)
        else:
            result += " "

        if ((node.id + 1) % table_width == 0):
            result += "\n"

    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dijkstra Algorithm")
    parser.add_argument("filename", help="Name of file to load")
    args = parser.parse_args()

    table, table_width = read_table_from_file(args.filename)

    graph, list_of_nodes, end_nodes = build_graph(table, table_width)

    shortest_path = shortest_path_dijkstra(end_nodes[0], end_nodes[1], graph)

    result = prepare_result(list_of_nodes, shortest_path, table_width)
 
    print(result)
