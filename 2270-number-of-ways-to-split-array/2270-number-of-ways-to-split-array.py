class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        _sum = 0
        for i in range(len(nums)):
            _sum += nums[i]
            nums[i] = _sum
        
        num_ways = 0
        for i in range(len(nums)):
            if i != len(nums) - 1 and nums[-1] - nums[i] <= nums[i]:
                num_ways += 1
        
        return num_ways