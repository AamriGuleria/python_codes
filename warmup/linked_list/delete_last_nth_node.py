
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = head
        lst=[]
        while ptr:
            lst.append(ptr.val)
            ptr=ptr.next

        new_ptr = ListNode(0)
        final_ptr=new_ptr
        k=len(lst)
        for i in range(k):
            if i == k-n:
                continue
            new_ptr.next = ListNode(lst[i])
            new_ptr = new_ptr.next
        return final_ptr.next