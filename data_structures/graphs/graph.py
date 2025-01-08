class Graph:
    def __init__(self):
        self.adj_list = {}


    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex,":",self.adj_list[vertex])

        print("Graph printed")

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)
            return True
        return False

    def remove_edge(self,vertex1,vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            try:
                self.adj_list[vertex1].remove(vertex2)
                self.adj_list[vertex2].remove(vertex1)
                return True

            except ValueError:
                pass
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            list_of_edges = self.adj_list[vertex]
            for edge in list_of_edges:
                self.adj_list[edge].remove(vertex)
            self.adj_list.pop(vertex)
            return True
        return False

graph = Graph()
graph.print_graph()
graph.add_vertex("a")
graph.add_vertex("b")
graph.add_vertex("c")
graph.add_edge("a","b")
graph.add_edge("b","c")
graph.print_graph()
graph.remove_vertex("a")
graph.print_graph()