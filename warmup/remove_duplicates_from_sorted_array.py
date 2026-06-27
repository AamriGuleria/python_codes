from typing import List

def optimized_approach(self,nums):
    r = 1
    w = 1
    n = len(nums)
    while r<n:
        if nums[r]>nums[w - 1]:
            nums[w]=nums[r]
            w=w+1
        r=r+1
    return w

def removeDuplicates(self, nums: List[int]) -> int:
    unique = sorted(set(nums))
    for i in range(len(unique)):
        nums[i] = unique[i]
    return len(unique)

if __name__ == "__main__":
    array = str(input("Enter the array elements: "))
    array = array.split()
    removeDuplicates(array)