class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        dirs = [(-1,0),(0,-1)]
        
        for i in range(len(grid)):
            
            for j in range(len(grid[0])):
                temp = []
                
                for i_add,j_add in dirs:
                    
                    row = i + i_add
                    col = j + j_add
                    
                    if 0<= row < len(grid) and 0<= col < len(grid[0]):
                        temp.append(grid[row][col])
                        
                if not temp:
                    continue
                    
                grid[i][j] += min(temp)
                
        return grid[-1][-1]