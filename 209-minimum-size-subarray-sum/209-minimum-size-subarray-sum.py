class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        res = float('inf')
        
        l = 0
        r = 0
        
        while r < len(nums):
            total += nums[r]
            r += 1
            
            while total >= target:
                total -= nums[l]
                res = min(r - l,res)
                l += 1
                    
        if total >= target:
            res = min(r - l, res)
            
        return res if res != float('inf') else 0
            