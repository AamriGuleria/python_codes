from collections import Counter
from typing import List

def singleNumber(self, nums: List[int]) -> int:
    freq = Counter(nums)
    for key,val in freq.items():
        if val == 1:
            return key
    return -1


if __name__ == "__main__":
    array = str(input("Enter the array elements: "))
    array = array.split()
    k = int(input("Enter the number"))
    singleNumber(array)