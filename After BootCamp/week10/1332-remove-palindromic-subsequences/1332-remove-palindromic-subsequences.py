class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 2 - all(s[i] == s[~i] for i in range(len(s) // 2))