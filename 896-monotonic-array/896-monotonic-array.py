class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        if len(nums) <= 2:
            return True
        
        inc = []
        dec = []
        
        for i in range(0, len(nums) - 1):
            if nums[i + 1] >= nums[i]:
                inc.append(nums[i + 1])
            
            if nums[i + 1] <= nums[i]:
                dec.append(nums[i + 1])
            
                
        return (len(inc) == len(nums) - 1) or (len(dec) == len(nums) - 1)      