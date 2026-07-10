from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        final = []
        def backtrack(start, temp, remaining_k, remaining_n):
            if remaining_k == 0 and remaining_n == 0:
                final.append(temp[:])
                return
            if remaining_k <= 0 or remaining_n <= 0:
                return
            for i in range(start, 10):
                if i > remaining_n:
                    break
                temp.append(i)
                backtrack(i + 1, temp, remaining_k - 1, remaining_n - i)
                temp.pop()
        backtrack(1, [], k, n)
        return final