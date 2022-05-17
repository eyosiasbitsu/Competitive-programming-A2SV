class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        dirs = [(0,1),(1,0),(1,1),(-1,-1),(-1,0),(0,-1),(-1,1),(1,-1)]
        if grid[0][0] != 0:
            return -1
        
        cach = {}
        
        que = deque()
        que.append((0,0,1))
        grid[0][0] = 1
        
        while que:
            i,j,st = que.popleft()
            
            if (i,j) == (n-1,n-1):
                return st
            
            for i_add,j_add in dirs:
                new_i = i + i_add
                new_j = j + j_add
                
                if(0<= new_i< n and 
                   0 <= new_j < n and 
                   grid[new_i][new_j] == 0):
                    que.append((new_i,new_j,st+1))
                    grid[new_i][new_j] = 1
        
        return -1