from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        lst = []
        def recursive_appraoch(node):
            if not node:
                return
            recursive_appraoch(node.left)
            lst.append(node.val)
            recursive_appraoch(node.right)
        recursive_appraoch(root)

        return lst[k-1] if len(lst) >= k else -1