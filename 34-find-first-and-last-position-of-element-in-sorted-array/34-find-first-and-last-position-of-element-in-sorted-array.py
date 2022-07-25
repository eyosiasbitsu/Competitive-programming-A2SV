class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = -1
        high = -1
        
        for i in range(len(nums)):
            if nums[i] == target:
                low = i
                break
        
        for i in range(len(nums) - 1,-1,-1):
            if nums[i] == target:
                high = i
                break
        
        return [low,high]