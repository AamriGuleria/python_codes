from typing import List
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        lst=[]
        def recursive_approach(node,level,check):
            nonlocal lst
            if node == None:
                return
            if check:
                level+=1
            if not check and node==target:
                check=True
            if level==k:
                lst.append(node.val)
            
            recursive_approach(node.left,level,check)
            recursive_approach(node.right,level,check)     
            
        recursive_approach(root,0,False)
        return lst
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent_child = {}
        def build_parent(node,parent):
            if not node:
                return
            parent_child[node]=parent
            build_parent(node.left,node)
            build_parent(node.right,node)
        build_parent(root,None)

        # BFS from target, treating parent/left/right as neighbors
        visited = set()
        queue = deque([target])
        visited.add(target)
        distance = 0
        while queue:
            if k == distance:
                return [n.val for n in queue]
            for _ in range(len(queue)):
                elem = queue.popleft()
                for neighbor in (elem.left,elem.right,parent_child[elem]):
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            distance += 1
        return []