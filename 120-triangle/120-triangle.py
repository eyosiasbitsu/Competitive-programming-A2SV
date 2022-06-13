class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.cach = {}
        
        def dfs(i,l):
            if l == len(triangle) - 1:
                return triangle[l][i]
            
            if (i,l) not in self.cach:
                self.cach[(i,l)] = (triangle[l][i] +
                    min(dfs(i,l+1),dfs(i+1,l+1)))
                
            return self.cach[(i,l)]
        
        return dfs(0,0)
            