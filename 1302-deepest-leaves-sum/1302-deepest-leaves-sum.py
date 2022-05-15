# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        que = deque()
        que.append(root)
        
        while que:
            temp = 0
            for i in range(len(que)):
                cur = que.popleft()
                
                if cur.left:
                    que.append(cur.left)
                
                if cur.right:
                    que.append(cur.right)
                
                temp += cur.val
        
        return temp