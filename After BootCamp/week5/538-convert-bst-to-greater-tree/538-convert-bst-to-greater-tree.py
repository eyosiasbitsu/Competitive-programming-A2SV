# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = self.traversal(root)
        arr.sort(key = lambda x : x.val)
        arr.append(TreeNode())
        
        for i in range(len(arr) - 2,-1,-1):
            arr[i].val = arr[i].val + arr[i+1].val
            
        return root
        
    def traversal(self,node):
        if not node:
            return []
        
        return self.traversal(node.left) + [node] + self.traversal(node.right)
    
        