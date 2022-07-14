class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        dp = [0]
        z = 0
        
        for n in nums:
            z += n
            dp.append(z)
        
        lookup = {v : i for i,v in enumerate(dp)}
        
        y = sum(nums) - x
        ans = - 1
        
        for l_val, l_idx in lookup.items():
            if l_val + y in lookup:
                ans = max(lookup[l_val + y]-l_idx,ans)
        
        return len(nums) - ans if ans != -1 else ans
        