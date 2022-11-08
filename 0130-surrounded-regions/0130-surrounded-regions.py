class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        
        for i in range(len(board)):
            if board[i][0] == "O":
                self.dfs(directions, board, i, 0)
            
            if board[i][-1] == "O":
                self.dfs(directions, board, i, len(board[0]) - 1)
        
        for i in range(len(board[0])):
            if board[0][i] == "O":
                self.dfs(directions, board, 0, i)
            
            if board[-1][i] == "O":
                self.dfs(directions, board, len(board) - 1, i)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 1:
                    board[i][j] = "O"
                
                elif board[i][j] == "O":
                    board[i][j] = "X"
        
        
    def isValid(self, grid, row, col):
        return (0 <= row < len(grid) and
                0 <= col < len(grid[0]) and 
                grid[row][col] == "O")
    
    def dfs(self, dirs, grid, row, col):
        
        grid[row][col] = 1
        
        for row_dir, col_dir in dirs:
            next_row = row + row_dir
            next_col = col + col_dir
            
            if self.isValid(grid, next_row, next_col):
                self.dfs(dirs, grid, next_row, next_col)