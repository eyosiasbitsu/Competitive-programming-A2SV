class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        
        _sum = 0
        
        for i in range(len(nums)):
            _sum += nums[i]
            nums[i] = _sum
        
        min_average_index = -1
        min_average = float("inf")
        
        for i in range(len(nums)):
            first_average = nums[i] // (i + 1)
            last_average = (nums[-1] - nums[i]) // (len(nums) - i - 1) if i != len(nums) - 1 else 0
            
            if abs(first_average - last_average) < min_average:
                min_average = abs(first_average - last_average)
                min_average_index = i
        
        return min_average_index