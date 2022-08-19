class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for n in nums:
            print(n, nums[n])
            if nums[abs(n)] < 0:
                return abs(n)
            
            nums[abs(n)] *= -1
        