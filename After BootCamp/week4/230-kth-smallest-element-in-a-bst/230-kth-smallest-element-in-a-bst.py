# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def count(node):
            if not node:
                return []
            return count(node.left) + [node.val] +count(node.right)
        
        ar = count(root)
        
        return ar[k-1]