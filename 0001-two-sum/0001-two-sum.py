class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for idx, num in enumerate(nums):
            nums[idx] = (num, idx)
        
        nums.sort()
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            temp_sum = nums[left][0] + nums[right][0]
            
            if temp_sum > target:
                right -= 1
            
            elif temp_sum < target:
                left += 1
            
            else:
                return [nums[left][1], nums[right][1]]
        
        return [-1, -1]
            
            
            
            
            
            