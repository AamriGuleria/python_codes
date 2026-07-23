from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lst = []
        n = len(lists)
        for i in range(n):
            head = lists[i]
            while head:
                lst.append(head.val)
                head=head.next
        lst.sort()
        new_node = ListNode(0)
        return_node = new_node
        for num in lst:
            new_node.next = ListNode(num)
            new_node=new_node.next
        return return_node.next