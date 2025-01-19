def dfs(matrix, row, col):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]) or matrix[row][col] != 1:
        return

    matrix[row][col] = 0
    dfs(matrix, row -1, col)
    dfs(matrix, row + 1, col)
    dfs(matrix, row , col - 1)
    dfs(matrix, row , col + 1)

input_matrix = [["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]]

def find_islands(matrix):
    n = len(matrix)
    m = len(matrix[0])
    islands = 0
    for row in range(n):
        for col in range(m):
            if matrix[row][col] == 1:
                islands += 1
                dfs(matrix, row, col)
    print(islands)

find_islands(input_matrix)

