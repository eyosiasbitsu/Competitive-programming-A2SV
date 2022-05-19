class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ar = []
        st = ""
        
        for c in s:
            st += c
            if len(st) == k:
                ar.append(st)
                st = ""
        
        if 0 < len(st) < k:
            st += (fill*(k-len(st)))
            ar.append(st)
        
        return ar