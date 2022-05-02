class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = ""
        s2 = ""
        
        for c in s:
            if not s1 and c == "#":
                continue
            if c == "#":
                s1 = s1[:-1]
            else:
                s1 += c
        for c in t:
            if not s2 and c == "#":
                continue
            if c == "#":
                s2 = s2[:-1]
            else:
                s2 += c
                
        return s1 == s2