class Solution:
    def isValid(self, s: str) -> bool:
        mappings = {
            "]": "[",
            "}": "{",
            ")": "("
        }
        lst = []
        for i in s:
            if i in mappings:
                if lst and lst[-1] == mappings[i]:
                    lst.pop()
                else:
                    return False
            else:
                lst.append(i)
        return len(lst) == 0