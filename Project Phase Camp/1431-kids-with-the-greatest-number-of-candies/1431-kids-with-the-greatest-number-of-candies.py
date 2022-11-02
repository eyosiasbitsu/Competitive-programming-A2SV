class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        large = float("-inf")
        
        for c in candies:
            large = max(large, c)
        
        for i in range(len(candies)):
            if candies[i] + extraCandies >= large:
                candies[i] = True
                
            else:
                candies[i] = False
                
        return candies