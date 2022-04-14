class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        
        for k in range(len(nums)):
            nums[k] = (nums[k],k)
            
        nums.sort()
        
        while i <= j:
            temp = nums[i][0] + nums[j][0]
            if temp > target:
                j -= 1
                
            elif temp < target:
                i += 1
                
            elif temp == target:
                return [nums[i][1],nums[j][1]]