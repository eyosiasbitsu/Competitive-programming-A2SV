# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(prev, node):
            if not node:
                return 0
            
            if node.val < prev:
                return dfs(prev, node.left) + dfs(prev, node.right)
            
            left = dfs(node.val, node.left)
            right = dfs(node.val, node.right)
            
            return 1 + left + right
        
        return dfs(float("-inf"), root)
        