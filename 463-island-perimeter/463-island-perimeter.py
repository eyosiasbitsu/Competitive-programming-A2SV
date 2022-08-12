class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        m,n = len(grid), len(grid[-1])
        self.dir = [(1,0), (0,1), (0,-1), (-1,0)]
        self.seen = set()
        
        def count(r, c, m, n):
            if not (0 <= r < m) or not (0<= c < n):
                return 1
            
            if grid[r][c] == 0:
                return 1
            
            temp = 0
            self.seen.add((r,c))
            
            for i_add, j_add in self.dir:
                new_i, new_j = r + i_add, c + j_add
                
                if (new_i, new_j) not in self.seen:
                    temp += count(new_i, new_j, m, n)
                    
            return temp
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return count(i, j, m, n)
            
                
        