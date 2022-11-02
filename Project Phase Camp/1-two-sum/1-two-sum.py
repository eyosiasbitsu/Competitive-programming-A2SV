class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i, n in enumerate(nums):
            nums[i] = (n,i)
        
        nums.sort()
        
        l = 0
        r = len(nums) - 1
        
        while l < r:
            temp = nums[l][0] + nums[r][0]
            
            if temp == target:
                return nums[l][1], nums[r][1]
            
            if temp > target:
                r -= 1
            
            else:
                l += 1
        
        