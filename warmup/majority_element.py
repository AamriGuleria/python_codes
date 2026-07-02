from collections import Counter
from typing import List

def majorityElement2(self, nums: List[int]) -> List[int]:
    n=len(nums)
    max_len = n//3
    count = Counter(nums)
    return [num for num,c in count.items() if c>max_len]

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

#  Boyer-Moore Voting (O(n) time, O(1) space)
def optimizedMajorityElement(self, nums: List[int]) -> List[int]:
    length = len(nums)
    max_freq = length // 3
    candidate1 = candidate2 = None
    count1 = count2 = 0
    for num in nums:
        if candidate1 == num:
            count1 += 1
        elif candidate2 == num:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    result = []
    for c in (candidate1, candidate2):
        if c is not None and nums.count(c) > max_freq:
            result.append(c)
    return result

if __name__ == "__main__":
    array = str(input("Enter the array elements: "))
    array = array.split()
    majorityElement(array)