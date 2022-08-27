class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        res = [-1 for _ in range(len(nums))]
        
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[(i + j)%len(nums)] > nums[i]:
                    res[i] = nums[(i + j)%len(nums)]
                    break
        
        return res