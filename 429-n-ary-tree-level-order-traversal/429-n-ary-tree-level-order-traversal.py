"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        res = []
        que = deque([root])
        
        while que:
            temp = []
            
            for _ in range(len(que)):
                cur = que.popleft()
                temp.append(cur.val)
                
                for child in cur.children:
                    que.append(child)
            
            res.append(temp)
        
        return res
                
                
                
                
                