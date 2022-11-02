class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] != 1:
                return nums[i] - 1
            
        return len(nums) if nums[0] == 0 else 0