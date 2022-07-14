class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        temp = 0
        idx = {}
        l = 0
        i = 0
        res = 0
        
        while i < len(nums):
            if nums[i] not in idx:
                temp += nums[i]
                idx[nums[i]] = i
                
            else:
                res = max(temp,res)
                nl = idx[nums[i]]
                temp += nums[i]
                while l <= nl:
                    temp -= nums[l]
                    l += 1
                    
                idx[nums[i]] = i
            i += 1
            
        res = max(temp,res)
        
        return res