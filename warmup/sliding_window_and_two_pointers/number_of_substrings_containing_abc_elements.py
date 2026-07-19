class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n):
            sub = set()
            for j in range(i, n):
                sub.add(s[j])         
                if len(sub) == 3:      
                    count += 1
        return count