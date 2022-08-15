class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        
        @lru_cache(None)
        def dp(l, r):
            if r - l < 0:
                return 0
            
            temp = 0
            
            for i in range(l, r + 1):
                cur = nums[l - 1]*nums[i]*nums[r + 1]
                cur += dp(l,i - 1)
                cur += dp(i + 1,r)
                temp = max(cur, temp)
            
            return temp
        
        return dp(1,len(nums) - 2)
        
    
    