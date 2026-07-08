
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ptr = head
        lst = []
        while ptr:
            lst.append(ptr.val)
            ptr = ptr.next
        
        i = 0
        n = len(lst)
        while i < n:
            if i + k - 1 < n:
                lst[i:i+k] = lst[i:i+k][::-1]   
            else:
                break
            i = i + k
        
        dummy = ListNode(0)
        tail = dummy                             
        for val in lst:
            tail.next = ListNode(val)
            tail = tail.next
        return dummy.next