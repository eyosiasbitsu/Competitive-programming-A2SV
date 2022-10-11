class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        
        res = [-1 for _ in range(len(nums))]
        
        m = k
        l = 0
        r = 2*k + 1
        sm = 0
        
        if r <= len(nums):
            sm = sum(nums[l:r])
            res[m] = sm//(2*k + 1)
        
        while r < len(nums):
            sm += nums[r]
            sm -= nums[l]
            
            l += 1
            m += 1
            r += 1
            
            res[m] = sm // (2*k + 1)
        
        return res
            