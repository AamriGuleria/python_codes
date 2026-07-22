from typing import List
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        hand.sort()
        for i in range(n):
            if hand[i] == -1:
                continue
            sub = [hand[i]]
            hand[i] = -1
            for j in range(i+1,n):
                if hand[j]==-1:
                    continue
                if len(sub) == groupSize:
                    break
                if hand[j] == sub[-1] + 1:
                    sub.append(hand[j])
                    hand[j] = -1
            if len(sub) != groupSize:
                return False
        return True