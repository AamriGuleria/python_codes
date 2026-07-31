from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        total=0
        max_total = 0
        def recursive_approach(root):
            if root==None:
                return 0
            if root.val>=0:
                return root.val+recursive_approach(root.left)+recursive_approach(root.right)
            else:
                # max_total = max(max_total,total)
                return max(recursive_approach(root.left),recursive_approach(root.right))
        return recursive_approach(root)