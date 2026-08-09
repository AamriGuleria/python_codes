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

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        n = len(nums)
        for i in range(n):
            second_element = target-nums[i]
            if second_element in seen:
                return [seen[second_element],i]
            seen[nums[i]]=i
        return [-1,-1]