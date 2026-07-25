from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        m = len(g)
        n = len(s)
        i=0
        j=0
        count = 0
        while i<m and j<n:
            if g[i]<=s[j]:
                count+=1
                i=i+1
                j=j+1
            else:
                j += 1
        return count