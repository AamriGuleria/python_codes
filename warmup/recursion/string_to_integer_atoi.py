class Solution:
    def myAtoi(self, s: str) -> int:
        i, n = 0, len(s)
        while i < n and s[i] == ' ':
            i += 1
        if i == n:
            return 0
        sign = 1
        if s[i] in '+-':
            if s[i] == '-':
                sign = -1
            i += 1
        digits = ""
        while i < n and s[i].isdigit():
            digits += s[i]
            i += 1
        if not digits:
            return 0

        result = sign * int(digits)
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        return max(INT_MIN, min(INT_MAX, result))