from collections import Counter
class Solution:
    def __init__(self):
        self.counter = 0
    def beauty(self,s):
        count = Counter(s) 
        values = count.values()
        max_val,min_val = max(values),min(values)
        return max_val-min_val

    def beautySum(self, s: str) -> int:
        n=len(s)
        for i in range(n-1):
            sub = s[i]
            for j in range(i+1,n):
                sub=sub+s[j]
                self.counter+=self.beauty(sub)
        return self.counter

if __name__ == "__main__":
    string = str(input("Enter your string: "))
    service = Solution()
    result = service.beautySum(string)
    print(f"The sum of beauty of all substrings is: {result}")