import string
from heapq import heappush, heappop
from collections import defaultdict, namedtuple
from typing import List, Set, Dict, Tuple
import random


class Edge:
    def __init__(self,s,d,w):
        self.s = s
        self.d = d
        self.w = w

    def __lt__(self, other):
        return self.w < other.w

    def __gt__(self, other):
        return self.w > other.w

    def __repr__(self):
        return f"s:{self.s},d:{self.d},w:{self.w}"

class Graph:
    def __init__(self):
        self.adj_list: Dict[int, List[Tuple[Edge]]] = defaultdict(list)
        self.vertices : Set[int] = set()


    def add_edge(self,s,d,w):
        self.vertices.add(s)
        self.vertices.add(d)
        self.adj_list[s].append(Edge(s,d,w))
        self.adj_list[d].append(Edge(d,s,w))

    def get_edges(self,s) -> List[Edge]:
        return self.adj_list[s]

    def get_all_vertices(self) -> Set[int]:
        return self.vertices

    def print_graph(self):
        for vertex in self.vertices:
            vertex_str = ""
            for edge in self.adj_list[vertex]:
                vertex_str += f"d={edge.d}w={edge.w},"

            print(f"{vertex}->{vertex_str}")



    def minimum_spanning_tree(self) ->List[Edge]:
        pq = []
        visited = set()
        mst: List[Edge] = []

        chosen =  next(iter(self.vertices))

        edges = self.get_edges(chosen)
        visited.add(chosen)

        for edge in edges:
            heappush(pq, edge)

        while pq and len(visited) < len(self.vertices):
            '''
                These two conditions serve different but important purposes in Prim's algorithm. Let me explain each one:
                pq (first condition):
                
                Checks if the priority queue still has edges to process
                If pq becomes empty but we haven't visited all vertices, it means the graph is disconnected
                Without this check, we'd get an error trying to heappop from an empty queue len(visited) < len(self.vertices):
                
                Checks if we've visited all vertices in the graph
                Once we've visited all vertices, we've found our complete MST and can stop
                Without this check, we might process unnecessary edges after finding the MST
            '''
            chosen_edge = heappop(pq)
            if visited.__contains__(chosen_edge.d):
                continue

            visited.add(chosen_edge.d)
            mst.append(chosen_edge)

            for edge in self.adj_list[chosen_edge.d]:
                heappush(pq, edge)

        return mst








graph_for_mst = Graph()

graph_for_mst.add_edge(0,2,1)
graph_for_mst.add_edge(0,5,2)

graph_for_mst.add_edge(1,2,1)
graph_for_mst.add_edge(1,3,3)

graph_for_mst.add_edge(2,3,3)
graph_for_mst.add_edge(2,4,1)
graph_for_mst.add_edge(2,5,2)

graph_for_mst.add_edge(3,4,1)

graph_for_mst.add_edge(4,5,5)
graph_for_mst.print_graph()

mst = graph_for_mst.minimum_spanning_tree()
for edge in mst:
    print(edge)
