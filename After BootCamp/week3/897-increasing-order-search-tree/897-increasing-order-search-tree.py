# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = TreeNode(0,None,None)
        
        def bfs(node):
            if not node:
                return []
            return bfs(node.left) + [node.val] + bfs(node.right) 
        
        ret = res
        temp = bfs(root)
        for i in temp:
            cur = TreeNode(i,None,None)
            res.right = cur
            res = res.right
        return ret.right