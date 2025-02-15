from typing import List
from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        set1 = set()
        set2 = set()

        q = deque()

        q.append(0)
        visited_set = set()

        while q:
            source = q.popleft()

            if not source in visited_set:
                visited_set.add(source)

            edges = graph[source]
            for dest in edges:
                if dest in visited_set:
                    continue
                q.append(dest)
                if (source in set1 and dest in set1) or (source in set2 and dest in set2):
                    return False

                if source in set1 or source in set2:
                    if source in set1:
                        set2.add(dest)

                    if source in set2:
                        set1.add(dest)
                else:
                    if dest in set1:
                        set2.add(source)
                    else:
                        set1.add(source)



        return True


print(Solution().isBipartite([[4,1],[0,2],[1,3],[2,4],[3,0]]))

