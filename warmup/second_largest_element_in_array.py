

def brute_force_approach(nums):
     
     nums = list(set(nums))
     nums.sort()
     print(nums[-2])
     
def secondLargestElement( nums):
        largest = -1
        second_largest = -1
        is_second_largest = False
        for i, num in enumerate(nums):
            if num>largest:
                largest = num
            elif num>second_largest and num<largest:
                is_second_largest = True
                second_largest = num

        return second_largest


if __name__ == "__main__":
     array  = input("Enter elements")
     array = array.split(" ")
     array = map(int,array)
     
     print(secondLargestElement(array))
