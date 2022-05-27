class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = {}
        trusted_by = defaultdict(int)
        
        for p1,p2 in trust:
            if p1 not in trusts:
                trusts[p1] = (0,0)
            
            trusts[p1] = (trusts[p1][0] + 1, p2)
            trusted_by[p2] += 1
        
        for p in range(1,n+1):
            if (trusted_by[p] == n - 1 and
                (p not in trusts or 
                (trusts[p][0] == 0 or
                 trusts[p][1] == p))):
                return p
            
        return -1