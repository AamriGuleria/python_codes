
from typing import List
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        count = 0
        rows,cols = len(grid),len(grid[0])
        def dfs(x, y):
            stack = [(x, y)]
            grid[x][y] = 0
            while stack:
                p, q = stack.pop()
                for dx, dy in directions:
                    nx, ny = p+dx, q+dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 0
                        stack.append((nx, ny))

        for i in range(rows):
            for j in range(cols):
                if (i == 0 or i == rows-1 or j == 0 or j == cols-1) and grid[i][j] == 1:
                    dfs(i, j)
        return sum(row.count(1) for row in grid)