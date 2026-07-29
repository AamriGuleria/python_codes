from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recursive_approach(self,root,level):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return level

        return max(self.recursive_approach(root.left,level+1),self.recursive_approach(root.right,level+1))
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recursive_approach(root,1)


#Cleaner version
class Solution:
    def recursive_approach(self,root):
        if root == None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recursive_approach(root)