from collections import Counter
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        result = freq.most_common(k)
        lst = []
        for tup in result:
            lst.append(tup[0])
        return lst