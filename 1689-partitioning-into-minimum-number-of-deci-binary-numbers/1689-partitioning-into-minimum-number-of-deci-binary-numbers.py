class Solution:
    def minPartitions(self, n: str) -> int:
        res = 0
        
        for num in n:
            res = max(int(num), res)
        
        return res