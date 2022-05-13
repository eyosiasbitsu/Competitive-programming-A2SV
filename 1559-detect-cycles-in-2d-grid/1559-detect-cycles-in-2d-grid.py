class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        
        seen = set()
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        set1 = set()
        
        def dfs(i,j,par):
            if (i,j) in seen:
                return True
            
            seen.add((i,j))
            set1.add((i,j))
            count = False
            
            for n in range(len(dirs)):
                i_add,j_add = dirs[n]
                
                new_i,new_j = i + i_add, j + j_add
                
                if (0 <= new_i < len(grid) and
                    0 <= new_j < len(grid[0]) and
                    grid[new_i][new_j] == grid[i][j]):
                    if not par:
                        count |= dfs(new_i,new_j,(i,j))
                    elif (new_i,new_j) != par:
                        count |= dfs(new_i,new_j,(i,j))
                     
            seen.remove((i,j))
            
            return count
    
        for k in range(len(grid)):
            for l in range(len(grid[0])):
                if (k,l) not in set1 and dfs(k,l,None):
                    return True
                
        return False