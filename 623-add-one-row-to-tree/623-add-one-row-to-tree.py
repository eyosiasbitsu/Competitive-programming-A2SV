# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        dummy = TreeNode()
        dummy.left = root
        
        lvl = 1
        que = deque([dummy])
        
        while que and lvl < depth:
            for _ in range(len(que)):
                cur = que.popleft()
                
                if cur.left:
                    que.append(cur.left)
                
                if cur.right:
                    que.append(cur.right)
            
            lvl += 1
            
        for node in que:
            templ = TreeNode()
            tempr = TreeNode()
            
            templ.val = val
            tempr.val = val
            
            left = node.left
            node.left = templ
            templ.left = left

            right = node.right
            node.right = tempr
            tempr.right = right
        
        return dummy.left
            
            
            
            
            
            
            
            
            
            