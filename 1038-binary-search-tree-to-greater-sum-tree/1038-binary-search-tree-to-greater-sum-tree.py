# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        self.sm = 0
        
        def dfs(node):
            if not node:
                return 0
            
            dfs(node.right)
            
            self.sm += node.val
            node.val = self.sm
            
            dfs(node.left)
        
        dfs(root)
        
        return root
        
        
        
        
        
        