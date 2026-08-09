from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_ones = 0
        n = len(nums)
        for i in range(n):
            if nums[i]==0:
                max_ones = max(max_ones, count)
                count = 0
            else:
                count+=1
        max_ones = max(max_ones, count)
        return max_ones