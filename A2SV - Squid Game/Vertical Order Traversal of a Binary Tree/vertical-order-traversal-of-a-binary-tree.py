# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        heap = []
        result = []

        self.dfs(root, 0, 0, heap)
        
        prev = None
        while heap:
            cur_col, cur_row, val = heapq.heappop(heap)

            if prev != None and cur_col == prev:
                result[-1].append(val)
            
            else:
                result.append([val])
                prev = cur_col
        
        return result

    def dfs(self, node, col, row, heap):
        if not node:
            return
        
        self.dfs(node.left, col - 1, row + 1, heap)
        self.dfs(node.right, col + 1, row + 1, heap)

        heapq.heappush(heap, (col, row, node.val))
