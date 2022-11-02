class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        que = deque([])
        fresh = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                
                if grid[i][j] == 2:
                    que.append((i,j))
        
        if fresh == 0:
            return 0
        
        res = -1
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        
        while que:
            size = len(que)
            
            for _ in range(size):
                r,c = que.popleft()
                
                for r_add, c_add in dirs:
                    new_r, new_c = r + r_add, c + c_add
                    
                    if (0<= new_r < len(grid) and
                            0 <= new_c < len(grid[0]) and
                                grid[new_r][new_c] == 1):
                        grid[new_r][new_c] = 2
                        que.append((new_r, new_c))
                        fresh -= 1
            
            res += 1
        
        return res if fresh == 0 else -1
        
        
        
        
        
        
        
        
        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                
            
            
            
            
            
            
            
            
            
            
            
            
            