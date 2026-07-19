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

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(goal):
            if goal < 0:
                return 0
            l = 0
            curr = 0
            res = 0
            for r in range(len(nums)):
                curr += nums[r]
                while curr > goal:
                    curr -= nums[l]
                    l += 1
                res += r - l + 1  
            return res
        
        return atMost(goal) - atMost(goal - 1)