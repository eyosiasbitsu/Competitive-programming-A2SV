class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [["."]*n for _ in range(n)]
        
        col = set()
        posD = set()
        negD = set()
        
        self.count = 0
        
        def backtrack(r):
            
            if r == n:
                self.count += 1
                return
            
            for c in range(n):
                if (c in col or r - c in negD or
                    r + c in posD):
                    continue
                
                col.add(c)
                posD.add(r + c)
                negD.add(r - c)
                
                backtrack(r+1)
                
                col.remove(c)
                posD.remove(r + c)
                negD.remove(r - c)
        
        backtrack(0)
        return self.count
                
                
                