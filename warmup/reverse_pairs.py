
from typing import List


def reversePairs(self, nums: List[int]) -> int:
    n = len(nums)
    count = 0
    for i in range(n - 1, 0, -1):
        for j in range(i - 1, -1, -1):  
            if nums[j] > 2 * nums[i]:   
                count += 1
    return count


class mergeSortApproach:
    
    def reversePairs(self, nums: List[int]) -> int:
        self.count = 0
        self.divide(nums)
        return self.count
    # Divide the arrays
    def countPairs(self, left, right):
        j = 0
        for i in range(len(left)):
            while j < len(right) and left[i] > 2 * right[j]:
                j += 1
            self.count += j
    def divide(self, nums):
        n = len(nums)
        if n <= 1:
            return nums
        mid = n//2
        left = self.divide(nums[:mid])
        right = self.divide(nums[mid:])
        self.countPairs(left,right)
        return self.merge(left,right)
    # Merge the two sorted arrays
    def merge(self,left,right):
        i=0
        j=0
        result = []
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                result.append(left[i])
                i=i+1
            else:
                result.append(right[j])
                j=j+1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

if __name__ == "__main__":
    array = str(input("Enter the array elements: "))
    array = array.split()
    service = mergeSortApproach()
    service.reversePairs(array)