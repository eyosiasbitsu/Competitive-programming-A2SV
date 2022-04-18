class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = len(nums)
        i = 0
        
        while i < l:
            nums.append(nums[i])
            i += 1
            
        return nums