from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root == None:
            return None
        if root.val<key:
            root.right = self.deleteNode(root.right, key)
        elif root.val>key:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left==None:
                return root.right
            elif root.right==None:
                return root.left
            else:
                successor = root.right
                while successor.left:
                    successor = successor.left
                root.val = successor.val
                root.right = self.deleteNode(root.right, successor.val)
        return root 
                