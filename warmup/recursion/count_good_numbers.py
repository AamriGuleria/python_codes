class Solution:
    def is_prime(self,n):
        return n in (2, 3, 5, 7)
    def isGood(self,n):
        for i,ch in enumerate(n):
            ch = int(ch)
            if i%2==0 and ch%2!=0:
                #Even position
                return False
            elif i%2!=0 and not self.is_prime(ch):
                return False
        return True

    def countGoodNumbers(self, n: int) -> int:
        count=0
        if n == 1:
            my_range = range(0, 10)
        else:
            my_range = range(10**(n-1), 10**n)
        for i in my_range:
            s = str(i).zfill(n)
            if self.isGood(str(s)):
                count=count+1
        return count

    def formulaBasedCountGoodNumbers(self, n: int) -> int:
        even_positions = (n + 1) // 2   
        odd_positions = n // 2 
        MOD = 10**9 + 7
        return (pow(5, even_positions, MOD) * pow(4, odd_positions, MOD)) % MOD