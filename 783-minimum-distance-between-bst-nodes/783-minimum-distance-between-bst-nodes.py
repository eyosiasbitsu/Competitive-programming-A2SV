# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        ar = self.tr(root)
        
        res = float("inf")
        
        for i in range(1,len(ar)):
            res = min(res,ar[i] - ar[i-1])
        
        return res
    
    
    def tr(self,node):
        if not node:
            return []
        
        return self.tr(node.left) + [node.val] + self.tr(node.right)