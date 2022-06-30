class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        target = nums[l//2]
        
        return sum(abs(n-target) for n in nums)