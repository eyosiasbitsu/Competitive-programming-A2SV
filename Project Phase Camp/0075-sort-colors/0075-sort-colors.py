class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        count = { 0 : 0, 1 : 0, 2 : 0 }
        
        for number in nums:
            count[number] += 1
        
        idx = 0
        while idx < len(nums):
            if count[0]:
                nums[idx] = 0
                count[0] -= 1
            
            elif count[1]:
                nums[idx] = 1
                count[1] -= 1
            
            else:
                nums[idx] = 2
                count[2] -= 1
            
            idx += 1
        
                
                
                
                
                
                
                
                
                