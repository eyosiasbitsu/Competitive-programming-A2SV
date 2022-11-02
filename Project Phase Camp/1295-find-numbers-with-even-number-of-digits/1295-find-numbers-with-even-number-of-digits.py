class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        
        for n in nums:
            if 10 <= n <= 99 or 1000 <= n <= 9999 or n == 100000:
                res += 1
        
        return res