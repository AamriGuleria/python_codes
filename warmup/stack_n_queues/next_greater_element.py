from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        lst = [-1]*n
        i = n-2
        while i >= 0:
            lst[i] = nums2[i+1] if nums2[i+1] > nums2[i] else (lst[i+1] if lst[i+1]> nums2[i] else -1)
            i -= 1
        result = []
        for ele in nums1:
            i = nums2.index(ele)   
            result.append(lst[i]) 
        return result