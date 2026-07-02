

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

if __name__ == "__main__":
    array = str(input("Enter the array elements: "))
    array = array.split()
    k = int(input("Enter the number"))
    threeSum(array)
