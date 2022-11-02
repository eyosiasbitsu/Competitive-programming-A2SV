class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.sum = 0
        self.tempsum = 0
        
        def helper(i,j):
            grid[i][j] = 0
            self.tempsum += 1
            
            if i + 1 < len(grid) and grid[i + 1][j]==1:
                helper(i+1,j)
                
            if i - 1 >= 0 and grid[i - 1][j]==1:
                helper(i-1,j)
                
            if j + 1 < len(grid[0]) and grid[i][j+1]==1:
                helper(i , j + 1 )
                
            if j - 1 >= 0 and grid[i][j-1]==1:
                helper(i , j - 1 )
                
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    helper(i,j)
                    self.sum = max(self.sum,self.tempsum)
                    self.tempsum = 0
                    
        return self.sum