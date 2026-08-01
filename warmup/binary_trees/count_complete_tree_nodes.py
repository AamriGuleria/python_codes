from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count=0
        def recursive_approach(node):
            nonlocal count
            if node==None:
                return
            count+=1
            recursive_approach(node.left)
            recursive_approach(node.right)
        recursive_approach(root)
        return count
