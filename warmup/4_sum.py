

def fourSum(nums, target):
    final_list=[]
    n=len(nums)
    nums.sort()
    for i in range(n-3):
        if i>0 and nums[i]==nums[i-1]:
            continue
        if nums[i]+nums[i+1]+nums[i+2]+nums[i+3]>target:
            break

        for j in range(i+1,n-2):
            if j>i and nums[j]==nums[j-1]:
                continue
            if nums[i]+nums[j]+nums[j+1]+nums[j+2]>target:
                break
            left=j+1
            right=n-1
            while left<right:
                total = nums[i]+nums[j]+nums[left]+nums[right]
                if total>target:
                    right-=1
                elif total < target:
                    left+=1
                else:
                    temp = [nums[i],nums[j],nums[left],nums[right]]
                    if temp not in final_list:
                        final_list.append(temp)
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
    return final_list


if __name__ == "__main__":
    array = str(input("Enter the array elements: "))
    array = array.split()
    k = int(input("Enter the target number"))
    fourSum(array,k)
