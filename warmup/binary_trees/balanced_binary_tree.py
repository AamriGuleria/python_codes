from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recursive_approach(self,root):
        if root == None:
            return 0
        
        left_val = self.recursive_approach(root.left)
        if left_val == -1:
            return -1
        right_val = self.recursive_approach(root.right)
        if right_val == -1:
            return -1
        if abs(left_val - right_val) > 1:
            return -1
        return 1 + max(left_val, right_val)


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.recursive_approach(root) != -1