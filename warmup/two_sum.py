
from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen = {}
    for i,num in enumerate(nums):
        existing = target-num
        if existing in seen:
            return [seen[existing],i]
        seen[num]=i
    return [-1,-1]

if __name__ == "__main__":
    array = str(input("Enter the array elements: "))
    array = array.split()
    twoSum(array)