from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        linear_list = []
        def recursive_approach(root):
            if root == None:
                return
            linear_list.append(root)
            recursive_approach(root.left)
            recursive_approach(root.right)
        recursive_approach(root)
        node = TreeNode(0)
        return_node = node
        for i in linear_list:
            node.left = None
            node.right = i
            node=node.right
        node.left = None
        return return_node.right
        

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node = TreeNode(0)
        dummy = node
        def recursive_approach(curr):
            nonlocal node
            if curr is None:
                return
            left, right = curr.left, curr.right
            node.left = None
            node.right = curr
            node = node.right
            recursive_approach(left)
            recursive_approach(right)
        recursive_approach(root)
        node.left = None
        return dummy.right