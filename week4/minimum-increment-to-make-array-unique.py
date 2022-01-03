class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        inc = 0
        if len(nums)==1:
            return 0
        for i in range(1,len(nums)):
            if nums[i] <= nums[i-1]:
                num = (abs(nums[i-1]-nums[i])+1)
                nums[i]+=num
                inc += num
        return inc
                