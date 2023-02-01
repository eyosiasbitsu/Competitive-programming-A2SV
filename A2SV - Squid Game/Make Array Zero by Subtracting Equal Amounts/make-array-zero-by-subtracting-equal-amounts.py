class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums = set(nums)
        
        if 0 in nums:
            nums.remove(0)
        
        return len(nums)
