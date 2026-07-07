# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        k = k % length
        if k == 0:
            return head 

        dummy = ListNode(0,head)
        slow = fast = dummy
        for i in range(k):
            fast = fast.next
        
        while fast.next:
            fast=fast.next
            slow=slow.next
        
        new_head = slow.next
        slow.next = None
        tail.next = head
        return new_head