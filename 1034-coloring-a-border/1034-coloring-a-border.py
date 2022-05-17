class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        r,c = len(grid),len(grid[0])
        
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        ar = []
        
        que = deque()
        que.append((row,col))
        cul = grid[row][col]
        
        set1 = set()
        set1.add((row,col))
        
        while que:
            i,j = que.popleft()
            
            for i_add,j_add in dirs:
                new_i,new_j = i + i_add, j+ j_add
                
                if (0 <= new_i < r and
                    0 <= new_j < c and
                    grid[new_i][new_j] == cul and
                   (new_i,new_j) not in set1):
                    que.append((new_i,new_j))
                    set1.add((new_i,new_j)) 
                
                if (new_j <= new_i < 0 or 
                    new_i >= r or new_j >= c or
                    (new_i,new_j) not in set1):
                    ar.append((i,j))
        
        for i,j in ar:
            grid[i][j] = color
            
        return grid
