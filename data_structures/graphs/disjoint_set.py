class DisjointSet:
    def __init__(self):
        self.parent = {}
        self.ranks = {}

    def make_set(self, node):
        if node not in self.parent:
            self.parent[node] = node
            self.ranks[node] = 0

    def find(self, node):
        if node not in self.parent:
            raise ValueError(f"Node {node} not found in any set")

        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # Path compression
        return self.parent[node]

    def union(self, node1, node2):
        if node1 not in self.parent or node2 not in self.parent:
            raise ValueError("One or both nodes not found in any set")

        parent1 = self.find(node1)
        parent2 = self.find(node2)

        if parent1 == parent2:
            return

        if self.ranks[parent1] < self.ranks[parent2]:
            self.parent[parent1] = parent2
        elif self.ranks[parent1] > self.ranks[parent2]:
            self.parent[parent2] = parent1
        else:
            self.parent[parent2] = parent1
            self.ranks[parent1] += 1