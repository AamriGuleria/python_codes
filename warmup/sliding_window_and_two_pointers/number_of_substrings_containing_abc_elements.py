

class Solution:
    # Gives TLE with O(n2)
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
    # Improved version
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        count = {}
        l=0
        res = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            while len(count) == 3:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l+=1
            res += l
        return res