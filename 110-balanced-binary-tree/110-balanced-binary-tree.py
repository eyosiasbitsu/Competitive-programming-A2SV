# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return True, 0
            
            left, lh = dfs(node.left)
            right, rh = dfs(node.right)
            
            h = 1 + max(lh, rh)
            bol = left and right and abs(lh - rh) <= 1
            
            return bol, h
        
        return dfs(root)[0]
            
            
            
            
            
            
            
            
            
            
            
            