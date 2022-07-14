class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = len(nums) + 1
        
        for i in range(len(nums)):
            if abs(nums[i]) <= len(nums):
                val = abs(nums[i])
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                return i + 1
        
        return len(nums) + 1