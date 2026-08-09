from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(1,n):
            if nums[i]!=nums[i-1]+1:
                return nums[i-1]+1
        return nums[n-1]+1 if nums[n-1]+1 == n else 0


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0,n+1):
            if i not in nums:
                return i
            
# Best Approach Gauss' sum formula 
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 1. Gauss' Sum Formula (Math)
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum