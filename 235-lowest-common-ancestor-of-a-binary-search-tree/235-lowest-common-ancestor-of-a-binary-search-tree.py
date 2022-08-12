# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # [p, q]
        
        self.result = None
        self.flag = False
        
        def dfs(node):
            if not node:
                return False, False
            qn = node == q
            pn = node == p
            
            pl, ql = dfs(node.left)
            pr, qr = dfs(node.right)
            
            qn = qn or ql or qr
            pn = pn or pl or pr
            
            if qn and pn and not self.flag:
                self.result = node
                self.flag = True
            
            return pn, qn
        
        dfs(root)
        
        return self.result