class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        st = [0 for _ in range(len(s))]
        
        for i in range(len(s)):
            st[indices[i]] = s[i]
        
        return "".join(st)