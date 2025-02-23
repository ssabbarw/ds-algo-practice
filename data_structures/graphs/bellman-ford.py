class Solution:
    '''
    Function to implement Bellman Ford
    V: nodes in graph
    edges: adjacency list for the graph
    src: source vertex
    '''

    def bellmanFord(self, V, edges, src):

        INF = 10 ** 8

        weights = [INF] * V
        weights[src] = 0

        for _ in range(V - 1):
            for u, v, w in edges:
                if weights[u] != INF and weights[u] + w < weights[v]:
                    weights[v] = weights[u] + w
                    return True

        for u, v, w in edges:
            if weights[u] != INF and weights[u] + w < weights[v]:
                # negative weight cycle found
                return {-1}

        return weights