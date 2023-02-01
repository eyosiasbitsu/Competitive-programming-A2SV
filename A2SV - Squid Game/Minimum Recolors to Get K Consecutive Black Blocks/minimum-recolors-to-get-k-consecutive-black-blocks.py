class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        res = float("inf")
        count = { "B" : 0, "W" : 0}

        for i in range(k):
            count[blocks[i]] += 1
        
        res = min(res, count["W"])
        left = 0

        for right in range(k, len(blocks)):
            count[blocks[right]] += 1
            count[blocks[left]] -= 1

            res = min(res, count["W"])
            left += 1
            
        return res
