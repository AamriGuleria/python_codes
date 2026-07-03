from typing import List

def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i=m-1
    j=n-1
    k=m+n-1
    while j >= 0:
        if i >= 0 and nums1[i]>nums2[j]:
            nums1[k]=nums1[i]
            i=i-1
        else:
            nums1[k]=nums2[j]
            j=j-1
        k=k-1


if __name__ == "__main__":
    array = str(input("Enter the array elements: "))
    array = array.split()
    array2 = str(input("Enter the array 2 elements: "))
    array2 = array.split()
    m = int(input("Enter the number for array 1"))
    n = int(input("Enter the number for array 2"))
    merge(array,m,array2,n)