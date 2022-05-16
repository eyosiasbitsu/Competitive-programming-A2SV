class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1 = version1.split(".")
        l2 = version2.split(".")
        
        for i in range(len(l1)):
            cur = l1[i]
            temp = 0
            
            for c in cur:
                temp = 10*temp + int(c)
            
            l1[i] = temp
            
        for i in range(len(l2)):
            cur = l2[i]
            temp = 0
            
            for c in cur:
                temp = 10*temp + int(c)
            
            l2[i] = temp
        
        i = 0
        
        while i < len(l2) and i < len(l1):
            if l2[i] > l1[i]:
                return -1
            if l1[i] > l2[i]:
                return 1
            
            i += 1
        
        while i < len(l2):
            if l2[i] != 0:
                return -1
            i += 1
        
        while i < len(l1):
            if l1[i] != 0:
                return 1
            i += 1
            
        return 0
        
        
        
                