# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        dummy = TreeNode()
        dummy.left = root
        temp = dummy
        left = True
        
        while root:
            if root.val < val:
                temp = root
                root = root.right
                left = False
            
            else:
                temp = root
                root = root.left
                left = True
        
        if left:
            temp.left = TreeNode(val)
        
        else:
            temp.right = TreeNode(val)
        
        return dummy.left
                
                
                
                
                
                
                
                
                
                