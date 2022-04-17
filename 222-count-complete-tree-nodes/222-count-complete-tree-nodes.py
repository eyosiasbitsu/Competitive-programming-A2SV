# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:return 0
        
        def lleft(node):
            if not node:return 0
            return 1 + lleft(node.left)
        
        def lright(node):
            if not node:return 0
            return 1 + lright(node.right)
        
        l,r = lleft(root),lright(root)
        if l > r:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        else:
            return 2**l - 1
        
    
    
    
    
    
    

            