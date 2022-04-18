# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.out = 0
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def sum1(node):
            if not node:
                return 0
            l = sum1(node.right)
            r = sum1(node.left)
            self.out += abs(l - r)
            return node.val + l + r
        sum1(root)
        return self.out
