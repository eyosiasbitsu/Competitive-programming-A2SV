class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        
        from collections import defaultdict
        from math import factorial as fac
        
        def C2(n):
            if n<2: return 0
            return (fac(n))//(2*fac(n-2))
        
        ans =0
        fir,sec = defaultdict(int),defaultdict(int)
        for x in arr:
            ans+=sec[target-x]
            fir[x]+=1
            for y in fir:
                if y==x: sec[x+y] += C2(fir[x])-C2(fir[x]-1)
                else: sec[x+y] += fir[y]

        return ans % ((10**9)+7)