from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        def recursive_approach(i):
            if i == n - 1:
                return True
            if i >= n or nums[i] == 0:
                return False
            jump_max = nums[i]
            for j in range(1, jump_max + 1):
                if recursive_approach(i + j):
                    return True
            return False
        return recursive_approach(0)

    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        n = len(nums)
        for i, num in enumerate(nums):
            if i>max_reach:
                return False
            max_reach = max(max_reach, i + num)
        return True