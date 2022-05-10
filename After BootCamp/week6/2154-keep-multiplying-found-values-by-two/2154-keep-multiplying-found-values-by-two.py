class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        set1 = set(nums)
        
        res = original
        
        while res in set1:
            res *= 2
        
        return res