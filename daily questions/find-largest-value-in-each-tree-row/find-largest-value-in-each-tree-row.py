# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ar = []
        que = deque([root])
        if not root:
            return ar
        while que:
            temp = float("-inf") - 1
            
            for i in range(len(que)):
                temp2 = que.popleft()
                
                if temp < temp2.val:
                    temp = temp2.val
                    
                if temp2.left:
                    que.append(temp2.left)
                    
                if temp2.right:
                    que.append(temp2.right)
                    
            ar.append(temp)
            
        return ar