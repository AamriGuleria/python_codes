from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def recursive_approach(root):
            if root==None:
                return 0
            if root.val>=0:
                return root.val+recursive_approach(root.left)+recursive_approach(root.right)
            else:
                return max(recursive_approach(root.left),recursive_approach(root.right))
        return recursive_approach(root)

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_total = float('-inf')
        def recursive_approach(root):
            if root==None:
                return 0
            left = max(recursive_approach(root.left), 0)
            right = max(recursive_approach(root.right), 0)
            self.max_total = max(self.max_total, root.val+left+right)
            return root.val+ max(left, right)
        recursive_approach(root)
        return self.max_total