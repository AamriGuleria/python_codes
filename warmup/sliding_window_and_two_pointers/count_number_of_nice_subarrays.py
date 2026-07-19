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
    
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        result=0
        for i in range(n):
            odd_count=0
            for j in range(i,n):
                if nums[j] % 2 != 0:
                    odd_count += 1
                if odd_count == k:
                    result += 1
        return result


    def improvedNumberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(k):
            if k < 0:
                return 0
            n=len(nums)
            result=0
            l=0
            count_odd=0
            def is_odd(num):
                return num%2!=0
            for r in range(n):
                if is_odd(nums[r]):
                    count_odd+=1
                while count_odd>k:
                    if is_odd(nums[l]):
                        count_odd-=1
                    l=l+1
                result += r - l + 1
            return result
        
        return atMost(k) - atMost(k-1)