

def brute_force_approach(nums):
     
     nums = list(set(nums))
     nums.sort()
     print(nums[-2])

def secondLargestElement(nums):
    largest = float('-inf')
    second_largest = float('-inf')

    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num

    return -1 if second_largest == float('-inf') else second_largest


if __name__ == "__main__":
     array  = input("Enter elements")
     array = array.split(" ")
     array = map(int,array)
     
     print(secondLargestElement(array))
