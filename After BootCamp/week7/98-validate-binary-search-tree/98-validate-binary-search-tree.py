# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        rn = (float("-inf"),float("inf"))
        
        def dfs(node,rn):
            if not node:
                return True
            
            if rn[0] >= node.val or node.val >= rn[1]:
                return False
            
            return (dfs(node.right,(node.val,rn[1])) and
                    dfs(node.left,(rn[0],node.val)))
        
        return dfs(root,rn)
        
            