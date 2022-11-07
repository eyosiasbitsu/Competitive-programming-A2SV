class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxArea = 0
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    maxArea = max(maxArea, self.dfs(directions, grid, i, j))
        
        return maxArea
                    
    def isValid(self, grid, r, c, Row, Col):
        return (0 <= r < Row and 
               0 <= c < Col and
               grid[r][c] == 1)
    
    def dfs(self, dirs, grid, row, col):
        
        area = 1
        for r_dir, c_dir in dirs:
            next_row = r_dir + row
            next_col = c_dir + col
            
            if self.isValid(grid, next_row, next_col, len(grid), len(grid[0])):
                grid[next_row][next_col] = 0
                area += self.dfs(dirs, grid, next_row, next_col)
        
        return area
                
                
                
                
                
                
                
