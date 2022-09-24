class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            nums[i] = (nums[i], i)
        
        nums.sort()
        
        l = 0
        r=  len(nums) - 1
        
        while l < r:
            if nums[l][0] + nums[r][0] == target:
                return [nums[l][1], nums[r][1]]
            
            if nums[l][0] + nums[r][0] > target:
                r -= 1
            
            else:
                l += 1
