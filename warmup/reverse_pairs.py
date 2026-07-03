
from typing import List


def reversePairs(self, nums: List[int]) -> int:
    n = len(nums)
    count = 0
    for i in range(n - 1, 0, -1):
        for j in range(i - 1, -1, -1):  
            if nums[j] > 2 * nums[i]:   
                count += 1
    return count


if __name__ == "__main__":
    array = str(input("Enter the array elements: "))
    array = array.split()
    reversePairs(array)