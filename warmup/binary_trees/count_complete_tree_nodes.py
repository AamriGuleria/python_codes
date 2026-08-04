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

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def recursive_approach(node):
            if node==None:
                return 0
            return 1+recursive_approach(node.left)+recursive_approach(node.right)
        return recursive_approach(root)

# Instead of counting each node , find if a subtree is perfect binary and find count using formula otherwise recursively traverse 
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def get_left_height(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h
        def get_right_height(node):
            h = 0
            while node:
                h += 1
                node = node.right
            return h

        def count(node):
            if not node:
                return 0
            
            left_h = get_left_height(node)
            right_h = get_right_height(node)

            if left_h == right_h:
                return (2**left_h)-1
            
            else:
                return 1+count(node.left)+count(node.right)

        return count(root)