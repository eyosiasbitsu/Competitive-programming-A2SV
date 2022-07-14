class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        
        for i in range(len(nums) - 1, 0, -2):
            res += nums[i - 1]
        
        return res