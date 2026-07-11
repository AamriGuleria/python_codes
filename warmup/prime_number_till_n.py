class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        for i in range(2, n):
            is_prime = True
            for j in range(2, i//2+1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                count += 1
        return count