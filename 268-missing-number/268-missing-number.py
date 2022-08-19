class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num = 0
        
        for n in nums:
            num |= (int(2**(n - 1)))
        
        count = 0
        
        while num:
            if num & 1:
                count += 1
                num >>= 1
            
            else:
                return count + 1
        
        return 0 if count == len(nums) else len(nums)