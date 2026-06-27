

from typing import List

def optimized_approach(self, nums):
    breaking_point = 0
    n = len(nums)

    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            breaking_point += 1
            if breaking_point > 1:
                return False

    if nums[n - 1] > nums[0]:
        return False

    return True


def check(self, nums: List[int]) -> bool:
    original_array = sorted(nums)
    # return self.rotate_to_original_array(original_array, nums)
    return self.optimized_approach(nums)

def rotate_to_original_array(self,sorted_array, array):
    array_len = len(array)
    for i in range(array_len):
        array = [array[-1]] + array[:-1]
        if array == sorted_array:
            return True
    return False


if __name__ == "__main__":
    array = str(input("Enter the array elements: "))
    array = array.split()
    check(array)