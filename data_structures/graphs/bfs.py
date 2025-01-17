from typing import Dict, List, Set
from collections import defaultdict, deque


class GraphEdge:
    def __init__(self,s,d,w):
        self.s = s
        self.d = d
        self.w = w

    def __lt__(self, other):
        return self.w < other.w

    def __repr__(self):
        return f"s:{self.s},d:{self.d},w:{self.w}"


class Graph:
    def __init__(self):
        self.adj_list : Dict[int, List[GraphEdge]] = defaultdict(list)
        self.vertices : Set[int] = set()

    def add_vertex(self, v):
        self.vertices.add(v)

    def add_edge(self,s,d,w):
        self.add_vertex(s)
        self.add_vertex(d)
        self.adj_list[s].append(GraphEdge(s=s,d=d,w=w))
        self.adj_list[d].append(GraphEdge(s=d,d=s,w=w))

    def print_graph(self):
        for v in self.vertices:
            print(f"{v}-> {self.adj_list[v]}")

    def get_edges(self,v):
        return self.adj_list[v]


    def graph_bfs(self, start_from):
        q = deque()
        bfs = []
        already_added_in_queue = [False] * len(self.vertices)
        q.append(start_from)
        already_added_in_queue[start_from] = True

        while q:
            vertex = q.popleft()
            bfs.append(vertex)
            edges = self.get_edges(vertex)
            for edge in edges:
                if not already_added_in_queue[edge.d]:
                    q.append(edge.d)
                    already_added_in_queue[edge.d] = True

        print(bfs)

graph = Graph()
graph.add_edge(0,2,1)
graph.add_edge(0,5,2)

graph.add_edge(1,2,1)
graph.add_edge(1,3,3)

graph.add_edge(2,3,3)
graph.add_edge(2,4,1)
graph.add_edge(2,5,2)

graph.add_edge(3,4,1)

graph.add_edge(4,5,5)
graph.graph_bfs(0)
