class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = deque()
        set1 = set(arr)
        res = 0
        if len(s) == 1:
            return 1
        
        for i in range(len(s)):
            if s[i] not in arr:
                set1.add(s[i])
                arr.append(s[i])
            
            else:
                res = max(len(arr),res)
                
                while arr[0] != s[i]:
                    arr.popleft()
                    
                arr.popleft()
                arr.append(s[i])
                set1 = set(arr)
        res = max(len(arr),res)
        
        return res
                
                