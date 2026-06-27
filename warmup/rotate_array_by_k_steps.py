from typing import List


def rotate(self, nums: List[int], k: int) -> None:
    n = len(nums)
    k=k%n
    first_half = nums[n-k:]
    nums[:] = first_half + nums[:n-k]
    print(nums)


if __name__ == "__main__":
    array = str(input("Enter the array elements: "))
    array = array.split()
    k = int(input("Enter the number"))
    rotate(array,k)