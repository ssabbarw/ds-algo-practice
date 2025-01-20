import math
from heapq import heappush, heappop
from typing import List, Set, Dict
from collections import defaultdict, namedtuple

class GraphNode:
    def __init__(self,dest,weight):
        self.dest = dest
        self.weight = weight

    def __eq__(self, other):
        if not isinstance(other, GraphNode):
            return NotImplemented

        return self.dest == other.dest

    def __repr__(self):
        return f"d={self.dest},w={self.weight}"

    def __str__(self):
        return f"str:- d={self.dest},w={self.weight}"

class Graph:
    def __init__(self):
        self.adj_list : Dict[int, List[GraphNode]] = defaultdict(list)
        self.vertices : Set[int] = set()

    def add_vertex(self, vertex):
        self.vertices.add(vertex)

    def add_edge(self,vertex1, vertex2, weight):
        if weight < 0:
            raise  ValueError("Negative weights not allowed in Dijkstra's algo")

        if vertex1 == vertex2:
            raise ValueError("Self loops not allowed")

        if vertex2 in self.adj_list[vertex1]:
            raise ValueError("Edge exists already")

        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        self.adj_list[vertex1].append(GraphNode(dest = vertex2, weight = weight))
        self.adj_list[vertex2].append(GraphNode(dest = vertex1, weight = weight))

    def print_graph(self):
        for vertex in self.vertices:
            print(f"{vertex}=> {self.adj_list[vertex]}")

    def run_dijkstra_algo(self, start=None):

        priority_queue = []
        parent_array = [None] * len(self.vertices)
        weights = [math.inf] * len(self.vertices)
        visited = set()

        if not start:
            start = next(iter(self.vertices))

        WeightedNode = namedtuple("WeightedNode" , ("weight", "node"))

        weights[start] = 0
        parent_array[start] = None
        heappush(priority_queue, WeightedNode(weights[start],start))

        while priority_queue:
            minimum_weighted_node :WeightedNode = heappop(priority_queue)
            if minimum_weighted_node.node in visited:
                continue

            visited.add(minimum_weighted_node.node)

            for edge in self.adj_list[minimum_weighted_node.node]:
                if weights[edge.dest] > minimum_weighted_node.weight + edge.weight:
                    parent_array[edge.dest] = minimum_weighted_node.node
                    weights[edge.dest] = minimum_weighted_node.weight + edge.weight
                    heappush(priority_queue, WeightedNode(weights[edge.dest],edge.dest))

        return parent_array, weights


    def print_shortest_path(self,source,destination):
        parent_array, weights_array = self.run_dijkstra_algo(source)
        current = destination
        path = []

        while True:
            if current is not None:
                path.append(current)
                current = parent_array[current]
            else:
                return path[::-1]

        return path



graph = Graph()
graph.add_edge(0,2,4)
graph.add_edge(0,1,4)
graph.add_edge(1,2,2)
graph.add_edge(2,3,10)
graph.add_edge(2,4,1)
graph.add_edge(2,5,6)
graph.add_edge(3,5,2)
graph.add_edge(4,5,3)

graph.print_graph()
print(graph.print_shortest_path(source=2,destination=3))

