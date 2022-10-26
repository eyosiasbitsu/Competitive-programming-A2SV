class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [0 for _ in range(len(nums) + 1)]
    
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] = nums[i - 1] + prefix_sum[i - 1]

        prefix_sum_indexes = {}
        result = 0

        for i in range(len(prefix_sum)):
            n = prefix_sum[i]

            if n - k in prefix_sum_indexes:
                result += prefix_sum_indexes[n - k]

            prefix_sum_indexes[n] = 1 + prefix_sum_indexes.get(n, 0)

        return result