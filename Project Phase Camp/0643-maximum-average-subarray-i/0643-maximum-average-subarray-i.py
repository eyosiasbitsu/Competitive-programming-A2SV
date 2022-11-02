class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        r = k
        l = 0
        sm = sum(nums[:r])
        
        res = sm / k
        
        while r < len(nums):
            sm -= nums[l]
            sm += nums[r]
            
            res = max(sm / k, res)
            
            l += 1
            r += 1
        
        return res