class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        top_three = [float("-inf"), float("-inf"), float("-inf")]

        for n in nums:
            if n not in top_three and top_three[0] < n:
                top_three[0] = n
                top_three.sort()
        
        if top_three[0] != float("-inf"):
            return top_three[0]
        
        return top_three[2]
