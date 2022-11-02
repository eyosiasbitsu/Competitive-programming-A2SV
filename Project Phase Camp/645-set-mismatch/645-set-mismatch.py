class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        def cyclic_sort():
            i = 0
            n = len(nums)
            
            while i != n:
                correct = nums[i] - 1
                
                if nums[i] != nums[correct]:
                    nums[i], nums[correct] = nums[correct], nums[i]
                
                else:
                    i += 1
            
        cyclic_sort()
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return [nums[i], i + 1]