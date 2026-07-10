from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {
            "2":"abc", "3":"def", "4":"ghi", "5":"jkl",
            "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"
        }
        final=[]
        def recursive_approach(digits, temp_string, i):
            if len(temp_string) == len(digits):
                final.append(temp_string)
                return
            sub = mapping.get(digits[i])
            for j in sub:
                recursive_approach(digits, temp_string + j, i + 1)
        recursive_approach(digits,"",0)
        return final