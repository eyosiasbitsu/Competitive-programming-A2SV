class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        mycoins = 0
        count = 0
        for i in range(1,len(piles)-count,2): 
            if i <= len(piles):
                mycoins += piles[i]
                piles.pop()
                count+=1
        return mycoins
            