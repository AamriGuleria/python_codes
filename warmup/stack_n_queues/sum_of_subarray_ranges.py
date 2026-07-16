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



    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        def sumOfMaxSubArrays():
            stack = []
            total_max = 0
            for i in range(n+1):
                curr = nums[i] if i < n else float('inf')
                while stack and nums[stack[-1]]<curr:
                    mid = stack.pop()
                    left_bound = stack[-1] if stack else -1
                    total_max = total_max+ nums[mid]*(mid-left_bound)*(i-mid)
                stack.append(i)
            return total_max
            
        def sumOfMinSubArrays():
            stack = []
            total_min = 0
            for i in range(n+1):
                curr = nums[i] if i < n else float('-inf')
                while stack and nums[stack[-1]]>curr:
                    mid = stack.pop()
                    left_bound = stack[-1] if stack else -1
                    total_min = total_min+ nums[mid]*(mid-left_bound)*(i-mid)
                stack.append(i)
            return total_min
        
        return sumOfMaxSubArrays() - sumOfMinSubArrays()