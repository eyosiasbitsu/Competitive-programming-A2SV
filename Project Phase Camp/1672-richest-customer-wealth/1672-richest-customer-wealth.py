class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = float("-inf")
        
        for i in range(len(accounts)):
            for j in range(1, len(accounts[0])):
                accounts[i][j] = accounts[i][j] + accounts[i][j - 1]
            
            res = max(res, accounts[i][-1])
        
        return res