class disjoint:
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.rank = [0]*size
        self.size = size
        
    def find(self,x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self,x,y):
        rootx = self.find(x)
        rooty = self.find(y)
        
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.root[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.root[rootx] = rooty
            else:
                self.root[rooty] = rootx
                self.rank[rootx] += 1
            self.size -= 1
    def connected(self,x,y):
        return self.find(x) == self.find(y)
    
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)
        set1 = disjoint(size)
        
        for i in range(size):
            for j in range(size):
                if isConnected[i][j] == 1:
                    set1.union(i,j)
          
        return set1.size

    
        
        
        
        
        
        
        
        
        
        
        
        
        
        