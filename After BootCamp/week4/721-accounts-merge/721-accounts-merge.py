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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        pidx = {}
        set1 = disjoint(len(accounts))
        
        for i in range(len(accounts)):
            for j in range(1,len(accounts[i])):
                if accounts[i][j] not in pidx:
                    pidx[accounts[i][j]] = i
                else:
                    set1.union(i,pidx[accounts[i][j]])
        l = len(set1.par)
        res = []
        dict2 = defaultdict(list)
        for i in pidx:
            temp = set1.find(pidx[i])
            dict2[temp].append(i)
        for i in dict2:
            dict2[i].sort()
            res.append([accounts[i][0]] + dict2[i])
        
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        