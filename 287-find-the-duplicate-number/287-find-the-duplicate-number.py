class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        def cyclic_sort():
            i = 0
            n = len(nums)
            
            while i != n:
                correct = nums[i] - 1
                
                if correct + 1 != nums[correct]:
                    nums[correct], nums[i] = nums[i], nums[correct]
                
                else:
                    i += 1
        
        cyclic_sort()
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return nums[i]
            
            
            
            
            
            
            
            