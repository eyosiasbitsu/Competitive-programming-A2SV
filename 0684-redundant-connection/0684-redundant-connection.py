class UnionFind:
    
    def __init__(self, size):
        self.parent = {}
        self.rank = {}
        
        for i in range(1, size + 1):
            self.parent[i] = i
            self.rank[i] = 1
    
    def find(self, node):
        par = self.parent[node]
        
        while par != self.parent[par]:
            self.parent[par] = self.parent[self.parent[par]]
            par = self.parent[par]
        
        return par
    
    def union(self, node1, node2):
        par1 = self.find(node1)
        par2 = self.find(node2)
        
        if par1 == par2:
            return True
        
        if self.rank[par1] > self.rank[par2]:
            self.parent[par2] = par1
        
        elif self.rank[par1] < self.rank[par2]:
            self.parent[par1] = par2
        
        else:
            self.parent[par1] = par2
            self.rank[par2] += 1
        
        return False
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        disjoint_set = UnionFind(len(edges))
        
        for edge in edges:
            if disjoint_set.union(edge[0], edge[1]):
                return edge
        
        
        
        
        
        
        