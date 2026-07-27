from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        max_len = 0
        n=len(nums)
        min_jumps = 0
        for i,num in enumerate(nums):
            if max_len >= n-1:
                break
            if i>max_len:
                return -1
            max_len = max(max_len,i+num)
            min_jumps = min_jumps+1
        return min_jumps