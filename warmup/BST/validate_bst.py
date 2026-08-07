from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recursive_appraoch(node, low, high):
            if not node:
                return True
            if (low is not None and node.val <= low) or (high is not None and node.val >= high):
                return False
            return recursive_appraoch(node.left, low, node.val) and recursive_appraoch(node.right, node.val, high)
        return recursive_appraoch(root, None, None)