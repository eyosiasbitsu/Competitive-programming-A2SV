# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        def dfs(node):
            if not node:
                return [False, False, node]
            
            
            l1,l2,left = dfs(node.left)
            r1,r2,right = dfs(node.right)
            cur1 = node == p
            cur2 = node == q
            
            if l1 and l2:
                return [l1,l2,left]
            
            if r1 and r2:
                return [r1,r2,right]
            
            temp1 = cur1 or l1 or r1
            temp2 = cur2 or l2 or r2
            
            return [temp1,temp2,node]
        
        result = dfs(root)
        
        return result[2]
            
            
            
            
            
            
            
            