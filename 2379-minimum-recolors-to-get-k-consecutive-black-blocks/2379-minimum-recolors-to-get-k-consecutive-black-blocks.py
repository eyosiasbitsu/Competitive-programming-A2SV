class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        count = defaultdict(int)
        for i in range(k):
            count[blocks[i]] += 1
        
        l = 0
        res = count["W"]
        
        for r in range(k, len(blocks)):
            count[blocks[r]] += 1
            count[blocks[l]] -= 1
            l += 1
            
            res = min(res, count["W"])
        
        return res
            