class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0
        
        while i < len(nums):
            n = 2
            val = nums[i]
            while n > 0 and i < len(nums) and nums[i] == val:
                i += 1
                n -= 1
            
            while i < len(nums) and nums[i] == val:
                nums[i] = 10**4 + 1
                i += 1
        
        nums.sort()
        
        res = 0
        
        for n in nums:
            if n > 10**4:
                return res
            
            res += 1
