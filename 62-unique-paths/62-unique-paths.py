class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = {}
        
        def path(r,c):
            if not 0 <= r < m or not 0 <= c < n:
                return 0
            
            if r == 0 and c == 0:
                return 1
            
            if (r,c) not in dp:
                dp[(r,c)] = path(r - 1,c) + path(r,c - 1)
            
            return dp[(r,c)]
        
        return path(m-1,n - 1)