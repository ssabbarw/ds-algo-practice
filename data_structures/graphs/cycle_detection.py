from typing import Set, List, Dict
from collections import defaultdict, deque, namedtuple


class Graph:
    def __init__(self):
        self.adj_list: Dict[int, Set[int]] = defaultdict(set)
        self.vertices :Set[int] = set()

    def add_vertex(self,v):
        self.vertices.add(v)

    def add_edge(self, s, d):
        if s == d:
            raise ValueError("Self loops not allowed")
        if d in self.adj_list[s]:
            raise ValueError("Duplicate edges not allowed")

        self.add_vertex(s)
        self.add_vertex(d)

        self.adj_list[s].add(d)
        self.adj_list[d].add(s)

    def print_graph(self):
        for vertex in self.vertices:
            print(f"{vertex} => {self.adj_list[vertex]}")

    def check_cycle_with_bfs(self):
        visited = set()

        for vertex in self.vertices:
            if vertex not in visited:
                if self.bfs_cycle(visited,vertex):
                    return True

        return False

    def bfs_cycle(self, visited, start):
        visited.add(start)

        ParentChild = namedtuple("ParentChild", ("parent", "child"))
        q = deque()
        q.append(ParentChild(None, start))
        while q:
            q_pop = q.popleft()
            current_vertex = q_pop.child
            parent_of_current = q_pop.parent

            for edge_dest in self.adj_list[current_vertex]:

                if edge_dest in visited and edge_dest != parent_of_current:
                    return True

                if edge_dest not in visited:
                    visited.add(edge_dest)
                    q.append(ParentChild(current_vertex, edge_dest))
        return  False

    def dfs_print(self, start = None):
        stack :List[int]= []
        visited :Set[int] = set()
        dfs_result: List[int] = []

        for vertex in self.vertices:
            if vertex not in visited:
                stack.append(vertex)
                while stack:
                    current = stack.pop()
                    if current not in visited:
                        visited.add(current)
                        dfs_result.append(current)

                    for edge in self.adj_list[current]:
                        if edge not in visited:
                            stack.append(edge)

                print(dfs_result)

    def check_cycle_with_dfs(self):
        visited : Set[int] = set()
        NodeWithParent = namedtuple('CurrentParent', ('current', 'parent'))

        if not self.vertices:
            print("Graph is empty. No cycles to detect.")
            return False

        for vertex in self.vertices:
            if vertex in visited:
                continue
            stack :List[int]= [NodeWithParent(vertex,None)]

            while stack:
                current_node,parent_node = stack.pop()

                if current_node not in visited:
                    visited.add(current_node)

                for edge in self.adj_list[current_node]:
                    if edge not in visited:
                        stack.append(NodeWithParent(edge,current_node))
                    elif edge != parent_node:
                        return True

        return False




graph = Graph()
graph.add_edge(0,1)
graph.add_edge(1,3)
graph.add_edge(3,4)
graph.add_edge(4,5)
graph.add_edge(5,7)
graph.add_edge(7,6)
graph.add_edge(6,2)
graph.add_edge(2,0)
graph.add_edge(2,8)
graph.add_edge(8,9)
graph.add_edge(9,6)


print(graph.check_cycle_with_dfs())