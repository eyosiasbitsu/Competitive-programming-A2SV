class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        target = []
        
        for i in range(len(nums)):
            if not target:
                target.append(nums[i])
            
            else:
                idx = index[i]
                target = target[:idx] + [nums[i]] + target[idx:]
        
        return target