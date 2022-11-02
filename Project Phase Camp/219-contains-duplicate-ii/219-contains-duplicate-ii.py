class Solution:
    def containsNearbyDuplicate(self, nums: List[int], n: int) -> bool:
        if n == 0:
            return False
        
        idx = defaultdict(list)
        
        for i in range(len(nums)):
            idx[nums[i]].append(i)
        
        for k in idx:
            idx[k].sort()
        
        for k in idx:
            if len(idx[k]) <= 1:
                continue
                
            l = 0
            r = 1
            
            while r < len(idx[k]):
                if idx[k][r] - idx[k][l] <= n:
                    return True
                
                l += 1
                r += 1
        
        return False
                
                
                
                
                
                
                
                
                