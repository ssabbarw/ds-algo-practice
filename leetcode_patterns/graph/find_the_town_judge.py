from random import triangular
from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_given = [0] * (n+1)
        trust_received = [0] * (n+1)

        for t in trust:
            trust_given[t[0]] += 1
            trust_received[t[1]] += 1

        for i in range(1, n+1):
            if trust_given[i] == 0 and trust_received[i] == n - 1:
                return i

        return -1



print(Solution().findJudge(n = 3, trust = [[1,3],[2,3]]))