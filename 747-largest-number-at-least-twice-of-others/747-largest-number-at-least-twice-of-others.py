class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            if nums[0] <= 1:
                return 0
            
            return -1
        
        for i in range(len(nums)):
            nums[i] = (nums[i],i)
        
        nums.sort()
        
        if nums[-1][0] >= 2* nums[-2][0]:
            return nums[-1][1]
        
        return -1