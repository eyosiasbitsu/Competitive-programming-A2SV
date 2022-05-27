# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        que = deque()
        
        que.append((original,cloned))
        
        while que:
            origion, clone = que.popleft()
            
            if origion == target:
                return clone
            
            if origion.left:
                que.append((origion.left,clone.left))
            
            if origion.right:
                que.append((origion.right,clone.right))
        