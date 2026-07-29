from typing import Optional,List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.lst = []
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []

        self.lst.append(root.val)
        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)
        return self.lst
