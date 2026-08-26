from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {}
        for i,num in enumerate(inorder):
            index_map[num]=i
        def recursive_approach(preord, inord):
            if len(inord)==0:
                return None
            root_val = preord[0]
            root_node = TreeNode(root_val)
            mid_local = inord.index(root_val)
            left_size = mid_local
            
            root_node.left = recursive_approach(preord[1:1+left_size], inord[:mid_local])
            root_node.right = recursive_approach(preord[1+left_size:], inord[mid_local+1:])
            return root_node
        return recursive_approach(preorder, inorder)