class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        count = self.countFresh(grid)
        if count[0] == 0:
            return 0
        
        queue = deque([])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        
        self.populateQueue(queue, grid)
        minutes = self.bfs(grid, directions, queue, count)
        
        if count[0] == 0:
            return minutes
        
        return -1
    
    def populateQueue(self, queue, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i,j))
        
    def countFresh(self, grid):
        count = [0]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count[0] += 1
        
        return count
    
    def isValid(self, grid, row, col):
        return ( 0 <= row < len(grid) and
                0 <= col < len(grid[0]) and
                grid[row][col] == 1)
    
    def bfs(self, grid, dirs, queue, count):
        step = -1
        
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for row_dir, col_dir in dirs:
                    next_row = row + row_dir
                    next_col = col + col_dir

                    if self.isValid(grid, next_row, next_col):
                        queue.append((next_row, next_col))
                        grid[next_row][next_col] = 2

                        count[0] -= 1
                    
            step += 1
        
        return step
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        