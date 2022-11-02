# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        arr = []
        
        def dfs(node, r, c):
            if not node:
                return []
            
            heapq.heappush(arr, (c,r,node.val))
            
            dfs(node.right, r + 1, c + 1)
            dfs(node.left, r + 1, c - 1)
            
        dfs(root, 0, 0)
        
        res = []
        prev = -1
        
        while arr:
            cur = heapq.heappop(arr)
            
            if res and cur[0] == prev:
                res[-1].append(cur[-1])
                
            else:
                res.append([cur[-1]])
                prev = cur[0]
        
        return res
            