class Solution:
    def smallestNumber(self, pattern: str) -> str:
        self.res = "999999999"
        
        def dfs(st, idx):
            if idx == len(pattern):
                if st < self.res:
                    self.res = st
                    
                return
            
            for i in range(1, 10):
                n = str(i)
                
                if not st:
                    dfs(st + n, idx + 1)
                
                else:
                    set1 = set(list(st))
                    if ((pattern[idx] == 'I' and st[-1] < n) or (pattern[idx] == 'D' and st[-1] > n)) and n not in set1:
                        call = dfs(st + n, idx + 1)
        dfs("", -1)
        return self.res