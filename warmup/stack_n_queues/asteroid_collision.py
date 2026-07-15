from typing import List
class Solution:
    def sameSign(self,x, y):
        if (x*y > 0):
            return True
        else:
            return False
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        n = len(asteroids)
        i = n-1
        while i >= 0 :
            elem = asteroids[i]
            exploded = False
            while elem > 0 and stack and stack[0] < 0:
                if -stack[0] < elem:
                    stack.pop(0)          
                elif -stack[0] == elem:
                    stack.pop(0)          
                    exploded = True
                    break
                else:
                    exploded = True       
                    break
            if not exploded:
                stack.insert(0, elem)
            i -= 1
        
        return stack
