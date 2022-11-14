class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        max_sum = float("-inf")
        
        for n in nums:
            cur_sum = max(0, cur_sum)
            cur_sum += n
            
            max_sum = max(max_sum, cur_sum)
        
        return max_sum