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
        def do_dfs(node):
            if not node.right and not node.left:
                return node,node
            
            if not node.left and node.right:
                r, f_r = do_dfs(node.right)
                return node, f_r
            
            if not node.right and node.left:
                l, f_l = do_dfs(node.left)
                
                node.right = l
                node.left = None
                
                return node, f_l
            
            if node.left and node.right:
                l,f_l = do_dfs(node.left)
                r, f_r = do_dfs(node.right)
                
                f_l.right = r
                node.right = l
                node.left = None
                
                return node,f_r
        
        if root:
            do_dfs(root)