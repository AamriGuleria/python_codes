from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums)==1:
            return nums[0]
        max_sum = float("-inf")
        for i in range(n):
            for j in range(i+1,n+1):
                max_sum = max(max_sum,sum(nums[i:j]))

        return max_sum

# Kadane's algo , start new or continue prev
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        curr_sum = max_sum = nums[0]
        for i in range(1,n):
            curr_sum = max(nums[i] , curr_sum+nums[i])
            max_sum = max(max_sum, curr_sum)
        return max_sum