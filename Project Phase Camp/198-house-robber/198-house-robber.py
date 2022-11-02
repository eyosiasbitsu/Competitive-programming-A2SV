class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) <= 2:
            return max(nums)
        
        for i in range(2, len(nums)):
            nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
            nums[i - 1] = max(nums[i - 1], nums[i - 2])
            
        return max(nums[-1], nums[-2])