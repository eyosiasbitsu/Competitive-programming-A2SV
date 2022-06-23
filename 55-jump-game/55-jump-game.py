class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        if nums[0] == 0:
            return False
        
        r_idx = len(nums) - 1
        
        for i in range(len(nums) - 1,-1,-1):
            if nums[i] + i >= r_idx:
                r_idx = i
        
        if r_idx == 0: return True
        
        return False