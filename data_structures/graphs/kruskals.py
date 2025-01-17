from collections import defaultdict
from typing import Dict,List,Set

from data_structures.graphs.disjoint_set import DisjointSet


class GraphEdge:
    def __init__(self,w,d,s):
        self.w = w
        self.d = d
        self.s = s


    def __lt__(self, other):
        return self.w < other.w

    def __eq__(self, other):
        return self.s == other.s and self.d == other.d

    def __repr__(self):
        return f"|s={self.s},d={self.d},w={self.w}|"

class Graph:
    def __init__(self):
        self.adj_list :Dict[int, List[GraphEdge]] = defaultdict(list)
        self.vertices :Set[int] = set()

    def get_vertices(self):
        return self.vertices

    def get_edges(self,s):
        return self.adj_list[s]

    def get_all_edges(self):
        all_edges :List[GraphEdge] = []
        for vertex in self.vertices:
            all_edges.extend(self.adj_list[vertex])

        return all_edges

    def add_edge(self,s,d,w):
        self.vertices.add(s)
        self.vertices.add(d)

        self.adj_list[s].append(GraphEdge(s=s,d=d,w=w))
        self.adj_list[d].append(GraphEdge(s=d,d=s,w=w))

    def mst_kruskals(self):
        all_edges = self.get_all_edges()
        list.sort(all_edges)

        ds = DisjointSet(size = len(self.vertices))
        mst = []
        for edge in all_edges:
            source_parent = ds.find(edge.s)
            dest_parent = ds.find(edge.d)

            if source_parent != dest_parent:
                ds.union(source_parent, dest_parent)
                mst.append(edge)
        return mst




    def print_graph(self):
        for vertex in self.vertices:
            print(f"{vertex} => {self.adj_list[vertex]}")

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
mst = graph_for_mst.mst_kruskals()
print(mst)



