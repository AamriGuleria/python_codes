from typing import List
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        window = n-k
        if window == 0:
            return total
        min_sub = None
        i = 0
        for i in range(k+1):
            sub = sum(cardPoints[i:i+window])
            min_sub = sub if min_sub == None else min(min_sub,sub)
        return total-min_sub
            

    def optimalMaxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        window = n-k
        if window == 0:
            return total
        cur = sum(cardPoints[:window])
        min_sub = cur
        i = 0
        for i in range(1,k+1):
            cur += cardPoints[i + window - 1] - cardPoints[i - 1]
            min_sub = min(min_sub, cur)
        return total-min_sub