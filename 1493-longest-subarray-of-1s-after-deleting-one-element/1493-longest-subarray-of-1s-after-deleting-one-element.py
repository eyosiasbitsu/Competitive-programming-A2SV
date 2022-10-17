class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        count = [0, 0]
        l = 0
        res = 0
        
        for r in range(len(nums)):
            count[nums[r]] += 1
            
            while count[0] > 1:
                count[nums[l]] -= 1
                l += 1
            
            res = max(count[1] - (count[0] == 0), res)    
        
        return res