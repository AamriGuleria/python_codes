from typing import Optional , List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import defaultdict
        cols = defaultdict(list)
        def recursive_approach(root, x, y):
            if root == None:
                return
            cols[x].append((y, root.val))
            recursive_approach(root.left, x-1, y+1)
            recursive_approach(root.right, x+1, y+1)
        recursive_approach(root, 0, 0)
        result = []
        for x in sorted(cols.keys()):
            col = sorted(cols[x])     
            result.append([val for row, val in col])
        return result