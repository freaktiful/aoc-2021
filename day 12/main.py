from collections import defaultdict, Counter


def not_repeated_more_than_once(node, path):
    if node not in path:
        return True
    if node == 'start':
        return False
    else:
        aux = [(k, v) for k, v in Counter(path).items() if
               (k.islower() and (k != node) and (v > 1)) or ((k == node) and (v == 2))]
        return len(aux) == 0


class Graph(object):
    """ Undirected graph data structure """

    _graph = defaultdict(set)

    _paths = []

    _part = 1

    def __init__(self, connections, part):
        self._graph = defaultdict(set)
        self._part = part
        self._paths = []
        self.add_connections(connections)

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """
        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """
        self._graph[node1].add(node2)
        self._graph[node2].add(node1)

    def is_connected(self, node1, node2):
        """ Is node1 connected to node2 """
        return node1 in self._graph and node2 in self._graph[node1]

    def find_all_paths_recursive(self, u, d, path):
        """Function to find all paths from 'u' to 'd'."""
        path.append(u)
        # If current vertex is same as destination, then add path to path array
        if u == d:
            self._paths.append(path)
        else:
            # If current vertex is not destination
            # Recur for all the vertices accessible to this vertex
            for i in self.graph[u]:
                if (self._part == 1) and (i.isupper() or (i.islower() and i not in path)):
                    self.find_all_paths_recursive(i, d, path)
                if (self._part == 2) and (i.isupper() or (i.islower() and not_repeated_more_than_once(i, path))):
                    self.find_all_paths_recursive(i, d, path)
        # Remove current vertex from path
        path.pop()

    # Finds all paths from 's' to 'd'
    def find_all_paths(self, s, d):
        # Create an array to store paths
        path = []
        # Call the recursive helper function to find all paths
        self.find_all_paths_recursive(s, d, path)

    def return_number_of_paths(self):
        return(len(self._paths))

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))

    @property
    def graph(self):
        return self._graph


def format_input(name):
    output = []
    with open(name, 'r') as file:
        lines = file.read().split('\n')
        for line in lines:
            connection = line.split('-')
            output.append(connection)
    return output


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    formatted_input = format_input('input.txt')

    g = Graph(formatted_input, 1)
    g.find_all_paths('start', 'end')
    print(g.return_number_of_paths())

    g2 = Graph(formatted_input, 2)
    g2.find_all_paths('start', 'end')
    print(g2.return_number_of_paths())
