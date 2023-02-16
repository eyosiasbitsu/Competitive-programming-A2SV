class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        result = float("-inf")
        max_sum = float("-inf")

        for n in nums:
            max_sum = max(n, max_sum + n)
            result = max(result, max_sum)

        return result
