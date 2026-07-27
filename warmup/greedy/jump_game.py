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