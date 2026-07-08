"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        old_to_new = {}
        ptr = head
        while ptr:
            old_to_new[ptr] = Node(ptr.val)
            ptr = ptr.next
        ptr = head
        while ptr:
            old_to_new[ptr].next = old_to_new.get(ptr.next)
            old_to_new[ptr].random = old_to_new.get(ptr.random)
            ptr=ptr.next
        return old_to_new[head]