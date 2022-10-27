class Disjoint:
    
    def __init__(self, amount):
        self.size = [1 for _ in range(amount)]
        self.parent = [i + 1 for i in range(amount)]
    
    def find(self, x):
        
        if x != self.parent[x - 1]:
            self.parent[x - 1] = self.find(self.parent[x - 1])
            
        return self.parent[x - 1]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if self.same(x, y):
            return False
        
        if self.size[x - 1] > self.size[y - 1]:
            self.parent[y - 1] = x
            self.size[x - 1] + self.size[y - 1]
        else:
            self.parent[x - 1] = y
            self.size[y - 1] += self.size[x - 1]        
        
        return True
    
    def same(self, x, y):
        return self.parent[x - 1] == self.parent[y - 1]

    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        size = len(edges)
        
        unionFind = Disjoint(size)
        for fr, to in edges:
            if not unionFind.union(fr, to):
                return [fr, to]
        
        
        
        
        
        
        
        
        
        