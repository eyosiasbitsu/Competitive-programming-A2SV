class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        nums.sort()
        
        l = len(nums) - 3
        r = len(nums) - 1
        
        while r >= 2:
            s1 = nums[r]
            s2 = nums[r - 1]
            s3 = nums[r - 2]
            
            if s3 + s2 > s1:
                return s1 + s2 + s3
            r -= 1
        
        return 0