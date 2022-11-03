class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        count = 0
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "X":
                    count += 1
                    self.dfs(i, j, board)
        
        return count
        
    def dfs(self, row, col, grid):
        if not (0 <= row < len(grid)) or not (0<= col < len(grid[0])):
            return
        
        if grid[row][col] == ".":
            return
        
        grid[row][col] = "."
        self.dfs(row + 1, col, grid)
        self.dfs(row, col + 1, grid)