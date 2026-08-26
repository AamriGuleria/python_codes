from Optional import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index_map = {num: i for i, num in enumerate(inorder)}
        def recursive_approach(inord,postord):
            if len(postord) == 0:
                return None
            root_val = postord[-1]
            root_node = TreeNode(root_val)
            mid_local = inord.index(root_val)
            left_size = mid_local
            root_node.left = recursive_approach(inord[:mid_local], postord[:left_size])
            root_node.right = recursive_approach(inord[mid_local+1:], postord[left_size:-1])
            return root_node
        return recursive_approach(inorder,postorder)