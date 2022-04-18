
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        que = deque()
        fresh = 0
        lvl = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    que.append((i,j,0))
                if grid[i][j] == 1:
                    fresh += 1
        while que:
            for i in range(len(que)):
                r,c,level = que.popleft()
                lvl = level
                for r_add,c_add in dirs:
                    new_r = r + r_add
                    new_c = c + c_add
                    if 0<= new_r <len(grid) and 0 <= new_c < len(grid[0]) and grid[new_r][new_c] == 1:
                        que.append((new_r,new_c,level+1))
                        fresh -= 1
                        grid[new_r][new_c] = 2
        if fresh != 0:
            return -1
        return lvl
                                   
                    
                        
                                   