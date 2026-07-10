from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return_val = False
        row = len(board)
        cols = len(board[0])
        def backtrack_approach(i , j , word):
            nonlocal return_val
            if return_val:
                return
            if i < 0 or i >= row or j < 0 or j >= cols:
                return
            if board[i][j] != word[0]:
                return

            if len(word) == 1:
                return_val = True
                return
            temp = board[i][j]
            board[i][j] = "#"
            backtrack_approach(i+1, j, word[1:])
            backtrack_approach(i-1, j, word[1:])
            backtrack_approach(i, j+1, word[1:])
            backtrack_approach(i, j-1, word[1:])
            board[i][j] = temp

        for i in range(row):
            for j in range(cols):
                if return_val:
                    return True
                backtrack_approach(i, j, word)
        return return_val