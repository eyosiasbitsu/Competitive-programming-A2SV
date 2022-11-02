class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        set1 = set(list(jewels))
        
        count = 0
        
        for c in stones:
            if c in set1:
                count += 1
        
        return count