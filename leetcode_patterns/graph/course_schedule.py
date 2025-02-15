import heapq
from collections import defaultdict
from typing import Dict,List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indegree_map = defaultdict(int)

        adj_list = {}
        for i in range(numCourses):
            adj_list[i] = []
            indegree_map[i] = 0

        for pre_req in prerequisites:
            # prerequisites = [[1,0]]
            course, required_course = pre_req[0], pre_req[1]
            adj_list[required_course].append(course)
            indegree_map[course] += 1

        heap = [(item[1], item[0]) for item in indegree_map.items()]
        heapq.heapify(heap)

        print("heap", heap)

        while heap:
            heap_top = heapq.heappop(heap)

            course = heap_top[1]
            if heap_top[0] != 0:
                return False

            list_of_dependent_courese = adj_list[course]
            del indegree_map[course]


            for dependent_course in list_of_dependent_courese:
                indegree_map[dependent_course] -= 1

            heap = [(item[1], item[0]) for item in indegree_map.items()]
            heapq.heapify(heap)

        return True

print(Solution().canFinish(2, [[1,0],[0,1]]))