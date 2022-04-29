# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
    
        return self.trim(root,low,high)
    
    def trim(self,node,low,high):
        if not node:
            return node
        
        if node.val > high:
            return self.trim(node.left,low,high)
        
        if node.val < low:
            return self.trim(node.right,low,high)
        
        else:
            node.right = self.trim(node.right,low,high)
            node.left = self.trim(node.left,low,high)
            
            return node