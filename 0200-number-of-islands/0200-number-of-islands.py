class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                print(r, c)
                if grid[r][c] == "1":
                    self.dfs(grid, directions, r, c)
                    count += 1
        
        return count
    
    def isValid(self, row, col, i, j, grid):
        return 0 <= i < row and \
                    0 <= j < col and \
                        grid[i][j] == "1"    
    
    def dfs(self, grid, directions, row, col):
        queue = [(row, col)]
        
        while queue:
            cur_row, cur_col = queue.pop()
            grid[cur_row][cur_col] = "0"
            
            for row_dir, col_dir in directions:
                new_row, new_col = cur_row + row_dir, cur_col + col_dir
                
                if self.isValid(len(grid), len(grid[0]), new_row, new_col, grid):
                    queue.append((new_row, new_col))
                                