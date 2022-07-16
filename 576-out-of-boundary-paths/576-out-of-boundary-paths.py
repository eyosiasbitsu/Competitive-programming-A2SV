class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        self.dir = [(0,1),(1,0),(-1,0),(0,-1)]
        self.seen = {}
        
        def backtrack(r, c, move):
            if move < 0:
                return 0
            
            if not 0 <= r < m or not 0 <= c < n:
                return 1
            
            if (r,c,move) not in self.seen:
                temp = 0
                for r_add, c_add in self.dir:
                    new_r, new_c = r + r_add, c + c_add
                    temp += backtrack(new_r, new_c, move - 1)

                self.seen[(r,c,move)] = temp
        
            return self.seen[(r,c,move)]
            
        return backtrack(startRow, startColumn, maxMove) % (10**9 + 7)
        
        
        
        
        
            