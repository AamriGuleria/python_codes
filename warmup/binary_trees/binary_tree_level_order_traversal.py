from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.lst=[]
    def recursive_level_traversal(self,root,level):
        if root == None:
            return []
        if level == len(self.lst):
            self.lst.append([])
        self.lst[level].append(root.val)
        self.recursive_level_traversal(root.left,level+1)
        self.recursive_level_traversal(root.right,level+1)
        return self.lst
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
       return  self.recursive_level_traversal(root,0)
