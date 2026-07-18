from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            curr = 0
            for j in range(i, n):
                curr += nums[j]
                if curr == goal:
                    count += 1
                if curr > goal:
                    break
        return count