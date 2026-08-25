from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def division(self, preorder):
        if len(preorder) == 0:
            return None, [], []
        root_val = preorder[0]
        root = TreeNode(root_val)
        left = []
        right = []
        ind = None
        for i, num in enumerate(preorder[1:], start=1): 
            if root_val > num:
                left.append(num)
            else:
                ind = i
                break
        if ind is not None:
            right = preorder[ind:]
        return root, left, right
            
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def recursive_approach(order_list):
            if len(order_list) == 1:
                return TreeNode(order_list[0])
            root, left, right = self.division(order_list)
            if root == None:
                return None
            root.left = recursive_approach(left)
            root.right = recursive_approach(right)
            return root
        return recursive_approach(preorder)


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        stack = [root]
        for val in preorder[1:]:
            node = TreeNode(val)
            if val < stack[-1].val:
                stack[-1].left = node
            else:
                parent = stack[-1]
                while stack and stack[-1].val < val:
                    parent = stack.pop()
                parent.right = node
            stack.append(node)
        return root