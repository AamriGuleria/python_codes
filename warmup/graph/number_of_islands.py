from collections import deque
from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        island = 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1":
                    queue.append((i,j))
                    grid[i][j]=-1
                    island+=1
                    while queue:
                        x,y = queue.popleft()
                        for dx,dy in directions:
                            nx,ny = x+dx,y+dy
                            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == "1":
                                grid[nx][ny] = "-1"
                                queue.append((nx,ny))
        return island