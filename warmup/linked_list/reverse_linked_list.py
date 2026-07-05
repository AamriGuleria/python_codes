from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        temp = head
        while temp is not None:
            values.append(temp.val)
            temp=temp.next
        
        new_list = ListNode(0)
        final_list = new_list
        for v in values[::-1]:
            new_list.next = ListNode(v)
            new_list = new_list.next
        return final_list.next