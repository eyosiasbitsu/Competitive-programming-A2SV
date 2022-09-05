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
        
        que = deque([root])
        res = []
        
        while que:
            temp = []
            
            for _ in range(len(que)):
                cur = que.popleft()
                
                for child in cur.children:
                    que.append(child)
                
                temp.append(cur.val)
            
            res.append(temp)
        
        return res