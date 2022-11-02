class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            n = nums[i]
            while n < len(nums) and n != i:
                nums[i], nums[n] = nums[n], n
                n = nums[i]
                
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        
        return len(nums)