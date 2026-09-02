from typing import List
class Solution:
    def __init__(self):
        self.rows = None
        self.cols = None
    def recursive_search(self, mat, i, j, memo, visiting):
        if i < 0 or i >= self.rows or j < 0 or j >= self.cols:
            return float('inf')
        if mat[i][j] == 0:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]
        if (i, j) in visiting:
            return float('inf')

        visiting.add((i, j))
        down = 1 + self.recursive_search(mat, i+1, j, memo, visiting)
        up = 1 + self.recursive_search(mat, i-1, j, memo, visiting)
        left = 1 + self.recursive_search(mat, i, j-1, memo, visiting)
        right = 1 + self.recursive_search(mat, i, j+1, memo, visiting)
        visiting.remove((i, j))

        result = min(down, up, left, right)
        memo[(i, j)] = result
        return result
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        self.rows, self.cols = len(mat), len(mat[0])
        new_mat = [[-1] * self.cols for _ in range(self.rows)]
        memo = {}
        for i in range(self.rows):
            for j in range(self.cols):
                if mat[i][j] == 0:
                    new_mat[i][j] = 0
                else:
                    new_mat[i][j] = self.recursive_search(mat, i, j, memo, set())
        return new_mat
    

from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows , cols = len(mat),len(mat[0])
        queue = deque()
        dist = [[-1] * cols for _ in range(rows)]
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i, j))

        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
        return dist