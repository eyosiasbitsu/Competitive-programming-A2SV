# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        stk = []
        stk.append((root,root.val))
        
        while stk:
            nxt,s = stk.pop()
            
            if s == targetSum and not nxt.left and not nxt.right:
                return True
            
            if nxt.right:
                stk.append((nxt.right,s + nxt.right.val))
                
            if nxt.left:
                stk.append((nxt.left,s + nxt.left.val))
        
        return False
            