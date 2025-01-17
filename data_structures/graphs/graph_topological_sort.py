from collections import defaultdict, deque
from typing import List,Dict,Tuple

class GraphEdge:
    def __init__(self,s,d):
        self.s = s
        self.d = d

    def __repr__(self):
        return f"s{self.s}d{self.d}"

class Graph:
    def __init__(self):
        self.adj_list: Dict[int, List[GraphEdge]] = defaultdict(list)
        self.vertices = set()

    def add_vertex(self,v):
        self.vertices.add(v)

    def get_vertices(self):
        return self.vertices

    def get_edges(self,s):
        return self.adj_list[s]


    def add_edge(self,s,d):
        self.add_vertex(s)
        self.add_vertex(d)
        self.adj_list[s].append(GraphEdge(s,d))

    def print_topological(self):
        vertices_list = list(self.vertices)
        in_degrees = [0]  * len(self.vertices)

        for vertex in self.vertices:
            for edge in self.get_edges(vertex):
                in_degrees[edge.d] += 1

        queue = deque()
        result = []

        for i in range(len(in_degrees)):
            if in_degrees[i] == 0:
                queue.append(vertices_list[i])
                result.append(vertices_list[i])

        while queue:
            current = queue.popleft()
            for edge in self.get_edges(current):
                in_degrees[edge.d] -= 1

                if not in_degrees[edge.d]:
                    queue.append(edge.d)
                    result.append(edge.d)

        # If result contains all vertices, it's a valid topological sort
        if len(result) == len(self.vertices):
            print(f"sorted {result}")
        else:
            return print(None)  # Graph has a cycle


    def print_graph(self):
        for vertex in self.vertices:
            vertex_str = ""
            for edge in self.adj_list[vertex]:
                vertex_str += f"d={edge.d},"

            print(f"{vertex}->{vertex_str}")



graph_for_mst = Graph()

graph_for_mst.add_edge(0,2,)
graph_for_mst.add_edge(0,5)

graph_for_mst.add_edge(1,2)
graph_for_mst.add_edge(1,3)

graph_for_mst.add_edge(2,3)
graph_for_mst.add_edge(2,4)
graph_for_mst.add_edge(2,5)

graph_for_mst.add_edge(3,4)

graph_for_mst.add_edge(4,5)
graph_for_mst.print_graph()

graph_for_mst.print_topological()

