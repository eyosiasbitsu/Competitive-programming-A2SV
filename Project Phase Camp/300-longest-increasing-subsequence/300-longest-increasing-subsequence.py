class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        small = float('inf')
        l = 0
        dp = {}
        
        def dfs(i):
            
            if i not in dp:
                temp = 0
                
                for j in range(i + 1,len(nums)):
                    if nums[j] > nums[i]:
                        temp = max(temp, dfs(j))
                
                dp[i] = 1 + temp
                
            return dp[i]
        
        for i in range(len(nums)):
            dfs(i)
            
        res = float("-inf")
        
        dfs(0)
        
        for i in dp:
            res = max(res, dp[i])

        return res
        
        
                    