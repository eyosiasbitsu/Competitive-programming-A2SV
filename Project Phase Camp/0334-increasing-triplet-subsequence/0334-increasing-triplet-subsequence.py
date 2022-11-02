class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        l, r = float("inf"), float("inf")
        
        for n in nums:
            if n <= l:
                l = n
            
            elif n <= r:
                r = n
            
            else:
                return True
        
        return False