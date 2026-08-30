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