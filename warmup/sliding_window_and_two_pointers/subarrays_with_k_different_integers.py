from typing import List
from collections import Counter
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(k):
            if k == 0:
                return 0
            count = Counter()
            res = 0
            l = 0
            for r in range(len(nums)):
                count[nums[r]] += 1
                while len(count) > k:
                    count[nums[l]] -= 1
                    if count[nums[l]] == 0:
                        del count[nums[l]]
                    l=l+1
                res += r - l + 1
            return res

        return atMost(k) - atMost(k - 1)
        
