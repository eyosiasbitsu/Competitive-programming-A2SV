class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        def cyclic_sort():
            i = 0
            n = len(nums)
            
            while i != n:
                correct = nums[i] - 1
                
                if nums[correct] != nums[i]:
                    nums[correct], nums[i] = nums[i], nums[correct]
                
                else:
                    i += 1
            
        cyclic_sort()
        res = []
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.append(i + 1)
        
        return res