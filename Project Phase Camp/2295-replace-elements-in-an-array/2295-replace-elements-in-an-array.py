class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        idx = {}
        
        for i in range(len(nums)):
            idx[nums[i]] = i
        
        for num, by in operations:
            nums[idx[num]] = by
            idx[by] = idx[num]
            del idx[num]
            
        return nums