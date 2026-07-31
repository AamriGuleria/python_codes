from typing import Optional,List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lst = []
        def recursive_approach(root,level):
            if root==None:
                return
            if level == len(lst):
                lst.append([])
            lst[level].append(root.val)
            recursive_approach(root.left,level+1)
            recursive_approach(root.right,level+1)
        recursive_approach(root,0)
        for i in range(len(lst)):
            if i % 2 == 1:
                lst[i].reverse()
        return lst