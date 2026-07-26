from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        net_list = []
        cost = 5
        value = True
        for b in bills:
            net_list.append(b)
            return_amt = b-cost
            i=0
            while return_amt > 0 and i<len(net_list):
                if net_list[i]<=return_amt:
                    return_amt = return_amt-net_list[i]
                    net_list.remove(net_list[i])
                i=i+1
            if return_amt!=0:
                value=False
                break
        return value

    def correctedLemonadeChange(self, bills: List[int]) -> bool:
        five=ten=0
        for b in bills:
            if b==5:
                five+=1
            elif b==10:
                if five==0:
                    return False
                five-=1
                ten+=1
            else:
                if five>0 and ten>0:
                    five-=1
                    ten-=1
                elif five>=3:
                    five-=3
                else:
                    return False
        return True
            