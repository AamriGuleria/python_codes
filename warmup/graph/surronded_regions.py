from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows , cols = len(board),len(board[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        def dfs(x,y):
            stack = [(x,y)]
            board[x][y]="#"
            while stack:
                p,q = stack.pop()
                for dx,dy in directions:
                    nx,ny = p+dx,q+dy
                    if 0<nx<rows and 0<ny<cols and board[nx][ny]=="O":
                        board[nx][ny]="#"
                        stack.append((nx,ny))

        for i in range(rows):
            for j in [0, cols-1]:
                if board[i][j] == "O":
                    dfs(i, j)
        for j in range(cols):
            for i in [0, rows-1]:
                if board[i][j] == "O":
                    dfs(i, j)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"

