
from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        last_seen = []
        l = r = 0
        n = len(nums)
        max_len = 0
        while r < n:
            if nums[r] == 0:
                last_seen.append(r)
            if len(last_seen) > k:
                l = last_seen[0] + 1  
                last_seen.pop(0)      
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len