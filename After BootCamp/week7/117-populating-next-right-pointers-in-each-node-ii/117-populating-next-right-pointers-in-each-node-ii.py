"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        que = deque()
        que.append(root)
        
        while que:
            for i in range(len(que)):
                cur = que.popleft()
                if que:
                    cur.next = que[0]
                    
                if cur.left:
                    que.append(cur.left)
                    
                if cur.right:
                    que.append(cur.right)
                    
            cur.next = None
        
        return root