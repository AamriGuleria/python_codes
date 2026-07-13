from typing import List 
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = [-1]*n
        i=n-1
        while i>=0:
            j = (i + 1) % n
            while i!=j:
                if nums[j]>nums[i]:
                    stack[i]=nums[j]
                    break
                j = (j + 1) % n
            i=i-1
        return stack
            