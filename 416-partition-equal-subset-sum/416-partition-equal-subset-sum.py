class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        
        if target % 2:
            return False
        
        target //= 2
        @cache
        def dp(target, i):
            if target == 0:
                return True
            
            if target < 0 or i == len(nums):
                return False
            
            return dp(target - nums[i], i + 1) or dp(target, i + 1)
        
        return dp(target, 0)