"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node', count = None) -> 'Node':
        
        if not node:
            return
        
        if count == None:
            count = {}
            
        temp = Node()
        temp.val = node.val
        count[node.val] = temp
        
        if not node.neighbors:
            return temp
        
        for neigh in node.neighbors:
            if neigh.val not in count:
                call = temp.neighbors.append(self.cloneGraph(neigh, count))
            
            else:
                temp.neighbors.append(count[neigh.val])
        
        print(temp.val)
        return temp