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