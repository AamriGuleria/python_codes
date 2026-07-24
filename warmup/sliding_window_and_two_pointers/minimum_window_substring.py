from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        count = Counter(t)
        m = len(t)
        n = len(s)
        l=0
        min_len = float("inf")
        min_str = ""
        for r in range(n):
            if count[s[r]] > 0:
                m -= 1
            count[s[r]] -= 1  
            while m == 0:
                if min_len>r-l+1:
                    min_len = r-l+1
                    min_str = s[l:r+1]
                count[s[l]] += 1
                if count[s[l]] > 0:
                    m += 1
                l += 1
        return min_str
