from typing import List
def majorityElement(self, nums: List[int]) -> List[int]:
    n=len(nums)
    max_freq = n//3
    final_list = []
    seen={}
    for i in nums:
        seen[i] = seen.get(i, 0) + 1
    for k, v in seen.items():
        if v > max_freq:
            final_list.append(k)
    return final_list

if __name__ == "__main__":
    array = str(input("Enter the array elements: "))
    array = array.split()
    majorityElement(array)