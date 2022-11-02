class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []
        res = []
        
        for n in nums:
            if n < 0:
                neg.append(n)
            
            else:
                pos.append(n)
        
        n = 0
        p = 0
        fn = False
        fp = True
        
        while p + n < len(nums):
            if fp:
                res.append(pos[p])
                p += 1
                fp = False
                fn = True
            
            else:
                res.append(neg[n])
                n += 1
                fp = True
                fn = False
        
        return res
        
        