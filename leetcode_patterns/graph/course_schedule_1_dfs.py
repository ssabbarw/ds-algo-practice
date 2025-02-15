from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = []
        visited = set()
        stack = []

        for i in range(numCourses):
            graph.append([])

        for course, pre_req in prerequisites:
            graph[pre_req].append(course)

        def dfs(graph, node, visited, stack):
            print(node, visited)
            visited.add(node)
            neighbours = graph[node]

            for neighbour in neighbours:
                if neighbour not in visited:
                    dfs(graph, neighbour, visited, stack)

            stack.append(node)

        for i in range(numCourses):
            if i not in visited:
                dfs(graph, i, visited, stack)


        print(stack)

        return len(stack) == numCourses

print(Solution().canFinish(numCourses=2,prerequisites=[[1,0],[0,1]]))