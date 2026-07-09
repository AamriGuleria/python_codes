from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        n = len(candidates)
        def recursive_approach(temp, target , start):
            if target == 0:
                result.append(temp[:])
                return
            for i in range(start,n):
                if candidates[i] > target:   
                    break
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                temp.append(candidates[i])
                recursive_approach(temp, target - candidates[i], i + 1)
                temp.pop()
        
        recursive_approach([], target, 0)
        return result