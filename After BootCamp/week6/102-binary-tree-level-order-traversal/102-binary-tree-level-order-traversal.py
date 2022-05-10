# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        que = deque([root])
        ar = []
        
        while que:
            temp = []
            
            for i in range(len(que)):
                cur = que.popleft()
                temp.append(cur.val)
                
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
                    
            ar.append(temp)
        
        return ar