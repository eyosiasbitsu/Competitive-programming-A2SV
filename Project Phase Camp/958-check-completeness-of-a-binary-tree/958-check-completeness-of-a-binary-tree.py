# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        
        que = deque([root])
        gf = False
        
        while que:
            flag = False
            
            for n in que:
                if flag and n:
                    return False
                
                if not n:
                    flag = True
            
            for _ in range(len(que)):
                cur = que.popleft()
                if cur and gf: return False
                
                if not cur: gf = True
                    
                if cur:
                    que.append(cur.left)
                    que.append(cur.right)
        
        return True
            
            
            
            
            
            
            
            
            