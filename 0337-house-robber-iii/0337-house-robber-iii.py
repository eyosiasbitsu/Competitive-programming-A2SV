# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        result = self.dfs(root)
        
        return max(result)
    
    def dfs(self, node):
        if not node:
            return [0, 0]
        
        left_child, left_grand_child = self.dfs(node.left)
        right_child, right_grand_child = self.dfs(node.right)
        
        with_node = left_grand_child + right_grand_child + node.val
        with_out_node = max(left_child, left_grand_child) + \
                            max(right_child, right_grand_child)
        
        return with_node, with_out_node
        
        
        
        
        
        
        
        
        