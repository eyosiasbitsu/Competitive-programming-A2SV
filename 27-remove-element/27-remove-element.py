class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 
        i = 0
        
        if val not in nums:
            return len(nums)
        
        while i < len(nums):
            if nums[i] == val:
                j = i
                while j < len(nums) and nums[j] == val:
                    j += 1
                
                if j < len(nums):
                    nums[i], nums[j] = nums[j], nums[i]
                    
            i += 1
            
        return nums.index(val)