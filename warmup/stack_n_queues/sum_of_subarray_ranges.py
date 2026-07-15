from typing import List
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(n-1):
            curr_min = nums[i]
            curr_max = nums[i]
            for j in range(i+1,n):
                curr_min = min(curr_min,nums[j])
                curr_max = max(curr_max,nums[j])
                total = total+ curr_max - curr_min
        return total