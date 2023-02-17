class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        seen = set()
        candidate = -1
        idx = -1

        for i in range(len(s) - 1, -1, -1):
            if s[i] not in seen:
                candidate = s[i]
                idx = i
                seen.add(s[i])

        return idx
        
