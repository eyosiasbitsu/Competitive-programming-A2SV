# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root
        if node.val == val:
            return node
        while node and node.val != val:
            if val < node.val:
                node = node.left
            else:
                node = node.right
        return node
        # if node.left