from collections import deque
from typing import List

class Solution:

    def __init__(self):
        self.count = 0

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        result: List[List[int]] = []
        bfs_q = deque()

        for row in range(len(mat)):
            result.append([None] * len(mat[0]))
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    bfs_q.append((row, col))
                    result[row][col] = 0
                else:
                    result[row][col] = -1

        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        while bfs_q:
            cur_row, cur_col = bfs_q.popleft()
            for row_add, col_add in directions:
                new_row = cur_row + row_add
                new_col = cur_col + col_add

                if (0 <= new_row < len(mat) and 0 <= new_col < len(mat[0])
                        and result[new_row][new_col] == -1):
                    result[new_row][new_col] = result[cur_row][cur_col] + 1
                    bfs_q.append((new_row, new_col))

        return result

sol = Solution()
print((sol.updateMatrix([[0,0,0],[0,1,0],[1,1,1]])))

