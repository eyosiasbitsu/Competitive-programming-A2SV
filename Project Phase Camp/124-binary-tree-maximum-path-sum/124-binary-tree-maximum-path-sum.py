# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        self.res = float("-inf")
        
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            r1 = node.val + right
            r2 = node.val + left
            r3 = node.val + left + right
            self.res = max(r3, self.res, node.val, r1, r2)
            
            return max(r1, r2, node.val)
        
        dfs(root)
        return self.res