from typing import List
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
            if level==k:
                lst.append(node.val)
            if check:
                level+=1
            if not check and node==target:
                check=True
            
            recursive_approach(node.left,level,check)
            recursive_approach(node.right,level,check)     
            
        recursive_approach(root,0,False)
        return lst