class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        
        self.dp = {}
        
        
        def dfs(idx, prev, count):
            
            if count > target:
                return float('inf')
            
            if idx == m:
                return 0 if count == target else float('inf')
            
            if (idx, prev, count) not in self.dp:
                if houses[idx] == 0:
                    temp = float('inf')
                    
                    for c in range(1, n + 1):
                        temp = min(temp, dfs(idx + 1, c, count + (c != prev)) + cost[idx][c - 1])
                        
                    self.dp[(idx, prev, count)] = temp
                
                else:
                    temp = None
                    temp = dfs(idx + 1, houses[idx], count + (houses[idx] != prev))
                        
                    self.dp[(idx, prev, count)] = temp
            
            return self.dp[(idx, prev, count)]
                        
        result = dfs(0, 0, 0)

        return result if result != float('inf') else -1
                        
                        
                        
                        
                        
                        
                