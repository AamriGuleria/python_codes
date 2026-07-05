from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def optimizedMiddleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        n=1
        while node.next != None:
            node = node.next
            n=n+1
        print(f"Length of the linked list {n}")
        i=0
        while i!=n//2 and head is not None:
            head=head.next
            i=i+1
        return head