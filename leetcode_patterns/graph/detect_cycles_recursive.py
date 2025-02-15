from collections import defaultdict
from typing import List, Dict, Set
class Graph:
    def __init__(self):
        self.graph: Dict[int, List] = defaultdict(list)
        self.vertices  :Set[int] = set()


    def add_edge(self, source, dest):
        if source == dest:
            raise ValueError("Self loop detected")

        self.vertices.add(source)
        self.vertices.add(dest)

        self.graph[source].append(dest)
        self.graph[dest].append(source)

    def print_graph(self):
        for vertex in self.vertices:
            print(f"{vertex}->{self.graph[vertex]}")

    def dfs_iterative(self, node):
        if node not in self.vertices:
            raise ValueError("Node does not exits")

        stack = [node]
        visited = set()
        result  = []

        while stack:

            print(stack)
            curr = stack.pop()

            if curr not in visited:
                result.append(curr)
                visited.add(curr)
            else:
                continue

            neighbours = self.graph[curr]

            for neighbour in neighbours:
                if neighbour not in visited:
                    stack.append(neighbour)

        return result




graph = Graph()
graph.add_edge(1,2)
graph.add_edge(1,4)
graph.add_edge(2,3)
graph.add_edge(2,4)
graph.add_edge(3,5)
graph.add_edge(5,4)
graph.print_graph()
print("\n")
print(graph.dfs_iterative(2))


