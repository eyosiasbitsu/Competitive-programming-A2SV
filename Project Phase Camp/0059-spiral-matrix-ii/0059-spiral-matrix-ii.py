class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        row_direction, col_direction = 0, 1
        result = [[0 for _ in range(n)] for _ in range(n)]
        
        current_row, current_col = 0, -1
        i = 0
        
        while i < n*n:
            next_row = current_row + row_direction
            next_col = current_col + col_direction
            
            if self.inbound(next_row, next_col, n) and \
                result[next_row][next_col] == 0:
                result[next_row][next_col] = i + 1
                
                i += 1
                current_row = next_row
                current_col = next_col
                
            else:
                row_direction, col_direction = -col_direction, row_direction
        
        return result
    
    def inbound(self, row, col, n):
        return 0 <= row < n and 0 <= col < n
                
                