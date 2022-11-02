class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        grid = [[0]*n for _ in range(m)]
        self.dr = [(0,1),(1,0),(-1,0),(0,-1)]
        self.guarded = set()
        
        for i, j in guards:
            grid[i][j] = 1
        
        for i, j in walls:
            grid[i][j] = 2
        
        def dfs(r,c):
            
            # going up wards
            for i in range(r - 1, -1, -1):
                if grid[i][c] == 1 or grid[i][c] == 2:
                    break
                
                self.guarded.add((i,c))
            
            # goind to the right
            for i in range(c + 1, n):
                if grid[r][i] == 1 or grid[r][i] == 2:
                    break
                
                self.guarded.add((r,i))
            
            # going down
            for i in range(r + 1, m):
                if grid[i][c] == 1 or grid[i][c] == 2:
                    break
                
                self.guarded.add((i,j))
            
            # going to the left
            for i in range(c - 1, -1, -1):
                if grid[r][i] == 1 or grid[r][i] == 2:
                    break
                    
                self.guarded.add((r,i))
                
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i,j)
        
        return m*n - len(self.guarded) - len(guards) - len(walls)
                
            
            