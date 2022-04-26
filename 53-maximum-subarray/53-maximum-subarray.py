class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefixSum = 0
        maxSub = nums[0]
        for n in nums:
            if(prefixSum < 0):
                prefixSum = 0
            prefixSum += n
            maxSub = max(maxSub, prefixSum)
        return maxSub