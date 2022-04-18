# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.dict1 = {}
        self.bool1 = False
        def dfs(node):
            if not node:
                return
            if node.val in self.dict1:
                self.bool1 = True
            else:
                self.dict1[k-node.val] = 0
            dfs(node.right)
            dfs(node.left)
        
        dfs(root)
        
        return self.bool1
    