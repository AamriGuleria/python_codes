from collections import deque
from typing import List
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        if grid[0][0] != 0 or grid[n-1][m-1] != 0:
            return -1
        if n == 1 and m == 1:
            return 1
        directions = [(1,0),(-1,0),(0,1),(0,-1),(-1,1),(-1,-1),(1,-1),(1,1)]
        queue = deque([(0, 0, 1)])  
        grid[0][0] = "#"
        while queue:
            i, j, path_len = queue.popleft()
            for dx, dy in directions:
                nx, ny = i + dx, j + dy
                if nx < 0 or nx > n-1 or ny < 0 or ny > m-1 or grid[nx][ny] != 0:
                    continue
                if nx == n-1 and ny == m-1:
                    return path_len + 1
                grid[nx][ny] = "#"
                queue.append((nx, ny, path_len + 1))

        return -1
