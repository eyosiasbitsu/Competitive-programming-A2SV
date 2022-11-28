# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        queue = deque([(0, root)])
        res = 0
        
        while queue:
            l = float("inf")
            r = 0
            
            for _ in range(len(queue)):
                idx, cur = queue.popleft()
                if cur:
                    l = min(l, idx)
                    r = max(r, idx)
                    
                    if cur.left:
                        queue.append((2*idx, cur.left))
                    
                    if cur.right:
                        queue.append((2*idx + 1, cur.right))
                        
            if r >= l:
                res = max(res, r - l + 1)
                
        return res  
                