class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        m = nums[-1]
        n = 1
        
        for i in range(len(nums) - 1, - 1, -1):
            if nums[i] < m:
                n += 1
                m = nums[i]
                
            if n == 3:
                return m
        
        return nums[-1]