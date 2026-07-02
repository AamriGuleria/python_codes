

def threeSum(self, nums: list[int]) -> list[list[int]]:
    target=0
    final_list=[]
    for i,num in enumerate(nums):
        seen = []
        for j in range(i+1,len(nums)):
            key=target-(num+nums[j])
            if key in seen:
                temp=sorted([num,nums[j],key])
                if temp not in final_list:
                    final_list.append(temp)
            seen.append(nums[j])
    return final_list

def correctedThreeSum(self, nums: list[int]) -> list[list[int]]:
    nums.sort()
    final_list = []
    n = len(nums)

    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        if nums[i] > 0:
            break

        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                final_list.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1

    return final_list

if __name__ == "__main__":
    array = str(input("Enter the array elements: "))
    array = array.split()
    k = int(input("Enter the number"))
    threeSum(array)
