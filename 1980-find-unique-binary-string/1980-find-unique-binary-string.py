class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        def cyclic_sort():
            i = 0
            n = len(nums)
            
            while i < n:
                correct = nums[i]
                if correct < len(nums) and nums[correct] != nums[i]:
                    nums[correct], nums[i] = nums[i], nums[correct]
                
                else:
                    i += 1
                
        l = len(nums[0])
        
        for i in range(len(nums)):
            nums[i] = int(nums[i], 2)
            
        print(nums)
        cyclic_sort()
        
        
        for i in range(len(nums)):
            if nums[i] != i:
                cur = "0"*l + bin(i)[2:]
                return cur[len(cur) - l :]
        
        cur = "0"*l + bin(len(nums))[2:]
        return cur[len(cur) - l :]
            
        
        
        
            
            
            