class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.cach = {}
        
        def dp(num):
            if num == 0:
                return 1
            
            if num < 0:
                return 0
            
            if num not in self.cach:
                self.cach[num] = 0
                for n in nums:
                    self.cach[num] += dp(num - n)
            
            return self.cach[num]
        
        return dp(target)
                