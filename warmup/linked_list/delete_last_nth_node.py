
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
    
    # First let fast travel n distance then fast travels L-n distance and slow completes same distance from beginning
    def optimizedRemoveNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        fast = slow = dummy
        for i in range(n):
            fast=fast.next
        
        while fast.next:
            fast=fast.next
            slow= slow.next
        slow.next = slow.next.next
        return dummy.next
 