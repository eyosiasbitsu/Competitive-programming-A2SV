class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [0]*m
        cols = [0]*n
        
        for i,j in indices:
            
            rows[i] += 1
            cols[j] += 1
            
        count = 0
        
        for i in range(m):
            for j in range(n):
                cur = cols[j] + rows[i]
                
                if cur % 2 != 0:
                    count += 1
                    
        return count