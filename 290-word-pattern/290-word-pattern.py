class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ar = s.split()
        dict1 = {}
        dict2 = {}
        
        if len(pattern) != len(ar):
            return False
        
        for i in range(len(ar)):
            if ar[i] in dict1:
                if dict1[ar[i]] != pattern[i]:
                    return False
                
            if ar[i] not in dict1:
                if pattern[i] in dict2:
                    return False
                
                dict1[ar[i]] = pattern[i]
                dict2[pattern[i]] = ar[i]
            
        return True
        