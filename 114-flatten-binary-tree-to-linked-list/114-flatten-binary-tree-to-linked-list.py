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
            if not node.right and not node.left:
                return node,node
            
            if node.left and not node.right:
                left,llast = dfs(node.left)
                node.right = left
                node.left = None
                
                return node,llast
                
            elif node.right and not node.left:
                right,rlast = dfs(node.right)
                
                node.right = right
                node.left = None
                
                return node,rlast
                
            elif node.right and node.left:
                left,llast = dfs(node.left)
                right,rlast = dfs(node.right)
                llast.right = right
                
                node.right = left
                node.left = None
                llast.next = right
                
                return node,rlast
        if root:
            dfs(root)
        
        