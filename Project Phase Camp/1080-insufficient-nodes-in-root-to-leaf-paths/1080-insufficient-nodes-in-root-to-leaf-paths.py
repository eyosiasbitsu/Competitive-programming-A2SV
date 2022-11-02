# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        
        def dfs(par, node, l, sm):
            if not node:
                return float("-inf")
            
            if not node.left and not node.right:
                sm += node.val
                if sm < limit:
                    if l:
                        par.left = None
                
                    else:
                        par.right = None
                    
                return sm
            
            left = dfs(node, node.left,True, sm + node.val)
            right = dfs(node, node.right,False, sm + node.val)
            
            if left < limit and right < limit:
                if l:
                    par.left = None
                
                else:
                    par.right = None
            
            return max(left, right)
        
        dummy = TreeNode()
        dummy.left = root
        
        dfs(dummy, root, True, 0)
        
        return dummy.left