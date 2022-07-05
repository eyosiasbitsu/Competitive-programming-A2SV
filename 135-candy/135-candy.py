class Solution:
    def candy(self, ratings: List[int]) -> int:
        relative_to_left = [1]*len(ratings)
        relative_to_right = [1]*len(ratings)
        
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                relative_to_left[i] += relative_to_left[i-1]
        
        for i in range(len(ratings) - 2, -1,-1):
            if ratings[i] > ratings[i+1]:
                relative_to_right[i] += relative_to_right[i+1]
        
        res = 0
        
        for i in range(len(ratings)):
            res += max(relative_to_right[i], relative_to_left[i])
        
        return res
        