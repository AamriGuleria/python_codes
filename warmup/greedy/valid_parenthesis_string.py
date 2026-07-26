class Solution:
    def checkValidString(self, s: str) -> bool:
        n=len(s)
        def recursive_approach(valid_stack,i):
            if i>=n:
                return len(valid_stack)==0
            if s[i]==')':
                if not valid_stack:
                    return False
                new_stack = valid_stack[:-1]
                return recursive_approach(new_stack, i+1)
            elif s[i]=='(':
                new_stack = valid_stack + ['(']
                return recursive_approach(new_stack, i+1)
            else:
                return (recursive_approach(valid_stack + ['('], i+1) or
                        recursive_approach(valid_stack[:-1] if valid_stack else valid_stack, i+1) or
                        recursive_approach(valid_stack, i+1))
        
        return recursive_approach([],0)

    def checkValidString(self, s: str) -> bool:
        n=len(s)
        lo=0
        hi=0
        for i in range(n):
            if s[i]=='(':
                lo+=1
                hi+=1
            elif s[i]==')':
                lo-=1
                hi-=1
            else:
                lo-=1
                hi+=1
            if hi<0:
                return False
            lo = max(lo, 0)
        return lo==0 