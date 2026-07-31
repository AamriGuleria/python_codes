from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.right = []
        self.max_level = 0
    # def left_shadow(self,root,level,max_level):
    #     if root == None:
    #         return 
    #     if level>max_level:
    #         self.right.append(root.val)
    #     self.left_shadow(root.right,level+1,max_level)
    def recursive_approach(self,root,level):
        if root == None:
            return
        self.right.append(root.val)
        self.max_level+=1
        self.recursive_approach(root.right,self.max_level)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.recursive_approach(root,0)
        # if root and root.left:
        #     self.left_shadow(root.left,0,self.max_level)
        return self.right

# Best Approach , at each level we have to append just one element which is most outer , so calling the function with right first then left so most outer element gets appended first
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def dfs(node, level):
            if not node:
                return
            if level == len(result):
                result.append(node.val)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        dfs(root, 0)
        return result