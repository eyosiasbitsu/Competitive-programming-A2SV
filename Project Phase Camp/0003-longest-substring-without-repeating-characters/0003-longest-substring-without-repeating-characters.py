class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        sub = set()
        l = 0
        res = 0
        
        for i in range(len(s)):
            while s[i] in sub:
                sub.remove(s[l])
                l += 1
            
            sub.add(s[i])
            res = max(i - l + 1, res)
        
        return res