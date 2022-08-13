class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total%2 != 0:
            return False
        
        target = total//2
        
        dp = [[0 for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        
        for i in range(1, len(nums) + 1):
            val = nums[i - 1]
            if val > target:
                return False
            
            for s in range(val):
                dp[i][s] = dp[i - 1][s]
                
            for j in range(val,target + 1):
                cur = val + dp[i - 1][j - val]
                
                if abs(target - cur) < abs(target - dp[i - 1][j]):
                    dp[i][j] = cur
                    
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[-1][-1] == target
                
                