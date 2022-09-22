class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        def cyclic_sort():
            i = 0
            n = len(nums)
            
            while i < n:
                correct = nums[i] - 1
                
                if correct >= 0 and nums[i] != nums[correct]:
                    nums[i], nums[correct] = nums[correct], nums[i]
                
                else:
                    i += 1
            
        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] > len(nums):
                nums[i] = 0
        
        cyclic_sort()
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i+1
        
        return len(nums) + 1
    
    
    
    
    
    
    