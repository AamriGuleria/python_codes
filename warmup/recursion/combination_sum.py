from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        n = len(candidates)
        def recursive_approach(temp, target , i):
            if target == 0:
                result.append(temp)
                return
            if i >= n or target < 0:
                return
            recursive_approach(temp + [candidates[i]], target - candidates[i], i)
            recursive_approach(temp, target, i + 1)
        
        recursive_approach([], target , 0)
        return result