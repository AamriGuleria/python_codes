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
class Solution:
    def mergeTwoLists(self,l1,l2):
        curr = ListNode(0)
        return_node = curr
        while l1 and l2:
            if l1.val<l2.val:
                curr.next, l1 = l1, l1.next
            else:
                curr.next, l2 = l2, l2.next
            curr = curr.next
        curr.next = l1 if l1 else l2
        return return_node.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        l3 = None
        while len(lists)>1:
            l1 = lists.pop()
            l2 = lists.pop()
            l3 = self.mergeTwoLists(l1,l2)
            lists.append(l3)
        return lists[0] if lists else l3

    def optimizedMergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i + 1 < len(lists) else None
                merged.append(self.mergeTwoLists(l1, l2))
            lists = merged
        return lists[0]
        