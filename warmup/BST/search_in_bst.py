from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def recursive_approach(node):
            if not node:
                return None
            if node.val == val:
                return node
            return recursive_approach(node.left) or recursive_approach(node.right)

        if recursive_approach(root):   
            return recursive_approach(root)
        else:
            return None