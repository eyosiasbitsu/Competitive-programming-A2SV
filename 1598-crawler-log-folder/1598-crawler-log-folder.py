class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        depth = 0
        
        for log in logs:
            if log == "./":
                continue
                
            if log == "../":
                depth -= 1
                depth = max(0, depth)
            
            else:
                depth += 1
        
        return depth