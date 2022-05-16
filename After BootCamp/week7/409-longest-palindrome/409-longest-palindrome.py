class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)
        
        for c in s:
            count[c] += 1
        
        n = 0
        for c in count:
            n += (count[c] - count[c] % 2)
        
        if n < len(s):
            n += 1
        
        return n