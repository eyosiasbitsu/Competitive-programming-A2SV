class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        def GCD(a, b):
            if b == 0:
                return a
            
            return GCD(b, a%b)
        
        smallest = min(nums)
        largest = max(nums)
        
        return GCD(largest, smallest)