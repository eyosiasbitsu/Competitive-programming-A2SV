# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        res = []
        
        def dfs(node, lst, s):
            if not node:
                return
            
            if not node.right and not node.left:
                if s + node.val == targetSum:
                    res.append(lst + [node.val])
                    
                return
            
            dfs(node.right, lst + [node.val], s + node.val)
            dfs(node.left, lst + [node.val], s + node.val)
        
        dfs(root, [], 0)
        
        return res