# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "()"
        
        cur = str(root.val)
        
        if root.right and not root.left:
            cur = cur + "()" + "(" + self.tree2str(root.right) + ")"
        
        elif root.right and root.left:
            cur = cur + "(" + self.tree2str(root.left) + ")" + "(" + self.tree2str(root.right) + ")"
        elif root.left:
            cur = cur + "(" + self.tree2str(root.left) + ")"
        
        return cur