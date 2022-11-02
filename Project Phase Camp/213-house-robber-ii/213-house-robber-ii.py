class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        
        return max(self.helper(nums[:-1]), self.helper(nums[1:]))
    
    def helper(self, arr):
        if len(arr) <= 2:
            return max(arr)
        
        for i in range(2,len(arr)):
            arr[i] = max(arr[i - 1], arr[i - 2] + arr[i])
            arr[i - 1] = max(arr[i - 1], arr[i - 2])
        
        return max(arr[-1], arr[-2])