from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def recursive_approach(self, current , open_count , close_count):
            if len(current) == 2*n:
                result.append(current)
                return
            

            if open_count<n:
                recursive_approach(self, current+"(", open_count+1, close_count)

            if close_count < open_count:
                recursive_approach(self, current+")", open_count, close_count+1)
                
        recursive_approach("", 0, 0)
        return result