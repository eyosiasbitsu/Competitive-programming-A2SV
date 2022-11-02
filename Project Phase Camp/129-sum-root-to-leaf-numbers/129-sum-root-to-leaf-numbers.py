# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        res = [0]
        
        def dfs(node, num):
            if not node.right and not node.left:
                res[-1] += num
                return 
            
            if node.right:
                dfs(node.right, 10*num + node.right.val)
            
            if node.left:
                dfs(node.left, 10*num + node.left.val)
        
        dfs(root, root.val)
        
        return res[-1]