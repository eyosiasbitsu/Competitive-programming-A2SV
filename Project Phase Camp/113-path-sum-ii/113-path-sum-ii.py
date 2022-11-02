# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        if not root:
            return []
        
        res = []
        
        def dfs(node, lst, sm):
            if not node:
                return
            
            if not node.right and not node.left:
                if sm == targetSum:
                    res.append(lst)
                
                return
            if node.right:
                dfs(node.right, lst + [node.right.val], sm + node.right.val)
            
            if node.left:
                dfs(node.left, lst + [node.left.val], sm + node.left.val)
        
        dfs(root, [root.val], root.val)
        return res