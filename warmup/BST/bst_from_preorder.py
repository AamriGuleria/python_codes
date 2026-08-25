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