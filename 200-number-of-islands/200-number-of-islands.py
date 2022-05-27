class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        
        def dfs(i,j):
            grid[i][j] = "0"
            
            for i_add,j_add in dirs:
                new_i,new_j = i + i_add, j + j_add
                
                if(0<= new_i < len(grid) and
                  0 <= new_j < len(grid[0]) and
                  grid[new_i][new_j] == "1"):
                    dfs(new_i,new_j)
        
        res = 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    dfs(r,c)
                    res += 1
        
        return res