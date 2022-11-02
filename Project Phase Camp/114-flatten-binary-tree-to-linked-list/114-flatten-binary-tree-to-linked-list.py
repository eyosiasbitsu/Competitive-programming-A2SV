# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def dfs(node):
            if not node:
                return node, node
            
            close_left, far_left = dfs(node.left)
            close_right, far_right = dfs(node.right)
                
            next_close = node
            next_far = node
            
            if far_right:
                next_far = far_right
                
            elif far_left:
                next_far = far_left
                
            if far_left and close_right:
                far_left.right = close_right
            
            temp = node.left
            node.left = None
            
            if temp:
                node.right = temp
            
            return next_close, next_far
        
        dfs(root)
            
            
            
            
            
            
            
            
            
            
            
            
            
    