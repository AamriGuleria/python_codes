from typing import Optional
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        final=[]
        def recursive_approach(digits, temp_string, i):
            if len(temp_string) == len(digits):
                final.append(temp_string)
                return
            sub = mapping.get(digits[i])
            for j in sub:
                temp_string = temp_string+j
                recursive_approach(digits, temp_string,i+1)
                temp_string = temp_string[:-1]
        recursive_approach(digits,"",0)
        return final
