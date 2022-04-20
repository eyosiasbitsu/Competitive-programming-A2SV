# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.temp = []
        
        def inorder(node):
            if not node:return
            
            inorder(node.left)
            self.temp.append(node)
            inorder(node.right)
            
        inorder(root)
        sr = sorted(node.val for node in self.temp)
        
        for i in range(len(sr)):
            self.temp[i].val = sr[i]
        