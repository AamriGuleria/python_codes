from typing import List
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        operators = ["*","+","-"]
        final = []
        def backtrack_approach(num, i , target, current_number, temp):
            if current_number == target:
                final.append(temp)
                return 
            if i > len(num):
                return
            for j in operators:
                original = current_number
                if j=="*":
                    current_number = current_number*int(num[i])
                    temp = temp+"*"+str(num[i])
                elif j=="+":
                    current_number = current_number+num[i]
                    temp = temp+"+"+str(num[i])
                else : 
                    current_number = current_number-num[i]
                    temp = temp+"-"+str(num[i])

                backtrack_approach(num,i+1,target,current_number,temp)
                temp = temp[:-2]
                current_num = original
            
        backtrack_approach(num, 0 , target, 0, "")
        return final
