# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        self.min = float("inf")
        
        def dfs(node):
            if not node:
                return float("-inf"),float("inf")
            
#             i recieve left maximum and right minimum from the function call
#              l_max and r_min

            l_max,l_min = dfs(node.left)
            r_max,r_min = dfs(node.right)
            
            self.min = min(abs(node.val - l_max), self.min, abs(node.val - r_min))
            
            mx = max(l_max, node.val,r_max)
            mn = min(node.val, l_min, r_min)
            
            return mx,mn
            
        dfs(root)
        return self.min