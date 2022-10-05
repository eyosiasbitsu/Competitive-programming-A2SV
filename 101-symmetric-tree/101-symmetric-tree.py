# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
   
        q = deque([root])

        while q:
            size = len(q)

            for _ in range(size):
                cur = q.popleft()

                if cur:
                    q.append(cur.left)
                    q.append(cur.right)

            l, r = 0, len(q) - 1
            while r > l:
                if ((not q[l] and q[r]) or 
                    (not q[r] and q[l])):
                    return False
                
                if q[l] and q[r] and q[l].val != q[r].val:
                    return False
                
                l += 1
                r -= 1
                
        return True
    
    
    
    