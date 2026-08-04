
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {}
        def build_parent(node,par):
            if not node:
                return
            parent[node]=par
            build_parent(node.left,node)
            build_parent(node.right,node)
        build_parent(root,None)

        ancestors_of_p = set()
        node = p
        while node:
            ancestors_of_p.add(node)
            node = parent[node]

        node = q
        while node:
            if node in ancestors_of_p:
                return node
            node = parent[node]
        return None
