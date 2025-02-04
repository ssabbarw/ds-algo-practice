from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = []
        for i in range(len(grid)):
            visited.append([0] * len(grid[0]))

        islands = 0

        def dfs(grid, visited, row, col):
            if row >= len(grid) or row < 0 or col >= len(grid) or col < 0 or grid[row][col] == "0" or visited[row][col]:
                return

            visited[row][col] = 1

            dfs(grid, visited, row - 1, col)
            dfs(grid, visited, row + 1, col)
            dfs(grid, visited, row, col - 1)
            dfs(grid, visited, row, col + 1)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if not visited[row][col] and grid[row][col] == "1":
                    islands += 1
                    dfs(grid, visited, row, col)

        return islands



print(Solution().numIslands( [["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]]))