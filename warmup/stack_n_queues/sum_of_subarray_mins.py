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

    def mostOptimalSumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        total = 0
        stack = []
        for i in range(n + 1): 
            curr = arr[i] if i < n else float('-inf') 
            while stack and arr[stack[-1]] >= curr:
                mid = stack.pop()
                left_bound = stack[-1] if stack else -1
                total += arr[mid] * (mid - left_bound) * (i - mid)
            stack.append(i)
        return total % MOD