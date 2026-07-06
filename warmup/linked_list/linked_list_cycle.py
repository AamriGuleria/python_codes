from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        temp = head
        while temp is not None:
            if temp in seen:
                return True
            seen.add(temp)
            temp=temp.next
        return False
    # turotoise and hare approach
    def optimizedHasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            if slow == fast.next:
                return True
            slow = slow.next
            fast = fast.next.next
        return False