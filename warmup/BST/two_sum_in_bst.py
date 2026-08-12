from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        def recursive_approach(node):
            if node == None:
                return False
            if k-node.val in seen:
                return True
            seen.add(node.val)
            return recursive_approach(node.left) or recursive_approach(node.right)
            return False
        return recursive_approach(root)

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                continue
            if k-node.val in seen:
                return True
            seen.add(node.val)
            stack.append(node.left)
            stack.append(node.right)
        return False