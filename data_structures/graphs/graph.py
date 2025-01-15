class GraphEdge:
    def __init__(self,weight, destination):
        self.weight = weight
        self.destination = destination

    def __repr__(self):
        return f"dest: {self.destination}, w = {self.weight}"

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

    def add_edge(self, vertex1, vertex2, weight = 1):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1].append(GraphEdge(destination=vertex2,weight=weight))
            self.adj_list[vertex2].append(GraphEdge(destination=vertex1,weight=weight))
            return True
        return False

    def remove_edge(self, parent, edge):
        if parent in self.adj_list and edge.destination in self.adj_list:
            list_of_edges_of_parent = self.adj_list[parent]
            list_of_edges_of_destination_vertex = self.adj_list[edge.destination]
            list_of_edges_of_parent = [graph_node for graph_node in list_of_edges_of_parent if graph_node.destination != edge.destination]
            list_of_edges_of_destination_vertex = [graph_node for graph_node in list_of_edges_of_destination_vertex if graph_node.destination != parent]

            self.adj_list[parent] = list_of_edges_of_parent
            self.adj_list[edge.destination] = list_of_edges_of_destination_vertex

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            list_of_edges = self.adj_list[vertex]
            for edge in list_of_edges:
                self.remove_edge(vertex, edge)
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