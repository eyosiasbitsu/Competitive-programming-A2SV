# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        que = deque([root])
        res = []
        
        while que:
            size = len(que)
            temp_sum = 0
            
            for _ in range(size):
                cur = que.popleft()
                temp_sum += cur.val
                
                if cur.left:
                    que.append(cur.left)
                
                if cur.right:
                    que.append(cur.right)
            
            avg = temp_sum / size
            res.append(avg)
        
        return res
            
            
            
            
            
            
            
            
            
                
                
                
                
                
                
                
                
                