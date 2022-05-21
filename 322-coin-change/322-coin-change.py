class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.dict1 = {}
        
        def helper(amount):
            
            if amount == 0:
                return 0
            if amount not in self.dict1:
                temp = float("inf")
                for i in range(len(coins)):
                    if amount -  coins[i] >= 0: 
                        temp2 = helper(amount-coins[i])
                        if temp2 < temp:
                            temp = temp2
                self.dict1[amount] = 1 + temp
            return self.dict1[amount]
        ans = helper(amount)
        return -1 if ans == float("inf") else ans