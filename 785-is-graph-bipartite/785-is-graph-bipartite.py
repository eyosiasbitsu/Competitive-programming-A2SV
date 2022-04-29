class disjoint:
    def __init__(self,size):
        self.par = [i for i in range(size)]
        self.rank = [1 for i in range(size)]
        
    def find(self,x):
        if self.par[x] == x:
            return x
        self.par[x] = self.find(self.par[x])
        
        return self.par[x]
    
    def union(self,x,y):
        parx = self.find(x)
        pary = self.find(y)
        if parx != pary:
            if self.rank[pary] > self.rank[parx]:
                self.par[parx] = pary
            elif self.rank[pary] < self.rank[parx]:
                self.par[pary] = parx
            else:
                self.par[pary] = parx
                self.rank[parx] += 1
                
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        disj = disjoint(len(graph))
        
        for i in range(len(graph)):
            for j in graph[i]:
                
                t1 = disj.find(i)
                t2 = disj.find(j)
                print(j,graph[i][0])
                if t1 == t2:
                    return False
                disj.union(j,graph[i][0])
             
        return True