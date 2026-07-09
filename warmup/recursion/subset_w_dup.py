from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        final=[]
        nums.sort()
        def recursive_appraoch(start,temp):
            final.append(temp[:])
            for i in range(start,n):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                temp.append(nums[i])
                recursive_appraoch(i+1,temp)
                temp.pop()

        recursive_appraoch(0,[])
        return final