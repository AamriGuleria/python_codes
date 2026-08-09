from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(1,n):
            if nums[i]!=nums[i-1]+1:
                return nums[i-1]+1
        return nums[n-1]+1