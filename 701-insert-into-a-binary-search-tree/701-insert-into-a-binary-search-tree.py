# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        temp = root
        par = None
        
        while temp:
            par = temp
            if val >= temp.val:
                temp = temp.right
            elif val < temp.val:
                temp = temp.left
        
        if val >= par.val:
            par.right = TreeNode(val)
        else:
            par.left = TreeNode(val)
        
        return root
                
            