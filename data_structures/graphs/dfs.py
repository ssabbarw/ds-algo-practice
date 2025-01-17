from collections import defaultdict
from typing import Dict, List, Set
class Graph:

    def __init__(self):
        self.adj_list : Dict[int, Set[int]]= defaultdict(set)
        self.vertices : Set[int] = set()

    def add_edge(self, s, d):
        self.vertices.add(s)
        self.vertices.add(d)

        self.adj_list[s].add(d)
        self.adj_list[d].add(s)


    def print_dfs_recur(self, start, visited, dfs):
        visited.add(start)

        for edge_vertex in self.adj_list[start]:
            if not edge_vertex in visited:
                self.print_dfs_recur(edge_vertex, visited, dfs)

        dfs.append(start)

    def print_dfs(self):
        start = next(iter(self.vertices))
        visited = set()
        dfs = []

        self.print_dfs_recur(start, visited, dfs)
        print(dfs)


graph = Graph()
graph.add_edge(0,2)
graph.add_edge(0,5)

graph.add_edge(1,2)
graph.add_edge(1,3)

graph.add_edge(2,3)
graph.add_edge(2,4)
graph.add_edge(2,5)

graph.add_edge(3,4)

graph.add_edge(4,5)
graph.print_dfs()


