class disjoint:
    def __init__(self,size):
        self.root = [i for i in range(size)]
        self.rank = [0]*size
        
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
                
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        pt = []
        
        for i in range(len(points)):
            for j in range(i,len(points)):
                d = self.calculate(points,i,j)
                pt.append((d,i,j))
        
        pt.sort()
        disj = disjoint(len(points))
        cost = 0
        for p in pt:
            p1 = disj.find(p[1])
            p2 = disj.find(p[2])
            if p1 != p2:
                disj.union(p1,p2)
                cost += p[0]
                
        return cost
    def calculate(self,arr,i,j):
        x1 = arr[i][0]
        x2 = arr[j][0]
        
        y1 = arr[i][1]
        y2 = arr[j][1]
        
        dist = abs(x1-x2) + abs(y1-y2)
        
        return dist
        