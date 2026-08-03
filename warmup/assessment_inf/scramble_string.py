class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        def helper(a,b):
            if a == b:
                return True
            if sorted(a)!=sorted(b):
                return False
            n = len(a)
            for i in range(1,n):
                x = a[:i] # First Part of s1
                y = a[i:] # Second Part of s2
                if helper(x,b[:i]) and helper(y,b[i:]): 
                    return True
                if helper(x,b[n-i:]) and helper(y,b[:n-i]):
                    return True

            return False
        return helper(s1,s2)