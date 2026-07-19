from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def count_odd(sub):
            count = 0
            for num in sub:
                if num % 2 != 0:
                    count += 1
            return count == k
        n=len(nums)
        result=0
        for i in range(n):
            for j in range(i,n):
                if count_odd(nums[i:j+1]):
                    result+=1
        return result