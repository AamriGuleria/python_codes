from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return sorted([i,j])
        return [-1,-1]