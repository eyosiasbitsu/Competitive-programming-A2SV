class DSU:
    def __init__(self):
        self.p = {}
        self.count = 0
    
    def add(self, x):
        if x in self.p: return
        self.p[x] = x
        self.count += 1
    
    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        if xp == yp: return False
        self.p[xp] = yp
        self.count -= 1
        return True
    
    def is_connected(self, x, y):
        if x in self.p and y in self.p:
            return self.find(x) == self.find(y)
        else:
            return False
    

class Solution(object):
    def equationsPossible(self, equations):
        
        dsu = DSU()
        for b, s, _, e in equations:
            dsu.add(b)
            dsu.add(e)
            if s == '=': dsu.union(b, e)
        
        for b, s, _, e in equations:
            if s == '!':
                if dsu.is_connected(b, e): return False
        return True