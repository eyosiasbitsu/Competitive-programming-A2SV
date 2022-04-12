class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        outputStr = [0]*n
        for i in range(n):
            for j in range(n):
                if nums[i] > nums[j]:
                    outputStr[i] += 1
        return outputStr
                
