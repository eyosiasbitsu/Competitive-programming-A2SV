class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        minHeap = [(grid[0][0], 0, 0)]
        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        seen = set((0,0))
        
        while minHeap:
            time, cur_row, cur_col, = heapq.heappop(minHeap)
            
            if (cur_row, cur_col) == (len(grid) - 1, len(grid) - 1):
                return time
            
            for row_dir, col_dir in directions:
                next_row = cur_row + row_dir
                next_col = cur_col + col_dir
                
                if self.isValid(grid, next_row, next_col, seen):
                    next_time = max(grid[next_row][next_col], time)
                      
                    seen.add((next_row, next_col))
                    heapq.heappush(minHeap, (next_time, next_row, next_col))
        
    def isValid(self, grid, row, col, visited):
        return (0 <= row < len(grid) and
                    0 <= col < len(grid[0]) and
                        (row, col) not in visited)