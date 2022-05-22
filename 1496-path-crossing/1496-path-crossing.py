class Solution:
    def isPathCrossing(self, path: str) -> bool:
        dirs = {'N' : (0,1), 'S': (0,-1), 'E' : (1,0),'W': (-1,0)}
        
        seen = set()
        
        i,j = 0,0
        seen.add((0,0))
        
        for c in path:
            i += dirs[c][0]
            j += dirs[c][1]
            
            if (i,j) in seen:
                return True
            
            seen.add((i,j))
            
        return False