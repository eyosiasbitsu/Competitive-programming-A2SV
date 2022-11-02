class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        pigs = 0
        n = minutesToTest / minutesToDie + 1
        
        while n**pigs < buckets:
            pigs += 1
        
        return pigs