


from typing import List


def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i=0
    n=len(nums)
    count_zeroes = 0
    while i < n:
        if nums[i]==0:
            count_zeroes+=1
            del nums[i]
            n=n-1
        else:
            i=i+1
    nums[:] = nums + [0] * count_zeroes

def optimized_approach(self,nums):
    w = 0
    r = 0
    n = len(nums)
    while r<n:
        if nums[r] != 0:
            nums[w], nums[r] = nums[r], nums[w]
            w += 1
        r=r+1
    return nums
if __name__ == "__main__":
    array = str(input("Enter the array elements: "))
    array = array.split()
    moveZeroes(array)