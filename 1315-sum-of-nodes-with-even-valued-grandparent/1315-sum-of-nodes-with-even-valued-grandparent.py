# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        def dfs(node, par, gpar):
            if not node:
                return 0
            
            right = dfs(node.right, node.val%2 == 0, par)
            left = dfs(node.left, node.val%2 == 0, par)
            
            return right + left + node.val if gpar else right + left
        
        return dfs(root, False, False)