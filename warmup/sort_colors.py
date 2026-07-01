from typing import List
def sortColors(self, nums: List[int]) -> None:
    n = len(nums)
    w = 0
    for r in range(n):
        if nums[r] == 0:
            nums[w], nums[r] = nums[r], nums[w]
            w += 1
    for r in range(w, n):
        if nums[r] == 1:
            nums[w], nums[r] = nums[r], nums[w]
            w += 1

if __name__ == "__main__":
    array = str(input("Enter the array elements: "))
    array = array.split()
    k = int(input("Enter the number"))
    sortColors(array)