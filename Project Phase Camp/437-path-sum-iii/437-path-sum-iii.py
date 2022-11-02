# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        pref = defaultdict(int)
        pref[0] = 1
        
        self.count = 0
        
        def dfs(node, prsum):
            if not node:
                return
            
            temp = node.val + prsum
            
            if temp - targetSum in pref:
                self.count += pref[temp - targetSum]
            
            pref[temp] += 1
            
            dfs(node.left, temp)
            dfs(node.right, temp)
            
            pref[temp] -= 1
            
        dfs(root, 0)
        
        return self.count
    
    
    
    
    
    
    
    
    
    