from typing import List
class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        req = {}
        for i in range(n):
            req[i]=capacity[i]-rocks[i]
        sorted_items = sorted(req.items(), key=lambda item: item[1])
        count=0
        for key,value in sorted_items:
            if value<=additionalRocks:
                count+=1
                additionalRocks-=value
            else:
                break
        return count

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        deficits = sorted(c - r for c, r in zip(capacity, rocks))
        count = 0
        for d in deficits:
            if d <= additionalRocks:
                count += 1
                additionalRocks -= d
            else:
                break
        return count