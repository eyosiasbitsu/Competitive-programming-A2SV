class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        if (len(needle) > len(haystack) or
            (len(needle) == len(haystack) and
             needle != haystack)):
            return -1
        
        for i in range(len(haystack)):
            if (i + len(needle) <= len(haystack) and
                haystack[i:i + len(needle)] == needle):
                return i
        
        return -1
        