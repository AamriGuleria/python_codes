from typing import List
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        total = 0
        for i in range(n):
            for j in range(i, n):
                total += min(arr[i:j+1])
        return total

    def optimizedSumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        total = 0
        for i in range(n):
            curr_min = arr[i]
            for j in range(i, n):
                curr_min = min(curr_min, arr[j])
                total += curr_min
        return total